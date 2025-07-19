from google.adk.agents import LlmAgent
from mcp_servers import MCPServers
from . import prompt

root_agent = LlmAgent(
    name="normal_agent",
    model="gemini-2.0-flash",
    instruction=prompt.PROMPT,
    # tools=MCPServers.CalendarInternal.get_tools(''),
    tools=[
        MCPServers.CalendarInternal,
        # MCPServers.CalendarInternal.get_tool(),
        # MCPServers.MCPCalendarRemote,
    ]
)
