from . import google_calendar
from . import time
# from . import google_workspace
# from . import calendar_toolset
from . import mcp_calendar_remote
from . import datetime
from . import calendar_built_in
from . import paper_mcp_server

class MCPServers:
    MCPCalendarRemote = mcp_calendar_remote.mcp
    CalendarInternal = calendar_built_in.mcp
    # CalendarToolset = calendar_toolset.mcp
    # GoogleWorkspace = google_workspace.mcp
    GoogleCalendar = google_calendar.mcp
    Time = time.mcp
    DateTime = datetime.mcp
    PaperSearchMCP = paper_mcp_server.mcp
