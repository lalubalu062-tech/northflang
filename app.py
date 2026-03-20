import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

print("🚀 Starting Web App...")

# Python ka Search Mission: FeelingSurf ka asli path aur naam dhundho
def find_feelingsurf():
    # Common Linux installation folders
    for root_dir in ['/opt', '/usr/bin', '/usr/local/bin']:
        if not os.path.exists(root_dir): continue
        for dirpath, _, filenames in os.walk(root_dir):
            for f in filenames:
                if f.lower().startswith('feelingsurf') and os.access(os.path.join(dirpath, f), os.X_OK):
                    if '.so' not in f:
                        return os.path.join(dirpath, f)
    # Fallback based on last successful run
    return "/opt/FeelingSurfViewer/FeelingSurfViewer"

exe_path = find_feelingsurf()
print(f"✅ Found FeelingSurf Executable at: {exe_path}")

print("Starting FeelingSurf Viewer in background...")
subprocess.Popen(["xvfb-run", "--auto-servernum", exe_path, "--no-sandbox"])

# Northflank aur UptimeRobot ke liye Web Server
class WebServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = """
        <html>
        <body style="text-align:center; padding-top:100px; font-family:Arial;">
            <h1 style="color:green;">🚀 System is Running 24/7 on Northflank</h1>
            <p>FeelingSurf Traffic Exchange is active in the background.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

# CHANGE: Port 7860 se 8080 kar diya
print("Starting Simple Web Server on Port 8080...")
HTTPServer(('0.0.0.0', 8080), WebServer).serve_forever()
