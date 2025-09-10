from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    StdioServerParameters,
)

mcp = MCPToolset(
    connection_params=StdioServerParameters(
        command="uv",
        args=[
            "run",
            "-m",
            "paper_search_mcp.server"
        ]
    )
)
