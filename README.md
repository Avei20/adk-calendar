# ADK Calendar Agent

<a href="https://studio.firebase.google.com/import?url=https%3A%2F%2Fgithub.com%2FAvei20%2Fadk-calendar">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://cdn.firebasestudio.dev/btn/try_dark_32.svg">
    <source
      media="(prefers-color-scheme: light)"
      srcset="https://cdn.firebasestudio.dev/btn/try_light_32.svg">
    <img
      height="32"
      alt="Try in Firebase Studio"
      src="https://cdn.firebasestudio.dev/btn/try_blue_32.svg">
  </picture>
</a>

A sophisticated calendar management system built with Google's Agent Development Kit (ADK) that provides intelligent time management and scheduling capabilities through Google Calendar integration.

## 🚀 Features

- **Multi-Agent Architecture**: Intelligent calendar management with specialized sub-agents for different tasks
- **Google Calendar Integration**: Seamless integration with Google Calendar API via MCP (Model Context Protocol)
- **Time Management**: Advanced scheduling, event management, and agenda planning
- **Timezone Support**: Multi-timezone awareness and handling
- **Real-time Context**: Dynamic context injection for personalized experiences
- **Observability**: Built-in monitoring with OpenTelemetry, Prometheus, and Grafana

## 🏗️ Architecture

The system consists of a main calendar agent with three specialized sub-agents:

- **Agenda Task Agent**: Handles task scheduling and management
- **Event Agent**: Manages calendar events and meetings
- **Agenda Discussion Agent**: Facilitates discussion scheduling and coordination

## 🛠️ Tech Stack

- **Framework**: Google Agent Development Kit (ADK)
- **Language**: Python 3.13+
- **Database**: PostgreSQL
- **AI Model**: Gemini 2.0 Flash
- **API**: FastAPI
- **Monitoring**: OpenTelemetry, Prometheus, Grafana
- **Containerization**: Docker & Docker Compose

## 📋 Prerequisites

- Python 3.13 or higher
- Docker and Docker Compose
- Google Cloud Platform account
- Google Calendar API credentials

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd adk-calendar
```

### 2. Set Up Environment Variables

Copy the environment template and configure your settings:

```bash
cp env.template .env
```

Edit `.env` file with your credentials:

```env
GEMINI_API_KEY=your_gemini_api_key_here
USE_VERTEX=false
```

### 3. Set Up Google Calendar Credentials

Place your Google OAuth credentials file as `key.json` in the project root directory.

### 4. Run with Docker Compose

```bash
docker-compose up --build
```

This will start all services:
- **ADK Calendar Agent**: `http://localhost:8080`
- **PostgreSQL Database**: `localhost:5432`
- **Jaeger Tracing**: `http://localhost:16686`
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000`

## 🔧 Development Setup

### Local Development

1. Install dependencies using uv:

```bash
uv sync
```

2. Set up the database:

```bash
# The database will be automatically created when running with Docker Compose
```

3. Run the application:

```bash
python main.py
```

### Project Structure

```
adk-calendar/
├── calendar_agent/           # Main agent implementation
│   ├── agent.py             # Root agent configuration
│   ├── context.py           # Context management
│   ├── prompt.py            # Agent prompts and instructions
│   ├── sub_agent/           # Specialized sub-agents
│   │   ├── agenda_discussion/
│   │   ├── agenda_task/
│   │   └── event/
│   └── tools/               # Custom tools and utilities
├── main.py                  # Application entry point
├── docker-compose.yaml      # Docker services configuration
├── Dockerfile              # Container configuration
├── pyproject.toml          # Python project configuration
└── README.md               # This file
```

## 🎯 Usage

The ADK Calendar Agent provides intelligent calendar management through natural language interactions. You can:

- Schedule meetings and events
- Manage tasks and agendas
- Coordinate discussions
- Handle timezone conversions
- Get current time information
- Manage Google Calendar entries

### Example Interactions

- "Schedule a meeting with John tomorrow at 2 PM"
- "What's on my calendar for next week?"
- "Create a task to review the quarterly report"
- "What time is it in Jakarta?"

## 📊 Monitoring

The application includes comprehensive monitoring:

- **Jaeger**: Distributed tracing and request flow visualization
- **Prometheus**: Metrics collection and storage
- **Grafana**: Metrics visualization and dashboards

Access the monitoring interfaces:
- Jaeger UI: http://localhost:16686
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## 🔒 Security

- Google OAuth credentials are required for Calendar API access
- Environment variables are used for sensitive configuration
- Database connections are secured within the Docker network

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [Google Agent Development Kit Documentation](https://developers.google.com/agent-development-kit)
- [Google Calendar API Documentation](https://developers.google.com/calendar)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

## 🆘 Support

For issues and questions:
- Check the existing issues in the repository
- Create a new issue with detailed information
- Contact the development team

---

**Note**: This project is actively developed and may have breaking changes. Please check the latest documentation for the most up-to-date information.