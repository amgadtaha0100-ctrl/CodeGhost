from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # كود تجريبي سريع للتأكد من الربط
        response = {
            "message": "مرحباً بك في CodeGhost! أداة اليوتيوب قيد التجهيز الآن."
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
