from typing import Any
import os
from decimal import Decimal
from mcp.server.fastmcp import FastMCP
from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.requests import AccountInfo
from xrpl.utils.xrp_conversions import drops_to_xrp

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