# XRPL MCP Server

A Model Context Protocol (MCP) server that provides AI models with access to XRP Ledger data and functionality.

## Overview

XRPL MCP Server acts as a bridge between large language models (LLMs) like Claude and GPT and the XRP Ledger. It enables AI models to retrieve account information from the XRP Ledger through a standardized API interface.

## Features

- Get account information (balance, sequence number)
- Reliable XRP Ledger data access through MCP
- Easy integration with MCP-compatible AI applications

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/xrpl-mcp-server.git
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

## Configuration

The server uses the following environment variables:

- `XRPL_NODE_URL` - XRP Ledger node URL (defaults to "https://s1.ripple.com:51234/")

## Usage

Run the server:

```
python src/server.py
```

### Using with Claude Desktop

1. Install the MCP:
   ```
   mcp install /path/to/xrpl-mcp-server
   ```

2. The XRPL tools will be available to Claude, allowing you to ask for XRP Ledger account information.

## Examples

Ask Claude:

> What is the balance of the XRP account rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe?

Claude can then use the `get_account_info` tool to fetch this information directly from the XRP Ledger.

## Development

See the `memory-bank` directory for detailed documentation about architecture, coding rules, and implementation plans.

## License

[Specify your license here]
