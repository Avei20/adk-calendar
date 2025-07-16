from google.adk.agents.llm_agent import LlmAgent
from agents.calendar_agent import prompt
from mcp_servers import MCPServers

root_agent = LlmAgent(
    name="simple_calendar_agent",
    model="gemini-2.0-flash",
    description="Agent who can arrange the time management centralized on Google Calendar",
    instruction=prompt.PROMPT,
    tools=[MCPServers.GoogleCalendar]
)
