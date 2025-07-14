from google.adk.agents import LlmAgent
from . import prompt
from calendar_agent.context import use_context

from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    StdioServerParameters,
    StdioConnectionParams,
)

event_agent = LlmAgent(
    name="event_management_agent",
    model="gemini-2.0-flash",
    description="",
    instruction=prompt.PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@cocal/google-calendar-mcp"],
                    env={"GOOGLE_OAUTH_CREDENTIALS": "/app/key.json"},
                )
            )
            # tool_filter=["calendar_list_accounts"],
        ),
        use_context,
    ],
)
