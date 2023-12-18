# Import necessary libraries
import tkinter as tk
# import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ctypes
import requests
import win32api
import tempfile
import threading
from metadata import __AppName__
from resourcepath import resource_path
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import socket
import uuid
import datetime
from tkinter.messagebox import showerror

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
       
        
        # Google Sheets API credentials
        # self.creds = ServiceAccountCredentials.from_json_keyfile_name(
        #     resource_path(relative_path="creds.json"),  # Replace with the path to your JSON file
        #     ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"],
        # )
        # self.client = gspread.authorize(self.creds)
        

        # def get_country():
        #     try:
        #         # Make a request to ipinfo.io to get information about the public IP address
        #         response = requests.get('https://ipinfo.io')
        #         data = response.json()
                
        #         # Extract the country from the response
        #         country = data.get('country')
                
        #         if country:
        #             return country
        #         else:
        #             return 'Country not found'
        #     except Exception as e:
        #         return f'Error: {e}'

        # # Example usage
        # country = get_country()

        # # UI elements
        # self.install_id = str(uuid.uuid4())  # Generate a unique ID for each installation
        # # Access your Google Sheet by title
        # sheet = self.client.open("CONVETRANSFER_DATA").sheet1  # Replace with your sheet title
        # hostname = socket.gethostname()
        # ip_address = socket.gethostbyname(hostname)
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # screensized = str(self.screensize) 
        # sheet.append_row([self.install_id, country, timestamp, hostname, ip_address, screensized])
        

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
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            resource_path(relative_path="creds.json"),  # Replace with the path to your JSON file
            ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"],
        )
        self.client = gspread.authorize(self.creds)
        

        def get_country():
            try:
                # Make a request to ipinfo.io to get information about the public IP address
                response = requests.get('https://ipinfo.io')
                data = response.json()
                
                # Extract the country from the response
                country = data.get('country')
                
                if country:
                    return country
                else:
                    return 'Country not found'
            except Exception as e:
                return f'Error: {e}'

        # Example usage
        country = get_country()

        # UI elements
        self.install_id = str(uuid.uuid4())  # Generate a unique ID for each installation
        # Access your Google Sheet by title
        sheet = self.client.open("CONVETRANSFER_DATA").sheet1  # Replace with your sheet title
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        screensized = str(self.screensize) 
        sheet.append_row([self.install_id, country, timestamp, hostname, ip_address, screensized])
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
        # except Exception as e:
        #     showerror(title='Error' , message=f'Please connect to the internet to download the resources. {e}')

        except requests.exceptions.RequestException:
            message_ico = resource_path(relative_path='images/unt.ico')
            self.iconbitmap(default=message_ico)
            showerror(title='Error' , message=f'Please connect to the internet to download the resources.')
            self.downloadss.config(text='Error: No internet connection')
            self.progressbar.destroy()
            self.button1.destroy()
            self.t_time.destroy()
            APP.destroy()

        



if __name__ == '__main__':
    APP = Matchmaker()
    APP.find_match()
    APP.mainloop()
#
#In this updated code, the `Matchmaker` class is responsible for creating the main window of the application. The `find_match` method is used to find a match for the current screen size by making an HTTP request to a server. If a match is found, the `convetransfer_1280_720` method is called to download the update file and display the progress. The `install_update` method is used to install the downloaded update file.