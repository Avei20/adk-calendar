# import http.server

# class OAuthCallbackHandler(http.server.SimpleHTTPRequestHandler):
#     """Handle OAuth callback request to capture the authorization code"""
#     def __init__(self, *args, flow_instance=None, shutdown_event=None, **kwargs):
#         self.flow = flow_instance
#         self.shutdown_event = shutdown_event
#         self.auth_code = None
#         self.error = None
#         super().__init__(*args, **kwargs)

#     def do_get(self):
#         """Handle GET from OAuth Callback"""
#         query_components = parse_qs(urlparse(self.path).query)
#         code = query_components.get('code')
#         error = query_components.get('error')

#         if code:
#             self.auth_code = code[0]
#             logger.info("Authorization code received.")
#             self.wfile.write(b'<html><body><h1>Authentication Succesfull</h1>')
#             self.wfile.write(b'<p>Authorization code received. You can close this page.</p></body></html>')
#             return

#         if error:
#             self.error = error[0]
#             logger.error("OAuth Error: " + error[0])
#             self.wfile.write(b'<html><body><h1>Authentication Failde</h1>')
#             self.wfile.write(f'<p> Error :{self.error}. Please check server logs console.</p></body></html>'.encode())
#             return

#         logger.warning("Received callback without code or error.")
#         self.wfile.write(b'<html><body><h1>Invalid Callback</h1>')
#         self.wfile.write(b'<p>Received an unexpected request.</p></body></html>')

#         # Signal the main thread to stop the server
#         if self.shutdown_event:
#             self.shutdown_event.set()


# def start_local_http(port, flow, shutdown_event):
#     handler = lambda *args, **kwargs : OAuthCallbackHandler(
#         *args, flow_instance=flow, shutdown_event=shutdown_event, **kwargs
#     )

#     httpd = None

#     try:
#         httpd = socketserver.TCPServer(("", port), handler)
#         logger.info(f"Starting temporary OAuth callback or port " + port)
#         httpd.serve_forever()
#     except OSError as e:
#         logger.error()
