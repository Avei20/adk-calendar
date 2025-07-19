from mcp_servers.calendar_built_in import get_calendar_filter
from google.adk.agents import LlmAgent
from . import prompt
from multi_calendar_agent.context import use_context

from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    StdioServerParameters,
    StdioConnectionParams,
)

agenda_discussion_agent = LlmAgent(
    name="agenda_discussion_management_agent",
    model="gemini-2.0-flash",
    description="",
    instruction=prompt.PROMPT,
    tools=[
        get_calendar_filter(['']),
            # tool_filter=["calendar_list_accounts"],
        # ),
        use_context,
    ],
)
