#!/usr/bin/env python3
"""
FormLens Project Web Server
Serves the FormLens project page on port 5012
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse

class FormLensHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Handle the /formlens path
        if path == '/formlens' or path == '/formlens/':
            # Redirect to index.html
            self.path = '/formLens_project_page/index.html'
        elif path.startswith('/formlens/'):
            # Handle requests like /formlens/images/... -> /formLens_project_page/images/...
            relative_path = path[9:]  # Remove '/formlens/'
            self.path = f'/formLens_project_page/{relative_path}'
        elif path.startswith('/images/') or path.startswith('/results/'):
            # Handle direct requests to images/ and results/ directories
            self.path = f'/formLens_project_page{path}'
        
        # Call the parent class method
        return super().do_GET()
    
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the parent directory so we can serve the formLens_project_page folder
    os.chdir('/home/shaon')
    
    PORT = 5013
    
    # Create the server
    with socketserver.TCPServer(("", PORT), FormLensHandler) as httpd:
        print(f"🚀 FormLens Project Server running on:")
        print(f"   http://10.4.16.81:{PORT}/formlens")
        print(f"   http://localhost:{PORT}/formlens")
        print(f"\n📁 Serving files from: /home/shaon/formLens_project_page/")
        print(f"🔄 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped.")
            httpd.shutdown()

if __name__ == "__main__":
    main()
