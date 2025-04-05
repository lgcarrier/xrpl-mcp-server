# XRPL MCP Server Coding Rules

## Code Style & Formatting

1. **Python Standards**
   - Follow PEP 8 style guide for Python code
   - Use 4 spaces for indentation (no tabs)
   - Keep line length to maximum 100 characters
   - Use appropriate docstrings for all modules, classes and functions
   - Use Google-style docstrings with parameter descriptions

2. **Naming Conventions**
   - Use `snake_case` for variables, functions, and methods
   - Use `PascalCase` for classes
   - Use `UPPER_CASE` for constants and environment variables
   - Use descriptive names that clearly indicate purpose
   - Prefix environment variables with `XRPL_` for clarity

## Project Structure

1. **Module Organization**
   - Keep server.py as the main entry point
   - Use separate modules for different XRPL feature categories
   - Group related functions and classes in the same file
   - Keep files focused on a single responsibility
   - Use relative imports for project modules

2. **File Structure**
   - Maximum file size: 400 lines (split larger files)
   - Maintain a flat hierarchy with minimal nesting
   - Organize imports at the top of each file in groups:
     - Standard library (e.g., os, typing)
     - External dependencies (e.g., mcp, xrpl)
     - Internal project modules

## Error Handling

1. **Exception Management**
   - Use try/except blocks for XRPL API operations
   - Check response.is_successful() for API responses
   - Handle specific error codes from XRP Ledger
   - Always provide clear, user-friendly error messages
   - Ensure graceful degradation on API failures

2. **Status Codes**
   - Return appropriate error messages for API failures
   - Include context in error messages (e.g., "Account not found")
   - Provide actionable information when possible

## API Design

1. **Function Signatures**
   - Use typing hints for all parameters and return values
   - Document parameters with clear descriptions in docstrings
   - Default values should be immutable (no `{}` or `[]` as defaults)
   - Keep parameter lists short and focused

2. **Tool Design**
   - Each MCP tool should have a clear, focused purpose
   - Include detailed docstrings that explain when to use each tool
   - Provide examples in documentation where helpful
   - Return formatted strings for human readability

## Testing

1. **Test Coverage**
   - Maintain minimum 80% code coverage
   - Write unit tests for all API functions
   - Include both positive and negative test cases
   - Mock external XRPL API calls for deterministic tests

2. **Test Organization**
   - Follow test file naming: `test_<module_name>.py`
   - Group tests by functionality
   - Use descriptive test names that indicate what is being tested
   - Include tests for error handling cases

## Asynchronous Code

1. **Async Patterns**
   - Use `async/await` syntax for all XRPL API operations
   - Properly handle timeouts for external API calls
   - Use AsyncJsonRpcClient for all XRPL interactions
   - Avoid blocking operations in async code

2. **Resource Management**
   - Use async context managers (`async with`) when appropriate
   - Initialize XRPL client at module level for reuse
   - Set reasonable timeouts for all API calls
   - Handle connection errors appropriately

## Security

1. **Data Protection**
   - Never hardcode sensitive data (node URLs, credentials)
   - Use environment variables for configuration
   - Validate and sanitize all user inputs (account addresses)
   - Use HTTPS for all external API calls

2. **Code Security**
   - Validate input parameters before making API calls
   - Don't use `eval()` or similar potentially unsafe functions
   - Check for security vulnerabilities in dependencies
   - Avoid exposing detailed error information to users

## Documentation

1. **Code Documentation**
   - Each function should have a docstring following Google style
   - Include Args, Returns, and Raises sections in docstrings
   - Document parameter types and expected values
   - Comment complex logic or non-obvious decisions

2. **User Documentation**
   - Maintain clear README with installation and usage instructions
   - Document environment variables and configuration options
   - Provide examples for each MCP tool
   - Include troubleshooting information for common issues

## XRP Ledger Specific Guidelines

1. **API Usage**
   - Use the xrpl-py library for all XRPL interactions
   - Follow XRPL best practices for API calls
   - Use appropriate request models (e.g., AccountInfo)
   - Convert values to human-readable format (e.g., drops_to_xrp)
