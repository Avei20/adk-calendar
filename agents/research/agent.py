from google.adk.agents.llm_agent import LlmAgent
from mcp_servers import MCPServers
from . import prompt

root_agent = LlmAgent(
    name="research_agent",
    model="gemini-2.5-pro",
    description="A research agent that uses the Gemini-2.5 Pro model to generate research papers.",
    instruction=prompt.PROMPT ,
    tools=[
        MCPServers.PaperSearchMCP,
    ]
)
