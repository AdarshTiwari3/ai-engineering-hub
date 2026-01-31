# create simple MCP server

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("simple-mcp-server")


@mcp.tool()
def add_values(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def say_hello(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    print("Running simple MCP server")

    mcp.run()
