from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("My First MCP Server")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


@mcp.tool()
def current_time() -> str:
    """Returns current time."""
    return str(datetime.now())