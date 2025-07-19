
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
)
from mcp import StdioServerParameters

mcp = MCPToolset(
    connection_params=StdioServerParameters(
        command="uvx",
        args= ["google-calendar-mcp"],
        env={
            "GOOGLE_APPLICATION_CREDENTIALS": "/home/Users/GithubRepo/playground/adk-calendar/key.json",
            "GOOGLE_CALENDAR_ID": "muhammadabdulazizalghofari@gmail.com"
        }
    )
# tool_filter=["calendar_list_accounts"],
)
