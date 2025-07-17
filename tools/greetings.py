from google.adk.tools import ToolContext

def greeting(tool_context: ToolContext) -> dict[str, str] | None :
    '''
    Fetches a greeting message if user was not greeted.
    '''
    adk_session_state = tool_context.state

    if not adk_session_state.get("is_greeted"):
        adk_session_state['is_greeted'] = True
        return {"status": "success", "message": "Hai! Aku Sore, Personal Assistant kamu dari masa depan"}
    return None
