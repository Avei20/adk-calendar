1. Click Open in Firebase Studio
2. While waiting everything is loaded lets get the client token from google.
3. Then run this command is local to get the user token
```bash 
GOOGLE_OAUTH_CREDENTIALS=/Users/avei/GithubRepo/playground/adk-calendar/key.json \
GOOGLE_MCP_TOKEN_PATH=/Users/avei/GithubRepo/playground/adk-calendar/token.json \ 
npx -y @cocal/google-calendar-mcp
```
4. Then copy the key.json and token.json in the root path. After that adjust the dev.nix with the environment variable.
