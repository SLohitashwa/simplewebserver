from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <h1>Name:Lohitashwa S</h1>
        <br>
        <h2>Reg.no:26015531</h2>
    </head>
    <body>
        <table border="1" cellspacing="15" cellpadding="15">
            <caption>PC Specifications</caption>
            <tr>
                <th>S.NO</th>
                <th>Name</th>
                <th>Info</th>
            </tr>
            <tr bgcolor="skyblue">
                <td>1</td>
                <td>Device name</td>
                <td>Lohit</td>
            </tr>
            <tr bgcolor="skyblue">
                <td>2</td>
                <td>Processor</td>
                <td>Intel core 5 210H (2.2GHZ)</td>
            </tr>
            <tr bgcolor="skyblue">
                <td>3</td>
                <td>Installed RAM</td>
                <td>16.0 GB</td>
            </tr>
            <tr bgcolor="skyblue">
                <td>4</td>
                <td>Graphics Card</td>
                <td>Intel(R) Graphics (128 MB)</td>
            </tr>
            <tr bgcolor="skyblue">
                <td>5</td>
                <td>Storage</td>
                <td>152 GB of 477 GB used</td>
            </tr>
            <tr bgcolor="skyblue">
                <td>6</td>
                <td>System type</td>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
        </table>
    </body>
</html> 
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()