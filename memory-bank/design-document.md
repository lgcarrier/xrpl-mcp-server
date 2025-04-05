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

The server exposes the following tools through the MCP interface:

1. **get_account_info**: Retrieve account information from the XRP Ledger
   - Input: address (XRP Ledger account address)
   - Output: Formatted account information including balance and sequence

2. **get_account_lines**: Retrieve trust lines for an XRP Ledger account
   - Input: 
     - address (XRP Ledger account address)
     - peer (optional, counterparty account address)
     - limit (optional, number of trust lines to return)
   - Output: JSON-formatted information about account trust lines

3. **get_account_nfts**: Retrieve NFTs owned by an XRP Ledger account
   - Input:
     - address (XRP Ledger account address)
     - limit (optional, number of NFTs to return) 
   - Output: JSON-formatted information about account's NFTs

4. **get_account_transactions**: Retrieve transaction history for an account
   - Input:
     - address (XRP Ledger account address)
     - limit (optional, number of transactions to return)
     - binary (optional, flag for binary format)
     - forward (optional, flag to search forward in history)
   - Output: JSON-formatted transaction history

5. **get_server_info**: Retrieve information about the connected XRPL server
   - Input: None
   - Output: JSON-formatted server information

6. **submit_transaction**: Submit a signed transaction to the XRP Ledger
   - Input: tx_blob (signed transaction blob in hexadecimal)
   - Output: JSON-formatted submission result

7. **get_transaction_info**: Retrieve information about a specific transaction
   - Input: transaction_hash (hash of the transaction)
   - Output: JSON-formatted transaction details

8. **get_book_offers**: Retrieve order book offers for a currency pair
   - Input:
     - taker_gets (currency the taker wants to receive)
     - taker_pays (currency the taker wants to pay)
     - limit (optional, number of offers to return)
   - Output: JSON-formatted order book offers

All tools have detailed documentation to guide LLMs on appropriate usage.

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

3. **Account Information Tools**: Tools for retrieving account data
   ```python
   @mcp.tool()
   async def get_account_info(address: str) -> str:
       request = AccountInfo(account=address)
       # Process request and return formatted response
       
   @mcp.tool()
   async def get_account_lines(address: str, peer: str = None, limit: int = None) -> str:
       # Process request and return JSON response
       
   @mcp.tool()
   async def get_account_nfts(address: str, limit: int = None) -> str:
       # Process request and return JSON response
       
   @mcp.tool()
   async def get_account_transactions(address: str, limit: int = None, binary: bool = False, forward: bool = False) -> str:
       # Process request and return JSON response
   ```

4. **Transaction Tools**: Tools for transaction operations
   ```python
   @mcp.tool()
   async def submit_transaction(tx_blob: str) -> str:
       # Process request and return JSON response
       
   @mcp.tool()
   async def get_transaction_info(transaction_hash: str) -> str:
       # Process request and return JSON response
   ```

5. **Market Data Tools**: Tools for market and server data
   ```python
   @mcp.tool()
   async def get_book_offers(taker_gets: dict, taker_pays: dict, limit: int = None) -> str:
       # Process request and return JSON response
       
   @mcp.tool()
   async def get_server_info() -> str:
       # Process request and return JSON response
   ```

### Environment Configuration

Required environment variables:
- XRPL_NODE_URL (optional, defaults to Ripple's public mainnet node)

### Response Formatting

The tools format responses in a structured way:
1. **Get Account Information**: Account address, XRP balance, and sequence number
2. **Trust Lines and NFTs**: JSON-formatted detailed information
3. **Transaction Data**: JSON-formatted transaction details
4. **Order Book Data**: JSON-formatted order offers
5. **Server Information**: JSON-formatted server status

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
6. Better human-readable formatting for JSON responses
7. Transaction building and local signing capabilities

## Integration Guidelines

1. Use with Claude Desktop via `mcp install`
2. Testing with MCP Inspector
3. Integration with custom LLM applications

## Deployment Considerations

1. Environment variable management
2. Resource requirements (minimal)
3. Monitoring for error rates
4. Uptime and availability metrics
