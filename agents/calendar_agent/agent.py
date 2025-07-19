import datetime
import time

from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent
from agents.multi_calendar_agent import prompt
from mcp_servers import MCPServers
from tools.get_current_datetime import tool
# from tools.greetings import greeting

def before_cb(callback_context: CallbackContext):
    adk_states = callback_context.state
    adk_states['is_greeted'] = False

    utc_now = datetime.datetime.utcnow()

    # Calculate the UTC+7 offset in seconds (7 hours * 60 minutes * 60 seconds)
    utc_offset_seconds = 7 * 60 * 60

    # Create a timedelta object for the offset
    utc_offset = datetime.timedelta(seconds=utc_offset_seconds)

    # Calculate the Asia/Jakarta time
    jakarta_now = utc_now + utc_offset

    # Format the datetime in different standards
    iso_format = jakarta_now.isoformat()
    rfc_format = jakarta_now.strftime("%a, %d %b %Y %H:%M:%S +0700")  # RFC 2822 format, adjusting timezone offset manually
    timestamp = time.mktime(jakarta_now.timetuple())

    result = {
        "iso": iso_format,
        "rfc": rfc_format,
        "timestamp": timestamp,
        "datetime": jakarta_now,
        "timezone": "Asia/Jakarta",
    }

    adk_states['current_datetime'] = result

    return

root_agent = LlmAgent(
    name="calendar_agent",
    model="gemini-2.5-flash",
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
