from typing import Any
import os
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
            balance_drops = int(account_data["Balance"])
            balance_xrp =  drops_to_xrp(balance_drops)  # Convert drops to XRP
            sequence = account_data["Sequence"]
            return f"Account: {address}\nXRP Balance: {balance_xrp}\nSequence: {sequence}"
        else:
            error = response.result.get("error", "Unknown error")
            if error == "actNotFound":
                return f"Account {address} not found on the ledger."
            return f"Error retrieving account info: {error}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')