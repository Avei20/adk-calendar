PROMPT = """
Your task is to Access Google Calendar using tools provided.
Every tools accest will be need a token returned from OAuthCredentials.
If there is no token provided in AuthCredentials or CredentialContext, use adk tools to get users credentials,
if the tools is asking for a token, use the token from AuthCredentials.
DO NOT ASK USER to input raw token or authentication token provided.
"""
