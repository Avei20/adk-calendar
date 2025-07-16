import os

from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
from authentications import Auth

with open(os.path.join(os.path.dirname(__file__), 'specs/calendar.yaml'), 'r') as f:
    spec_content = f.read()

mcp = OpenAPIToolset(
    spec_str=spec_content,
    spec_str_type="yaml",
    auth_scheme=Auth.Scheme,
    auth_credential=Auth.Credential,
)
