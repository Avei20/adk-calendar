import uvicorn
import openlit
import os
from google.adk.cli.fast_api import get_fast_api_app
from google.adk.sessions import DatabaseSessionService

openlit.init(
    otlp_endpoint=os.getenv("otel-collector", "http://localhost:4318"),
    application_name="calendar_agent",
    disable_batch=True,
    environment="development",
)

DB_URL = "postgresql://postgres:postgres@localhost:5432/adk"
# session_service = DatabaseSessionService(db_url=DB_URL)

app = get_fast_api_app(
    session_service_uri=DB_URL,
    agents_dir=os.path.dirname(os.path.abspath(__file__)),
    allow_origins=["*"],
    web=True,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT", 8080))
