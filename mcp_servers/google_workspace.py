
import os

from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    StdioConnectionParams,
    StdioServerParameters,
)

mcp = MCPToolset(
    connection_params=StdioServerParameters(
        command="docker",
        args=[
            "run",
            "--rm",
            "-i",
            "-p", "8080:8080",
            "-v", "~/.mcp/google-workspace-mcp:/app/config",
            "-v", "~/Documents/workspace-mcp-files:/app/workspace",
            "-e", "GOOGLE_CLIENT_ID",
            "-e", "GOOGLE_CLIENT_SECRET",
            "-e", "LOG_MODE=strict",
            "ghcr.io/aaronsb/google-workspace-mcp:latest"
        ],
    )
)
