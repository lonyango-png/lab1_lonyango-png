"""
engine.py  -  DO NOT EDIT
============================================
This file runs the little web server and keeps the information that the
website shows. The web page itself lives in index.html.

Functions students can use from road_simulation.py:
    log(message, level)      show a message in the terminal AND on the website
    set_time(seconds)        tell the engine what second it is
    set_driver_name(name)    the name shown on the car
    start_road_engine(road)  open the website and draw the road list
    update_road(...)         draw the next frame (car position, speed, etc.)
"""

import os
import time
import json
import webbrowser
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

_HERE = os.path.dirname(os.path.abspath(__file__))

# Everything the website needs to know, shared with the browser as JSON
_WORLD_STATE = {"road": [], "car": {}, "next": "", "status": "", "time": 0, "logs": [], "driver": "Driver"}


def log(message, level="info"):
    """Show a message in the TERMINAL and on the WEBSITE log panel.
    Levels: info, ok, warn."""
    _WORLD_STATE["logs"].append({"t": _WORLD_STATE["time"], "msg": message, "level": level})
    del _WORLD_STATE["logs"][:-200]   # keep only the last 200 messages
    print(f"[{_WORLD_STATE['time']:>3}s] {level.upper():<5} {message}")


def set_driver_name(name):
    _WORLD_STATE["driver"] = name


def set_time(seconds):
    _WORLD_STATE["time"] = seconds


def _launch_server(port=8008):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

        def do_GET(self):
            if self.path == "/state":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(_WORLD_STATE).encode("utf-8"))
            else:
                try:
                    with open(os.path.join(_HERE, "index.html"), "rb") as page:
                        content = page.read()
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(content)
                except FileNotFoundError:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"index.html not found next to engine.py")

    try:
        server = HTTPServer(("0.0.0.0", port), Handler)
    except OSError:
        server = HTTPServer(("0.0.0.0", 0), Handler)
        port = server.server_port

    url = f"http://127.0.0.1:{port}"
    print("=" * 60)
    print(f"ROAD SIMULATION READY! Open: {url}")
    print("=" * 60)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        webbrowser.open(url)
    except Exception:
        pass


def start_road_engine(road):
    _WORLD_STATE["road"] = list(road)
    _launch_server()


def update_road(position_m, speed, limit, lane, next_text, status, seconds):
    _WORLD_STATE["car"] = {"pos_m": position_m, "speed": speed, "limit": limit, "lane": lane}
    _WORLD_STATE["next"] = next_text
    _WORLD_STATE["status"] = status
    _WORLD_STATE["time"] = seconds
    time.sleep(0.12)