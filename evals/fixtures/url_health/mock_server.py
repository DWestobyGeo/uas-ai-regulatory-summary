"""Minimal local HTTP server used only by evals/run_url_health_fixture_check.py to exercise
scripts/check_source_urls.py's request logic (200 / 404 / HEAD-unsupported-falls-back-to-GET /
connection-refused) without touching the real internet -- safe to run in CI."""

import http.server
import socketserver


class Handler(http.server.SimpleHTTPRequestHandler):
    ROUTES_HEAD = {"/good.html": 200, "/notfound.html": 404, "/no-head.html": 405}
    ROUTES_GET = {"/good.html": 200, "/notfound.html": 404, "/no-head.html": 200}

    def do_HEAD(self):
        self.send_response(self.ROUTES_HEAD.get(self.path, 500))
        self.end_headers()

    def do_GET(self):
        code = self.ROUTES_GET.get(self.path, 500)
        self.send_response(code)
        self.end_headers()
        if code == 200:
            self.wfile.write(b"ok")

    def log_message(self, fmt, *args):
        pass  # keep CI output quiet


def serve(port: int) -> socketserver.TCPServer:
    httpd = socketserver.TCPServer(("127.0.0.1", port), Handler)
    return httpd
