# XRPL MCP Server Architecture

## System Overview

The XRPL MCP Server is a Model Context Protocol server that provides a bridge between AI applications and the XRP Ledger's capabilities. It enables LLMs to access structured information from the XRP Ledger through a standardized API.

## High-Level Architecture

```
┌───────────────┐     ┌───────────────────────┐     ┌────────────────────┐
│ AI Application│────▶│    XRPL MCP Server    │────▶│ XRPL Python SDK    │
│ (Claude/GPT)  │◀────│ (FastMCP API Gateway) │◀────│ (Account Info)     │
└───────────────┘     └───────────────────────┘     └────────────────────┘
                                                            │
                                                            ▼
                                                    ┌────────────────────┐
                                                    │    XRP Ledger      │
                                                    │    Network         │
                                                    └────────────────────┘
```

## Components

### 1. FastMCP API Gateway
- Exposes MCP-compatible endpoints for AI applications
- Handles request validation and error handling
- Manages tool registration and execution

### 2. XRPL Integration Layer
- Uses xrpl-py SDK to communicate with the XRP Ledger
- Handles data conversion between MCP format and XRPL format
- Provides error handling for API failures

### 3. Service Modules
- **Get Account Information**: Retrieves account balance and sequence from the ledger
- Future modules will provide additional XRPL capabilities

## Data Flow

1. An LLM or AI application makes a request to the MCP server via standard I/O or HTTP
2. The server validates the request and extracts parameters (e.g., account address)
3. The appropriate service module is invoked based on the tool called
4. The xrpl-py SDK formats and sends a request to the XRP Ledger node
5. The ledger response is processed, formatted, and returned through the MCP protocol
6. The AI application receives the structured data and can incorporate it into responses

## Authentication & Security

- Connection to public XRPL nodes requires no authentication
- Environment variables are used for configuration to avoid hardcoding
- Error handling prevents exposing sensitive system information
- Input validation helps prevent malformed requests

## Scalability Considerations

- Asynchronous request processing enables handling multiple concurrent requests
- Configurable XRPL node URLs allow for load balancing and failover
- JSON-RPC client connection pooling reduces overhead

## Integration Points

- MCP Inspector for testing/debugging
- Claude Desktop for direct installation
- Any MCP-compatible AI application
- XRP Ledger nodes (public or private)
