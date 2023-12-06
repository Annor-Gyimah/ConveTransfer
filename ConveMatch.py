# # import ttkbootstrap as ttk
# # import tkinter as tk
# # import ctypes
# # from tkinter import messagebox
# # from metadata import __AppName__, __version__

# # class Matchmaker(ttk.Window):
# #     user32 = ctypes.windll.user32
# #     screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# #     def __init__(self):
# #         super().__init__()
# #         self.resizable(False, False)
# #         w = 450
# #         h = 120
# #         sw = self.winfo_screenwidth()
# #         sh = self.winfo_screenheight()
# #         x = (sw - w) / 2
# #         y = (sh - h) / 2
# #         self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
# #         self.title('ConveTransfer Match')
# #         ttk.Button(self, text='kdf').pack()

# #     def update_using_manager(self):
# #         try:
# #             # Read content from the 'window.txt' file
# #             with open('window.txt', 'r') as file:
# #                 # Process each line in the file
# #                 for line in file:
# #                     # Strip whitespace and newline characters
# #                     data = line.strip()
                    
# #                     # Attempt to convert the string to a tuple
# #                     try:
# #                         window_size = eval(data)
# #                     except SyntaxError as se:
# #                         print(f"SyntaxError in 'window.txt': {se}")
# #                         continue

# #                     # Compare screensize with the current tuple
# #                     if window_size == self.screensize:
# #                         print('yes')
# #                         return  # Exit the loop if a match is found

# #                 # If no match is found
# #                 print('no')

# #         except Exception as e:
# #             print(f'The Error is here! {e}')

# # if __name__ == '__main__':
# #     APP = Matchmaker()
# #     APP.update_using_manager()
# #     APP.mainloop()

# import ttkbootstrap as ttk
# import tkinter as tk
# import ctypes
# import requests
# import win32api
# import tempfile
# import threading
# from metadata import __AppName__
# from resourcepath import resource_path

# class Matchmaker(ttk.Window):
#     user32 = ctypes.windll.user32
#     screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#     def __init__(self):
#         super().__init__()
#         self.resizable(False, False)
#         w = 450
#         h = 120
#         sw = self.winfo_screenwidth()
#         sh = self.winfo_screenheight()
#         x = (sw - w) / 2
#         y = (sh - h) / 2
#         self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
#         self.title('ConveTransfer Match')
#         self.iconpath = resource_path(relative_path='images/unt.ico')
#         self.iconbitmap(self.iconpath)
#         ttk.Button(self, text='kdf').pack()
#         self.progressbar = ttk.Progressbar(self,
#                                            orient='horizontal',
#                                            length=200,
#                                            mode='determinate',
#                                            value=0,
#                                            maximum=0,
#                                            bootstyle='success-striped')
#         self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#         self.button1 = ttk.Button(self, text='Wait!', width=9, state=ttk.DISABLED, command=self.install_update)
#         self.button1.place(x=-123, relx=1.0, y=-46, rely=1.0)
#         self.t_time = ttk.Label(self, text="yess")
#         self.t_time.pack(side=tk.LEFT, padx=(20, 5))

#     def install_update(self):
#         tmp = tempfile.gettempdir()
#         win32api.ShellExecute(0, 'open', f'{tmp}\\{__AppName__}.msi', None, None, 10)
#         self.destroy()

#     def convetransfer_1280_720(self, total_size):
#         with requests.get('http://localhost/suplike/socketra/updates/ConveTransfer.msi?raw=true', stream=True) as r:
#             self.progressbar['maximum'] = total_size
#             r.raise_for_status()
#             tm = tempfile.gettempdir()
#             tm = tm.replace("\\", "/")
#             bytes_sent = 0
#             with open(f'{tm}/{__AppName__}.msi', 'wb') as f:
#                 for chunk in r.iter_content(chunk_size=4096):
#                     if chunk:  # filter out keep-alive new chunks
#                         f.write(chunk)
#                         bytes_sent += len(chunk)
#                         progress = (bytes_sent / total_size) * 100
#                         self.progressbar['value'] += 4096
#                         self.update_idletasks()
#                         self.t_time.configure(text=f"{int(progress)}% ")
#         self.button1.config(text='Install', state=ttk.NORMAL)

#     def find_match(self):
#         try:
#             # Make an HTTP request to get the link(s)
#             response = requests.get('http://localhost/suplike/socketra/updates/windows.txt')
#             data = response.text.strip()  # Strip newline characters

#             # Process each line in the response text
#             for line in data.split('\n'):
#                 # Strip whitespace and newline characters
#                 url = line.strip()

#                 # Process the URL as needed (you can use it, display it, etc.)
#                 print(f'Processing URL: {url}')

#                 try:
#                     window_size = eval(url)
#                 except SyntaxError as se:
#                     print(f"SyntaxError in 'windows.txt': {se}")
#                     continue

#                 if window_size == self.screensize:
#                     total_size = int(requests.head('http://localhost/suplike/socketra/updates/ConveTransfer.msi?raw=true').headers.get('Content-Length'))
#                     self.t1 = threading.Thread(target=self.convetransfer_1280_720, args=(total_size,))
#                     self.t1.start()
#                     return
#             print('no')
#         except Exception as e:
#             print(f'The Error is here! {e}')

# if __name__ == '__main__':
#     APP = Matchmaker()
#     APP.find_match()
#     APP.mainloop()


