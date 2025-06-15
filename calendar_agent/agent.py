import datetime
from enum import Enum
from typing import Literal, Dict

from pydantic import BaseModel
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from . import prompt
from .sub_agent.agenda_task.agent import agenda_task_agent
from .sub_agent.event.agent import event_agent
from .sub_agent.agenda_discussion.agent import agenda_discussion_agent
from . import context

from google.adk.sessions import DatabaseSessionService

# Example using a local SQLite file:
db_url = "sqlite:///../data.db"
session_service = DatabaseSessionService(db_url=db_url)


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "jakarta":
        tz_identifier = "Asia/Jakarta"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}


def session_init_callback(callback_context, **kwargs):
    current_datetime = datetime.datetime.now()
    user_email = callback_context.state.get(
        "user:email", "muhammadabdulazizalghofari@gmail.com"
    )
    timezone_name = callback_context.state.get("user:timezone", "Asia/Jakarta")

    callback_context.state["current_datetime"] = current_datetime.strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    callback_context.state["user:email"] = user_email
    callback_context.state["user:timezone"] = timezone_name


class Timezone(str, Enum):
    UTC = "utc"
    LOCAL = "local"


class NowToolInput(BaseModel):
    timezone: Timezone


def now(timezone: Literal["utc", "local"]) -> Dict[str, str]:
    """
    Returns the current datetime in RFC 3339 format.
    Only use this tool when the user specifically asks for it or the current task would benefit from knowing the current datetime.

    Args:
        timezone: The timezone to use for the datetime. Use "utc" for UTC or "local" for local time.

    Returns:
        A dictionary containing the formatted current datetime message.
    """
    if timezone == Timezone.UTC:
        now = datetime.datetime.now(datetime.timezone.utc)
    elif timezone == Timezone.LOCAL:
        now = datetime.datetime.now()
    else:
        raise ValueError(f"Invalid timezone: {timezone}. Must be 'utc' or 'local'")

    # Format in RFC 3339 format (ISO 8601)
    now_str = now.isoformat()

    return {"datetime": now_str}


root_agent = LlmAgent(
    name="calendar_agent",
    model="gemini-2.0-flash",
    description="Agent who can arrange the time management centralized on Google Calendar",
    instruction=prompt.MULTIPLE_AGENT,
    sub_agents=[
        agenda_task_agent,
        event_agent,
        agenda_discussion_agent,
    ],
    tools=[
        # MCPToolset(
        #     # connection_params=StdioServerParameters(
        #     #     command="npx",
        #     #     args=["@cocal/google-calendar-mcp"],
        #     #     env={
        #     #         "GOOGLE_OAUTH_CREDENTIALS": "/home/avei/GithubRepo/playground/calendar-agent/key.json"
        #     #     },
        #     # ),
        #     tool_filter=["calendar_list_accounts"],
        # ),
        now,
        context.inject_context,
    ],
    before_agent_callback=session_init_callback,
)
