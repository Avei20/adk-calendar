from typing import Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent
from agents.calendar_agent import prompt
from mcp_servers import MCPServers
from tools.get_current_datetime import tool
# from tools.greetings import greeting

def before_cb(context: CallbackContext):
    context.state['is_greeted'] = False
    return

root_agent = LlmAgent(
    name="simple_calendar_agent",
    model="gemini-2.0-flash",
    description="Agent who can arrange the time management centralized on Google Calendar",
    instruction=prompt.PROMPT,

    tools=[
        MCPServers.CalendarInternal,
        # MCPServers.Time,
        # MCPServers.DateTime,
       tool,
       # greeting,
    ],
    before_agent_callback=before_cb,
)
