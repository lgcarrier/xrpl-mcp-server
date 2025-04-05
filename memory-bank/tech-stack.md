# XRPL MCP Server Tech Stack

## Programming Language

- **Python 3.10+**: Core programming language
  - Type hints for better code quality and IDE support
  - Asyncio for asynchronous operations
  - Modern language features (dataclasses, f-strings, etc.)

## Framework & Libraries

### Core Framework
- **FastMCP (1.5.0+)**: Model Context Protocol implementation
  - Tool registration and management
  - Request handling and validation
  - Response formatting

### XRP Ledger Integration
- **xrpl-py**: Official Python library for XRP Ledger interaction
  - AsyncJsonRpcClient for async communication with XRPL
  - Request models for structured API calls
  - Utilities for data conversion (e.g., drops_to_xrp)

## Development Tools

### Environment Management
- **venv**: Python virtual environment management
  - Isolates dependencies
  - Ensures reproducible environments

### Version Control
- **Git**: Source code management
  - Feature branches for development
  - Pull requests for code review

## Deployment Options

### Direct Execution
- **Python Interpreter**: Run directly with Python
  - Standard I/O for MCP communication

### Claude Desktop Integration
- **MCP Install**: Direct installation in Claude Desktop
  - Local execution with AI integration

## Infrastructure

### XRP Ledger Connectivity
- **Public Nodes**: Default connection to Ripple's public nodes
  - No additional infrastructure required
  - Configurable for private node connections

### Security
- **Environment Variables**: Configuration management
  - No hardcoded credentials or sensitive values
