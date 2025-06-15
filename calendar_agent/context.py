import datetime
import pytz

from google.adk.tools import FunctionTool, ToolContext


def inject_context(tool_context: ToolContext) -> dict:
    current_datetime = datetime.datetime.now()
    user_email: str = tool_context.state.get("user:email", "user@example.com")

    timezone_name = tool_context.state.get("user:timezone", "Asia/Jakarta")
    timezone = pytz.timezone(timezone_name)

    localized_datetime = current_datetime.astimezone(timezone)
    formatted_datetime = localized_datetime.strftime("%Y-%m-%d %H:%M:%S")

    tool_context.state["current_datetime"] = formatted_datetime
    tool_context.state["user:email"] = user_email
    tool_context.state["user:timezone"] = timezone_name

    return {
        "current_datetime": formatted_datetime,
        "user_email": user_email,
        "timezone": timezone_name,
    }


# context_tool = FunctionTool(
#     fn=inject_context,
#     name="inject_context",
#     description="Inject context data like current datetime, user email, and timezone",
# )


def use_context(query: str, tool_context: ToolContext) -> dict:
    current_datetime = tool_context.state.get("current_datetime", "Unknown")
    user_email = tool_context.state.get("user:email", "Unknown")
    timezone = tool_context.state.get("user:timezone", "Unknown")

    return {
        "query": query,
        "timestamp": current_datetime,
        "processed_for": user_email,
        "timezone_used": timezone,
        "message": f"Processed query `{query}` at {current_datetime} for {user_email} in {timezone} timezone",
    }


# use_context_tool = FunctionTool(
#     fn=use_context,
#     name="use_context",
#     description="Process a query using context data",
#     parameters={
#         "query": {
#             "type": "string",
#             "description": "The query to process",
#         }
#     },
# )
