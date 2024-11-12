from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1='CENTRE'><b>MY LAPTOP CONFIGURATION</b></h1>
        <h2>NAME: G P HARIESH<br> 
            REF NO: 24900267</h2>
        <ol>
        <li>Device name	GP_HARIESH_0407</li>
        <li>Processor	AMD Ryzen 5 5600H with Radeon Graphics</li>          3.30 GHz
        <li>Installed RAM	16.0 GB (15.3 GB usable)</li>
        <li>Device ID	40ED45FD-069E-4AE8-862C-EBEA6D5739AF</li>
        <li>Product ID	00342-42590-73672-AAOEM</li>
        <li>System type	64-bit operating system, x64-based processor</li>
        <li>Pen and touch	No pen or touch input is available for this display</li>
            
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()