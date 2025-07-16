from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp.client.stdio import StdioServerParameters


mcp = MCPToolset(
    connection_params=StdioServerParameters(
        command="uvx",
        args=["mcp-datetime"]
    )
)
