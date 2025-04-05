# XRPL MCP Server Design Document

## Project Overview

The XRPL MCP Server is a Model Context Protocol (MCP) implementation that provides AI models with access to XRP Ledger's capabilities. This server acts as a bridge between large language models (LLMs) and the XRP Ledger, enabling more intelligent responses based on the ledger data.

## Goals and Requirements

### Primary Goals
1. Enable LLMs to access XRP Ledger through a standardized API
2. Provide real-time account information retrieval
3. Support seamless integration with MCP-compatible AI systems
4. Ensure reliability and proper error handling

### Functional Requirements
1. Get account information (balance, sequence)
2. Support configurable XRP Ledger node connections
3. Handle error cases gracefully with informative messages

### Non-Functional Requirements
1. Performance: Sub-second response times for most queries
2. Reliability: Graceful error handling for network issues
3. Usability: Simple installation and configuration process
4. Security: No exposure of sensitive system information

## Design Decisions

### API Design

The server exposes one primary tool through the MCP interface:

1. **get_account_info**: Retrieve account information from the XRP Ledger
   - Input: address (XRP Ledger account address)
   - Output: Formatted account information including balance and sequence

The tool has detailed documentation to guide LLMs on appropriate usage.

### Technology Stack

1. **FastMCP**: For creating MCP-compatible API endpoints
2. **xrpl-py**: Official Python library for XRP Ledger interaction
3. **AsyncJsonRpcClient**: For asynchronous communication with XRPL nodes
4. **Python**: Core programming language (3.10+)

### Data Flow

```
┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐
│   Input   │───▶│  Request  │───▶│   XRPL    │───▶│ Response  │
│ Processing│    │ Formation │    │   Node    │    │ Formatting│
└───────────┘    └───────────┘    └───────────┘    └───────────┘
```

1. Parse and validate input from LLM (account address)
2. Form appropriate API request to the XRP Ledger (AccountInfo)
3. Execute request with proper error handling
4. Process and format response for LLM consumption (human-readable text)

### Error Handling Strategy

1. Input validation with clear error messages
2. API error catching with specific error messages for known error codes
3. General exception handling for unexpected issues
4. Clear feedback to LLMs on what went wrong and how to fix it

### Security Considerations

1. API configurations stored in environment variables
2. Public node usage by default (no sensitive credentials)
3. Input validation to prevent malformed requests
4. Error messages designed to avoid leaking system information

## Implementation Details

### Core Classes and Functions

1. **FastMCP Server**: Main application entry point
   ```python
   mcp = FastMCP("xrpl")
   ```

2. **XRPL Client**: Connection to XRP Ledger
   ```python
   XRPL_NODE_URL = os.getenv("XRPL_NODE_URL", "https://s1.ripple.com:51234/")
   XRPL_CLIENT = AsyncJsonRpcClient(XRPL_NODE_URL)
   ```

3. **get_account_info**: Tool for retrieving account data
   ```python
   @mcp.tool()
   async def get_account_info(address: str) -> str:
       request = AccountInfo(account=address)
       # Process request and return formatted response
   ```

### Environment Configuration

Required environment variables:
- XRPL_NODE_URL (optional, defaults to Ripple's public mainnet node)

### Response Formatting

The tool formats responses in a structured way:
1. **Get Account Information**: Account address, XRP balance, and sequence number

## Testing Strategy

1. Unit tests for function logic
2. Integration tests with mocked XRPL responses
3. End-to-end tests with testnet connections
4. Error case testing with various failure scenarios

## Future Enhancements

1. Support for more XRPL features:
   - Transaction submission
   - NFT operations
   - DEX interactions
2. Multi-network support (mainnet, testnet, devnet)
3. Webhook notifications for ledger events
4. Extended authentication options
5. Support for WebSocket connections

## Integration Guidelines

1. Use with Claude Desktop via `mcp install`
2. Testing with MCP Inspector
3. Integration with custom LLM applications

## Deployment Considerations

1. Environment variable management
2. Resource requirements (minimal)
3. Monitoring for error rates
4. Uptime and availability metrics
