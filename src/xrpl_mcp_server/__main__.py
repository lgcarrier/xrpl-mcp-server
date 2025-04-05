from xrpl_mcp_server.server import mcp

print("🚀 Starting XRPL MCP Server...")
print("✨ Server provides tools for the XRP Ledger")

if __name__ == "__main__":
    print("✅ Running XRPL MCP Server on stdio transport...")
    mcp.run(transport='stdio')