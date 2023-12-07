# import tkinter as tk
# from PIL import Image, ImageTk
# import os
# import requests
# import tempfile
# import win32api
# import ttkbootstrap as ttk
# import threading
# from metadata import __AppName__
# from metadata import __version__
from resourcepath import resource_path, resource_path2
# import sys
# import psutil
# import time
# import subprocess

# class UpdateManager(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)

#         self.transient(parent)
#         self.result = None
#         self.grab_set()
#         w = 350#450#350
#         h = 200#150#200
#         sw = self.winfo_screenwidth()
#         sh = self.winfo_screenheight()
#         x = (sw - w) / 2
#         y = (sh - h) / 2
#         self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
#         self.resizable(width=False, height=False)
#         self.title('Update Manager')
#         self.iconpath = resource_path(relative_path='images/unt.ico')
#         self.iconbitmap(self.iconpath)
#         self.ima = resource_path2(relative_path='images/updatemanager.jpg')
#         if os.path.exists(self.ima):
#             photo = Image.open(self.ima)
#             self.photo = ImageTk.PhotoImage(photo)
#             label = tk.Label(self, image=self.photo)
#             label.pack()
    
#         exe_directory = os.path.expanduser(f'~\\AppData\\Local\\convetransfer\\')

        

#         def install_update():
#             tmp = tempfile.gettempdir()

#             destination_directory = exe_directory

            
#             win32api.ShellExecute(0, 'open', f'{tmp}\\{__AppName__}.msi', None, None, 10)
#             parent.destroy()
        
        
#         def start_update_manager():
#             with requests.get('http://localhost/suplike/socketra/'
#                     'updates/ConveTransfer.exe?raw=true',stream=True) as r:
#                 self.progressbar['maximum'] = int(r.headers.get('Content-Length'))
#                 r.raise_for_status()
#                 tm = tempfile.gettempdir()
#                 tm = tm.replace("\\","/")
#                 with open(f'{tm}/{__AppName__}.exe', 'wb') as f:
#                     for chunk in r.iter_content(chunk_size=4096):
#                         if chunk:  # filter out keep-alive new chunks
#                             f.write(chunk)
#                             self.progressbar['value'] += 4096
#             self.button1.config(text='Install', state=ttk.NORMAL)

#         self.progressbar = ttk.Progressbar(self,
#                                            orient='horizontal',
#                                            length=200,
#                                            mode='determinate',
#                                            value=0,
#                                            maximum=0,
#                                            bootstyle='success-striped')
#         self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#         # self.progressbar = ttk.Floodgauge(self,
#         #                                    orient='horizontal',
#         #                                    length=720,
#         #                                    mode='determinate',
#         #                                    value=0,
#         #                                    maximum=0,
#         #                                    bootstyle='success')
#         #                                    
#         # self.progressbar.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
#         self.button1 = ttk.Button(self, text='Wait!',width=9, state=ttk.DISABLED, command=install_update)
#         self.button1.place(x=-119, relx=1.0, y=-46, rely=1.0)

#         self.t1 = threading.Thread(target=start_update_manager)
#         self.t1.start()

import tkinter as tk
from PIL import Image, ImageTk
import os
import requests
import tempfile
import win32api
import ttkbootstrap as ttk
import threading
from io import BytesIO

exe_directory = os.path.expanduser(f'~\\AppData\\Local\\convetransfer\\')


class UpdateManager(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 350
        h = 200
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('Update Manager')
        self.iconpath = resource_path(relative_path='images/unt.ico')
        self.iconbitmap(self.iconpath)
        self.ima = resource_path2(relative_path='images/updatemanager.jpg')
        if os.path.exists(self.ima):
            photo = Image.open(self.ima)
            self.photo = ImageTk.PhotoImage(photo)
            label = tk.Label(self, image=self.photo)
            label.pack()

        self.progressbar = ttk.Progressbar(self,
                                           orient='horizontal',
                                           length=200,
                                           mode='determinate',
                                           value=0,
                                           maximum=100,
                                           bootstyle='success-striped')
        self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button1 = ttk.Button(self, text='Wait!', width=9, state=ttk.DISABLED, command=self.install_update)
        self.button1.place(x=-119, relx=1.0, y=-46, rely=1.0)

        self.t1 = threading.Thread(target=self.start_update_manager)
        self.t1.start()
        self.after(100, self.check_progress)  # Periodically check progress

    def check_progress(self):
        if self.t1.is_alive():
            self.after(100, self.check_progress)  # Check progress again after 100ms
        else:
            # Update UI after the thread is finished
            self.progressbar.stop()
            self.progressbar['value'] = 100  # Ensure progress bar is full
            self.button1.config(text='Ok Ready!', state=ttk.NORMAL)

    def install_update(self):
        tmp = tempfile.gettempdir()
        installer = 'InstallerApp'
        win32api.ShellExecute(0, 'open', f'{tmp}\\{installer}.exe', None, None, 10)
        self.destroy()

    def start_update_manager(self):
        files_to_download = ['ConveTransfer.exe', 'InstallerApp.exe']
        total_size = sum(self.get_file_size(f'http://localhost/suplike/socketra/updates/{file_to_download}?raw=true')
                         for file_to_download in files_to_download)
        current_size = 0

        for file_to_download in files_to_download:
            with requests.get(f'http://localhost/suplike/socketra/updates/{file_to_download}?raw=true',
                              stream=True) as r:
                r.raise_for_status()
                tm = tempfile.gettempdir()
                tm = tm.replace("\\", "/")
                with open(f'{tm}/{file_to_download}', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:
                            f.write(chunk)
                            current_size += len(chunk)
                            progress_percent = (current_size / total_size) * 100
                            self.progressbar['value'] = progress_percent

    def get_file_size(self, url):
        response = requests.head(url)
        content_length = response.headers.get('content-length')
        return int(content_length) if content_length else 0


if __name__ == "__main__":
    root = tk.Tk()
    update_manager = UpdateManager(root)
    root.mainloop()
