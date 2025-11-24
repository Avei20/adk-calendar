from google.adk.agents.llm_agent import LlmAgent
# from google.adk.models.lite_llm import LiteLlm

from . import prompt

# model = LiteLlm(
#     model="",
#     api_base="https://cody.su/api/v1",
#     extra_headers={
#         "Authorization": "Bearer tm-12uP5TFckbOEcX9huiQuLzh3FMdxgrz3lB0onnoue07ab0aa"
#     },
# )

root_agent = LlmAgent(
    name="aws_caption_agent",
    model="gemini-3-pro-preview",
    description="Agent for generation caption for social media posting for AWS User Group Indonesia and Jakarta",
    instruction=prompt.PROMPT,
)
