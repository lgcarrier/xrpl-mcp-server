# XRPL MCP Server

A Model Context Protocol (MCP) server that provides AI models with access to XRP Ledger data and functionality.

## Overview

XRPL MCP Server acts as a bridge between large language models (LLMs) like Claude and GPT and the XRP Ledger. It enables AI models to retrieve account information from the XRP Ledger through a standardized API interface.

## Features

- Get account information (balance, sequence number)
- Query trust lines and issued currencies
- View NFTs owned by accounts
- Retrieve transaction history
- Access order book data from the DEX
- Submit signed transactions to the network
- Get server status information
- Reliable XRP Ledger data access through MCP
- Easy integration with MCP-compatible AI applications

## Installation

### From Source

1. Clone this repository:
   ```
   git clone https://github.com/lgcarrier/xrpl-mcp-server.git
   cd xrpl-mcp-server
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Using pip

```
pip install xrpl-mcp-server
```

## Configuration

The server uses the following environment variables:

- `XRPL_NODE_URL` - XRP Ledger node URL (defaults to "https://s1.ripple.com:51234/")

## Usage

### Run from Source

Launch the server:

```
python -m xrpl_mcp_server
```

### Run as Installed Package

```
xrpl-mcp-server
```

### Using with Claude or Other MCP-Compatible AI Assistants

1. Install the MCP:
   ```
   mcp install xrpl-mcp-server
   ```

2. The XRPL tools will be available to Claude, allowing you to ask for XRP Ledger account information.

## Available Tools

### get_account_info

Retrieves information about an XRP Ledger account.

**Parameters:**
- `address` (string): The XRP Ledger account address (starts with "r")

**Returns:**
- Account balance in XRP
- Account sequence number

### get_account_lines

Retrieves trust lines for an XRP Ledger account.

**Parameters:**
- `address` (string): The XRP Ledger account address (starts with "r")
- `peer` (string, optional): Address of a counterparty account to filter results
- `limit` (integer, optional): Limit for the number of trust lines returned

**Returns:**
- JSON-formatted information about the account's trust lines

### get_account_nfts

Retrieves NFTs owned by an XRP Ledger account.

**Parameters:**
- `address` (string): The XRP Ledger account address (starts with "r")
- `limit` (integer, optional): Limit for the number of NFTs returned

**Returns:**
- JSON-formatted information about the account's NFTs

### get_account_transactions

Retrieves transaction history for an XRP Ledger account.

**Parameters:**
- `address` (string): The XRP Ledger account address (starts with "r")
- `limit` (integer, optional): Limit for the number of transactions returned
- `binary` (boolean, optional): Flag to return transactions in binary format (default False)
- `forward` (boolean, optional): Flag to search forward in ledger history (default False)

**Returns:**
- JSON-formatted information about the account's transaction history

### get_server_info

Retrieves information about the connected XRP Ledger server.

**Parameters:**
- None

**Returns:**
- JSON-formatted information about the XRP Ledger server

### submit_transaction

Submits a signed transaction blob to the XRP Ledger.

**Parameters:**
- `tx_blob` (string): The signed transaction blob in hexadecimal format

**Returns:**
- JSON-formatted submission result

### get_transaction_info

Retrieves information about a specific transaction.

**Parameters:**
- `transaction_hash` (string): The hash of the transaction

**Returns:**
- JSON-formatted transaction details

### get_book_offers

Retrieves order book offers for a currency pair on the DEX.

**Parameters:**
- `taker_gets` (object): Currency the taker wants to receive, e.g., `{"currency": "XRP"}` or `{"currency": "USD", "issuer": "r..."}`
- `taker_pays` (object): Currency the taker wants to pay, e.g., `{"currency": "EUR", "issuer": "r..."}` or `{"currency": "XRP"}`
- `limit` (integer, optional): Limit for the number of offers returned

**Returns:**
- JSON-formatted order book offers

## Examples

Ask Claude:

> What is the balance of the XRP account rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe?

Claude can then use the `get_account_info` tool to fetch this information directly from the XRP Ledger.

Example response:
```
Account: rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe
XRP Balance: 25.5
Sequence: 123456
```

Here's another example:

> What NFTs does account rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe own?

Claude can use the `get_account_nfts` tool to retrieve this information.

## Development

See the `memory-bank` directory for detailed documentation about architecture, coding rules, and implementation plans.

To set up the development environment:

```
pip install -e ".[dev]"
```

## License

MIT License