# Import necessary libraries
import tkinter as tk
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ctypes
import requests
import win32api
import tempfile
import threading
from metadata import __AppName__
from resourcepath import resource_path

class Matchmaker(ttk.Window):
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        w = 450
        h = 120
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.title('___')
        self.iconpath = resource_path(relative_path='images/unt.ico')
        self.wm_iconbitmap(self.iconpath)
        self.downloadss = ttk.Label(self, text='Downloading resources....')
        self.downloadss.pack(side='top')
        self.progressbar = ttk.Progressbar(self,
                                           orient='horizontal',
                                           length=200,
                                           mode='determinate',
                                           value=0,
                                           maximum=0,
                                           bootstyle='success-striped')
        self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button1 = ttk.Button(self, text='Wait!', width=9, state=ttk.DISABLED, command=self.install_update)
        self.button1.place(x=-123, relx=1.0, y=-46, rely=1.0)
        self.t_time = ttk.Label(self, text="")
        self.t_time.pack(side=tk.LEFT, padx=(20, 5))

    def install_update(self):
        tmp = tempfile.gettempdir()
        win32api.ShellExecute(0, 'open', f'{tmp}\\{__AppName__}.msi', None, None, 10)
        self.destroy()

    def convetransfer_1280_720(self, total_size):
        with requests.get('http://localhost/Applight/updates/ConveTransfer.msiraw=true', stream=True) as r:
            self.progressbar['maximum'] = total_size
            r.raise_for_status()
            tm = tempfile.gettempdir()
            tm = tm.replace("\\", "/")
            bytes_sent = 0
            with open(f'{tm}/{__AppName__}.msi', 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        bytes_sent += len(chunk)
                        progress = (bytes_sent / total_size) * 100
                        self.progressbar['value'] += 4096
                        self.update_idletasks()
                        self.t_time.configure(text=f"{int(progress)}% ")
        self.button1.config(text='Install', state=ttk.NORMAL)

    def convetransfer_1366_768(self, total_size):
        with requests.get('http://localhost/Applight/updates/ConveTransfer.msi?raw=true', stream=True) as r:
            self.progressbar['maximum'] = total_size
            r.raise_for_status()
            tm = tempfile.gettempdir()
            tm = tm.replace("\\", "/")
            bytes_sent = 0
            with open(f'{tm}/{__AppName__}.msi', 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        bytes_sent += len(chunk)
                        progress = (bytes_sent / total_size) * 100
                        self.progressbar['value'] += 4096
                        self.update_idletasks()
                        self.t_time.configure(text=f"{int(progress)}% ")
        self.button1.config(text='Install', state=ttk.NORMAL)
    
    def convetransfer_1536_864(self, total_size):
        with requests.get('http://localhost/Applight/updates/ConveTransfer.msi?raw=true', stream=True) as r:
            self.progressbar['maximum'] = total_size
            r.raise_for_status()
            tm = tempfile.gettempdir()
            tm = tm.replace("\\", "/")
            bytes_sent = 0
            with open(f'{tm}/{__AppName__}.msi', 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        bytes_sent += len(chunk)
                        progress = (bytes_sent / total_size) * 100
                        self.progressbar['value'] += 4096
                        self.update_idletasks()
                        self.t_time.configure(text=f"{int(progress)}% ")
        self.button1.config(text='Install', state=ttk.NORMAL)

    
    def find_match(self):
        try:
            width, height = self.screensize  # Unpack the width and height from self.screensize
            if width == 1260 and height == 720:
                total_size = int(requests.head('http://localhost/Applight/updates/ConveTransfer.msi?raw=true').headers.get('Content-Length'))
                self.t1 = threading.Thread(target=self.convetransfer_1280_720, args=(total_size,))
                self.t1.start()
            # elif width == 1680 and height == 770:
            #     total_size = int(requests.head('http://localhost/suplike/socketra/updates/ConveTransfer.msi?raw=true').headers.get('Content-Length'))
            #     self.t1 = threading.Thread(target=self.convetransfer_1280_720, args=(total_size,))
            #     self.t1.start()
            elif width == 1366 and height == 768:
                total_size = int(requests.head('http://localhost/Applight/updates/ConveTransfer.msi?raw=true').headers.get('Content-Length'))
                self.t1 = threading.Thread(target=self.convetransfer_1366_768, args=(total_size,))
                self.t1.start()
            elif width == 1536 and height == 864:
                total_size = int(requests.head('http://localhost/Applight/updates/ConveTransfer.msi?raw=true').headers.get('Content-Length'))
                self.t1 = threading.Thread(target=self.convetransfer_1536_864, args=(total_size,))
                self.t1.start()
            else:
                # raise Exception("No match found for the current screen resolution.")
                total_size = int(requests.head('http://localhost/Applight/updates/ConveTransfer.msi?raw=true').headers.get('Content-Length'))
                self.t1 = threading.Thread(target=self.convetransfer_1366_768, args=(total_size,))
                self.t1.start()
        except Exception as e:
            print(f'The Error is here! {e}')
            print('Could not find a match')



if __name__ == '__main__':
    APP = Matchmaker()
    APP.find_match()
    APP.mainloop()
#
#In this updated code, the `Matchmaker` class is responsible for creating the main window of the application. The `find_match` method is used to find a match for the current screen size by making an HTTP request to a server. If a match is found, the `convetransfer_1280_720` method is called to download the update file and display the progress. The `install_update` method is used to install the downloaded update file.