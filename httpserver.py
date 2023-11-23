
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import urllib
import os
import html
import time
import shutil
import cgi
import tkinter as tk
from get_ip import wifi
import encodings
import codecs
import io


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.expanduser("~"), **kwargs)

    def list_directory(self, path):
        try:
            list = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        r = []
        try:
            displaypath = urllib.parse.unquote(self.path, errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        displaypath = html.escape(displaypath)
        r.append('<!DOCTYPE html>\n<html>\n<head>')
        r.append('<meta charset="utf-8">')
        r.append('<title>Directory listing for %s</title>' % displaypath)
        r.append('<style>')
        r.append('body {font-family: "Helvetica", sans-serif; margin: 2em; padding: 2em; background-color: #f5f5f5;}')
        r.append('h1 {color: #333;}')
        r.append('table {border-collapse: collapse; width: 100%;}')
        r.append('th, td {padding: 8px 12px; border: 1px solid #ddd; text-align: left; font-size: 14px;}')
        r.append('th {background-color: #4CAF50; color: white;}')
        r.append('tr:nth-child(even) {background-color: #f2f2f2;}')
        r.append('.upload-form {margin-top: 20px;}')
        r.append('.upload-input {margin-right: 10px;}')
        r.append('.upload-button {padding: 8px 12px; background-color: #4CAF50; color: white; border: none; cursor: pointer; margin-left: 0px;}')
        r.append('.destination {margin-top: 20px; margin-bottom: 30px;}')
        r.append('.radio-group {display: flex;}')
        r.append('.radio-group label {margin-right: 20px;}')
        r.append('</style>')
        r.append('</head>\n<body>')
        r.append('<h1>Directory listing for %s</h1>' % displaypath)
        
        # Add a form for navigating to the parent directory
        r.append('<form method="get" action="/">')
        r.append('<button type="submit">Parent Directory</button>')
        r.append('</form>')

        # Add a styled form for uploading files
        r.append('<form class="upload-form" enctype="multipart/form-data" method="post" action="/">')
        
        # File input div
        r.append('<div>')
        r.append('<input class="upload-input" type="file" name="file">')
        r.append('<button class="upload-button" type="submit">Upload File</button>')
        r.append('</div>')

        # Destination selection div
        r.append('<div class="destination">')
        r.append('<label>Select Destination:</label>')
        r.append('<div class="radio-group">')
        r.append('<input type="radio" name="destination" value="desktop" checked> Desktop')
        r.append('<input type="radio" name="destination" value="documents"> Documents')
        r.append('<input type="radio" name="destination" value="music"> Music')
        r.append('<input type="radio" name="destination" value="videos"> Videos')
        r.append('<input type="radio" name="destination" value="pictures"> Pictures')
        r.append('</div>')
        r.append('</div>')

        r.append('</form>')

        # Add a table with headers for filename, date, and filesize
        r.append('<table>')
        r.append('<tr>')
        r.append('<th>Filename</th>')
        r.append('<th>Date</th>')
        r.append('<th>Filesize</th>')
        r.append('</tr>')

        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + '/'
                linkname = name + '/'
            if os.path.islink(fullname):
                displayname = name + '@'
                # Note: a link to a directory displays with @ and links with /
            r.append('<tr>')
            r.append('<td><a href="%s">%s</a></td>' % (
                urllib.parse.quote(linkname),
                html.escape(displayname),
            ))
            r.append('<td>%s</td>' % time.ctime(os.path.getmtime(fullname)))
            r.append('<td>%s</td>' % sizeof_fmt(os.path.getsize(fullname)))
            r.append('</tr>')

        r.append('</table>')
        r.append('</body>\n</html>')
        encoded = '\n'.join(r).encode('utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
    
    def do_POST(self):
        # Handle file uploads
        if self.path == '/':
            content_type, _ = cgi.parse_header(self.headers.get('Content-Type'))
            if content_type == 'multipart/form-data':
                form_data = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']}
                )
                uploaded_file = form_data['file']
                if uploaded_file.file:
                    # Specify the directory to save uploaded files
                    destination = form_data.getvalue("destination")
                    upload_dir = self.get_destination_path(destination)
                    os.makedirs(upload_dir, exist_ok=True)
                    save_path = os.path.join(upload_dir, uploaded_file.filename)

                    # Save the file
                    with open(save_path, 'wb') as f:
                        shutil.copyfileobj(uploaded_file.file, f)
        
        # Redirect back to the directory listing after the upload
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def get_destination_path(self, destination):
        user_home = os.path.expanduser("~")
        destination_paths = {
            "desktop": os.path.join(user_home, "Desktop"),
            "documents": os.path.join(user_home, "Documents"),
            "music": os.path.join(user_home, "Music"),
            "videos": os.path.join(user_home, "Videos"),
            "pictures": os.path.join(user_home, "Pictures"),
        }
        return destination_paths.get(destination, user_home)
    def shutdown_server(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Server shutting down...")
        self.server.shutdown()



#  Specify the port to use
PORT = 8000
ipadd = wifi

if __name__ == "__main__":
    PORT = 8000

    try:
        # Start the HTTP server
        with TCPServer((f'{ipadd}', PORT), MyHandler) as httpd:
            print(f'Serving on port {PORT}')
            httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server: {e}")
        raise  # Reraise the exception to see the traceback

    

