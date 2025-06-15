from google.adk.agents import LlmAgent
from . import prompt
from calendar_agent.context import use_context

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

agenda_discussion_agent = LlmAgent(
    name="agenda_discussion_management_agent",
    model="gemini-2.0-flash",
    description="",
    instruction=prompt.PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["@cocal/google-calendar-mcp"],
                env={
                    "GOOGLE_OAUTH_CREDENTIALS": "/home/avei/GithubRepo/playground/calendar-agent/key.json"
                },
            ),
            tool_filter=[
                "calendar_create_event",
                "calendar_delete_event",
                "calendar_get_events",
            ],
        ),
        use_context,
    ],
)
