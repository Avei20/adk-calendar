from google.adk.agents.llm_agent import LlmAgent
from . import prompt
from mcp_servers import MCPServers
from tools.get_current_datetime import tool
from tools.greetings import greeting

root_agent = LlmAgent(
    name="sore",
    model="gemini-2.0-flash-lite",
    description="Agent who can arrange the time management centralized on Google Calendar",
    instruction=prompt.PROMPT,
    tools=[
        MCPServers.CalendarInternal,
        # MCPServers.Time,
        # MCPServers.DateTime,
       tool,
       greeting,
    ],
)
