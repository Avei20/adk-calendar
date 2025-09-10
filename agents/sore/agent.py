import datetime
import time

from typing import Optional
from google import adk
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from . import prompt
from mcp_servers import MCPServers
from tools.get_current_datetime import tool
from tools.greetings import greeting
from google.genai import types

# def before_cb(context: CallbackContext):
#     context.state['is_greeted'] = False
#     return

def greeting_agent_cb(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Logs entry and checks 'skip_llm_agent' in session state.
    If True, returns Content to skip the agent's execution.
    If False or not present, returns None to allow execution.
    """
    adk_state = callback_context.state

    is_greeted = adk_state.get("is_greeted", False)

    if not is_greeted:
        adk_state["is_greeted"] = True
        return types.Content(
            parts=[types.Part(text="Hai! Aku Sore. Istri kamu dari masa depan.")],
            role="model" # Assign model role to the overriding response
        )
    return None

def greeting_model_cb(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    adk_state = callback_context.state

    is_greeted = adk_state.get("is_greeted", False)

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

    adk_state['current_datetime'] = result

    if not is_greeted:
        adk_state['is_greeted'] = True
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="Hai! Aku Sore. Istri kamu dari masa depan.")],
            )
        )
    return None

root_agent = LlmAgent(
    name="sore",
    model="gemini-2.5-pro",
    description="Agent who can arrange the time management centralized on Google Calendar",
    instruction=prompt.PROMPT,
    tools=[
        MCPServers.CalendarInternal,
        # MCPServers.Time,
        # MCPServers.DateTime,
       tool,
       greeting,
    ],
    before_model_callback=greeting_model_cb,
)
