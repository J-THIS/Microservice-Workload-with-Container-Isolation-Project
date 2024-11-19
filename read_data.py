import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# microservice 1
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/read":
            # read grade table
            df = pd.read_csv('Grade Table.csv')
            
            # convert DataFrame to JSON
            data = df.to_dict(orient='records')
            
            # send response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), RequestHandler)
    server.serve_forever()

