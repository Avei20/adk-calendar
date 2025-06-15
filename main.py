import uvicorn
import openlit
import os
from google.adk.cli.fast_api import get_fast_api_app
from google.adk.sessions import DatabaseSessionService

openlit.init(otlp_endpoint="http://otel-collector:4318")

# DB_URL = "postgresql://postgres:postgres@db:5432/adk"
# session_service = DatabaseSessionService(db_url=DB_URL)
app = get_fast_api_app(
    agents_dir=os.path.dirname(os.path.abspath(__file__)), allow_origins=["*"], web=True
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
