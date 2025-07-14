from google.adk.agents import LlmAgent
from mcp_servers import MCPServers


root_agent = LlmAgent(
    name="normal_agent",
    model="gemini-2.0-flash",
    tools=[
        # MCPServers.Time,
        # MCPServers.GoogleCalendar,
        # MCPServers.GoogleWorkspace,
        MCPServers.MCPCalendarRemote,
    ]
)
