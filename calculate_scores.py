import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests

# microservice 2
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/calculate":
            # get data from microservice 1
            response = requests.get("http://read_service:8000/read")
            data = response.json()

            # convert to DataFrame
            df = pd.DataFrame(data)
            
            # caculate total scores
            df['Sum'] = df[['Chinese', 'Math', 'English', 'CloudComputing']].sum(axis=1)
            
            # caculate maximum score difference
            df['Range'] = df[['Chinese', 'Math', 'English', 'CloudComputing']].max(axis=1) - df[['Chinese', 'Math', 'English', 'CloudComputing']].min(axis=1)
            
            # return result
            result = df[['Name', 'Sum', 'Range']].to_dict(orient='records')
            
            # send response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8001), RequestHandler)
    server.serve_forever()

