import uvicorn
import openlit
import os
from google.adk.cli.fast_api import get_fast_api_app

otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "")

# Initialize Instrumentation if otlp_endpoint is not empty
if otlp_endpoint != "" :
    openlit.init(
        otlp_endpoint=otlp_endpoint,
        application_name="calendar_agent",
        disable_batch=True,
        environment="development",
    )

DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost:5432/adk")

# session_service = DatabaseSessionService(db_url=DB_URL)
# Running the service with db if not use in memory
try:
    print("Initialize with DB Session Service")
    app = get_fast_api_app(
        session_service_uri=DB_URL,
        agents_dir=os.path.dirname(os.path.abspath(__file__)) + "/agents",
        allow_origins=["*"],
        web=True,
    )
except:
    print("Failed to initalize with DB Session, Using in Memory")
    app = get_fast_api_app(
        agents_dir=os.path.dirname(os.path.abspath(__file__)) + "/agents",
        allow_origins=["*"],
        web=True,
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        reload=True,
    )
