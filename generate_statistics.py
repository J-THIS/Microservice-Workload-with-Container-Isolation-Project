import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import os

# microservice 3
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/generate":
            # get caculated data from microservice 2
            response = requests.get("http://calculate_service:8001/calculate")
            data = response.json()
 
            # transfer to DataFrame
            df = pd.DataFrame(data)
            
            # save the statistics table in CSV
            csv_file_path = '/usr/src/app/data/Statistics_Table.csv'
            # create that directory if not exist
            os.makedirs(os.path.dirname(csv_file_path), exist_ok=True) 
            
            df.to_csv(csv_file_path, index=False)
            
            # send response
            self.send_response(200)
            
            # set file as attachments for download
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="Statistics_Table.csv"')
            self.end_headers()
            
            # write file to http response stream
            with open(csv_file_path, 'rb') as f:
            	self.wfile.write(f.read())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8002), RequestHandler)
    server.serve_forever()

