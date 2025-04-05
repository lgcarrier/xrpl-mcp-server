# XRPL MCP Server

A Model Context Protocol (MCP) server that provides AI models with access to XRP Ledger data and functionality.

## Overview

XRPL MCP Server acts as a bridge between large language models (LLMs) like Claude and GPT and the XRP Ledger. It enables AI models to retrieve account information from the XRP Ledger through a standardized API interface.

## Features

- Get account information (balance, sequence number)
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

## Development

See the `memory-bank` directory for detailed documentation about architecture, coding rules, and implementation plans.

To set up the development environment:

```
pip install -e ".[dev]"
```

## License

MIT License
