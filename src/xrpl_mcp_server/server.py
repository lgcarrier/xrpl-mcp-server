from typing import Any
import os
from decimal import Decimal
from mcp.server.fastmcp import FastMCP
from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.requests import (
    AccountInfo,
    AccountLines,
    AccountNFTs,
    AccountTx,
    BookOffers,
    ServerInfo,
    Submit,
    Tx,
)
from xrpl.utils.xrp_conversions import drops_to_xrp
import json # Added import for JSON handling

# Initialize FastMCP server
mcp = FastMCP("xrpl")

# Initialize XRP Ledger client with a configurable node URL
# Default to Ripple's public mainnet node if no environment variable is set
XRPL_NODE_URL = os.getenv("XRPL_NODE_URL", "https://s1.ripple.com:51234/")
XRPL_CLIENT = AsyncJsonRpcClient(XRPL_NODE_URL)

# Custom function to safely convert drops to XRP regardless of input type
def drops_to_xrp_safe(drops) -> Decimal:
    """Safely convert drops to XRP handling both string and integer inputs."""
    # Ensure we're working with a string
    drops_str = str(drops)
    # The standard conversion is 1 XRP = 1,000,000 drops
    return Decimal(drops_str) / Decimal("1000000")

@mcp.tool()
async def get_account_info(address: str) -> str:
    """Get information about an XRP Ledger account.

    Args:
        address: The XRP Ledger account address (e.g., r...)

    Returns:
        A string with the account's balance and sequence number, or an error message.
    """
    request = AccountInfo(account=address)
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            account_data = response.result["account_data"]
            balance_drops = account_data["Balance"]
            # Use our custom safe function instead of the xrpl-py utility
            balance_xrp = drops_to_xrp_safe(balance_drops)
            sequence = account_data["Sequence"]
            return f"Account: {address}\nXRP Balance: {balance_xrp}\nSequence: {sequence}"
        else:
            error = response.result.get("error", "Unknown error")
            if error == "actNotFound":
                return f"Account {address} not found on the ledger."
            return f"Error retrieving account info: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@mcp.tool()
async def get_account_lines(address: str, peer: str = None, limit: int = None) -> str:
    """Get the trust lines for an XRP Ledger account.

    Args:
        address: The XRP Ledger account address (e.g., r...).
        peer: Optional address of a counterparty account to filter results.
        limit: Optional limit for the number of trust lines returned.

    Returns:
        A JSON string with the account's trust lines, or an error message.
    """
    kwargs = {"account": address, "ledger_index": "validated"}
    if peer:
        kwargs["peer"] = peer
    if limit is not None:
        kwargs["limit"] = limit
    request = AccountLines(**kwargs)
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            return json.dumps(response.result, indent=2)
        else:
            error = response.result.get("error", "Unknown error")
            if error == "actNotFound":
                return f"Account {address} not found on the ledger."
            return f"Error retrieving account lines: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@mcp.tool()
async def get_account_nfts(address: str, limit: int = None) -> str:
    """Get the NFTs owned by an XRP Ledger account.

    Args:
        address: The XRP Ledger account address (e.g., r...).
        limit: Optional limit for the number of NFTs returned.

    Returns:
        A JSON string with the account's NFTs, or an error message.
    """
    kwargs = {"account": address, "ledger_index": "validated"}
    if limit is not None:
        kwargs["limit"] = limit
    request = AccountNFTs(**kwargs)
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            return json.dumps(response.result, indent=2)
        else:
            error = response.result.get("error", "Unknown error")
            if error == "actNotFound":
                return f"Account {address} not found on the ledger."
            return f"Error retrieving account NFTs: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@mcp.tool()
async def get_account_transactions(address: str, limit: int = None, binary: bool = False, forward: bool = False) -> str:
    """Get the transaction history for an XRP Ledger account.

    Args:
        address: The XRP Ledger account address (e.g., r...).
        limit: Optional limit for the number of transactions returned.
        binary: Optional flag to return transactions in binary format (default False).
        forward: Optional flag to search forward in ledger history (default False).


    Returns:
        A JSON string with the account's transaction history, or an error message.
    """
    kwargs = {"account": address, "ledger_index": "validated"}
    if limit is not None:
        kwargs["limit"] = limit
    if binary:
        kwargs["binary"] = binary
    if forward:
        kwargs["forward"] = forward
    request = AccountTx(**kwargs)
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            return json.dumps(response.result, indent=2)
        else:
            error = response.result.get("error", "Unknown error")
            if error == "actNotFound":
                return f"Account {address} not found on the ledger."
            return f"Error retrieving account transactions: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@mcp.tool()
async def get_server_info() -> str:
    """Get information about the connected XRP Ledger server.

    Returns:
        A JSON string with the server information, or an error message.
    """
    request = ServerInfo()
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            return json.dumps(response.result, indent=2)
        else:
            error = response.result.get("error", "Unknown error")
            return f"Error retrieving server info: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@mcp.tool()
async def submit_transaction(tx_blob: str) -> str:
    """Submit a signed transaction blob to the XRP Ledger.

    Args:
        tx_blob: The signed transaction blob in hexadecimal format.

    Returns:
        A JSON string with the submission result, or an error message.
    """
    request = Submit(tx_blob=tx_blob)
    try:
        response = await XRPL_CLIENT.request(request)
        # Note: Submit response structure differs slightly
        return json.dumps(response.result, indent=2)
    except Exception as e:
        return f"Exception occurred during submission: {str(e)}"

@mcp.tool()
async def get_transaction_info(transaction_hash: str) -> str:
    """Get information about a specific transaction by its hash.

    Args:
        transaction_hash: The hash of the transaction.

    Returns:
        A JSON string with the transaction details, or an error message.
    """
    request = Tx(transaction=transaction_hash)
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            return json.dumps(response.result, indent=2)
        else:
            error = response.result.get("error", "Unknown error")
            # Common error for transaction not found
            if error == "txnNotFound":
                 return f"Transaction {transaction_hash} not found."
            return f"Error retrieving transaction info: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@mcp.tool()
async def get_book_offers(taker_gets: dict, taker_pays: dict, limit: int = None) -> str:
    """Get the order book offers for a currency pair on the DEX.

    Args:
        taker_gets: A dictionary defining the currency the taker wants to receive.
                    Example: {"currency": "XRP"} or {"currency": "USD", "issuer": "r..."}
        taker_pays: A dictionary defining the currency the taker wants to pay.
                    Example: {"currency": "EUR", "issuer": "r..."} or {"currency": "XRP"}
        limit: Optional limit for the number of offers returned.

    Returns:
        A JSON string with the order book offers, or an error message.
    """
    kwargs = {"taker_gets": taker_gets, "taker_pays": taker_pays, "ledger_index": "validated"}
    if limit is not None:
        kwargs["limit"] = limit
    request = BookOffers(**kwargs)
    try:
        response = await XRPL_CLIENT.request(request)
        if response.is_successful():
            return json.dumps(response.result, indent=2)
        else:
            error = response.result.get("error", "Unknown error")
            return f"Error retrieving book offers: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"