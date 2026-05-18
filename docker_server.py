import os
from http.server import ThreadingHTTPServer

from server import Handler, curl_requests


HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "7790"))


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    engine = "curl_cffi" if curl_requests is not None else "urllib"
    print(f"Local Pay URL Generator: http://127.0.0.1:{PORT}/")
    print(f"Listening on: {HOST}:{PORT}")
    print(f"Request engine: {engine}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
