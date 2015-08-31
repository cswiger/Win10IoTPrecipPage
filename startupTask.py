import http.server
import threading
from time import sleep, time
from weather import weather
from createPage import createPage
from datetime import datetime

jfc = weather()
out = createPage(jfc)


class TestRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        print("Got a request...")
        self.wfile.write(out)


httpd = http.server.HTTPServer(("", 80), TestRequestHandler)
print('Started web server on port %d' % httpd.server_address[1])

httpd_thread = threading.Thread(target=httpd.serve_forever)
httpd_thread.setDaemon(True)
httpd_thread.start()


while True:
   sleep(60)
   # update the page at the top of the hour
   if ( datetime.fromtimestamp(time()).minute == 1 ):
      jfc = weather()
      out = createPage(jfc)

