import datetime
import time

from google.adk.tools import ToolContext

def tool(tool_context:ToolContext)-> dict:
    """
    Returns the current date and time in Asia/Jakarta timezone (UTC+7)
    without using the pytz library, and returns the datetime in dict format.

    Returns:
        dict: A dictionary containing the datetime in various formats.
    """
    adk_state = tool_context.state
    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()

    # Calculate the UTC+7 offset in seconds (7 hours * 60 minutes * 60 seconds)
    utc_offset_seconds = 7 * 60 * 60

    # Create a timedelta object for the offset
    utc_offset = datetime.timedelta(seconds=utc_offset_seconds)

    # Calculate the Asia/Jakarta time
    jakarta_now = utc_now + utc_offset

    # Format the datetime in different standards
    iso_format = jakarta_now.isoformat()
    rfc_format = jakarta_now.strftime("%a, %d %b %Y %H:%M:%S +0700")  # RFC 2822 format, adjusting timezone offset manually
    timestamp = time.mktime(jakarta_now.timetuple())
    # Create the result dictionary
    result = {
        "iso": iso_format,
        "rfc": rfc_format,
        "timestamp": timestamp,
        "datetime": jakarta_now,
        "timezone": "Asia/Jakarta",
    }

    adk_state['current_datetime'] = result

    return result
