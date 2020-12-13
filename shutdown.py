# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import logging

logging.basicConfig(filename=os.environ['SHUTDOWN_LOG_PATH'], level=logging.INFO, format='%(asctime)s %(message)s')

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path != os.environ['SHUTDOWN_ENDPOINT_URL']):
            self.send_response(404)
            self.end_headers()
        else:
            logging.info('Shutdown endpoint called, performing shutdown now')
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            f = open(os.environ['SHUTDOWN_FILE_PATH'], 'w')
            f.write("true")
            f.close()
            self.wfile.write(bytes("OK", "utf-8"))
         

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
