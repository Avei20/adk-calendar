import os

from google.adk.tools.google_api_tool import CalendarToolset

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")


mcp = CalendarToolset(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
