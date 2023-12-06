import tkinter as tk
from PIL import Image, ImageTk
import os
import requests
import tempfile
import win32api
import ttkbootstrap as ttk
import threading
from metadata import __AppName__
from metadata import __version__
from resourcepath import resource_path, resource_path2


class UpdateManager(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 350#450#350
        h = 200#150#200
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
    
        # def backup_database():
        #     db_source = os.path.expanduser('~\\AppData\\Local\\file_transfer.db')
        #     if os.path.isfile(db_source):
        #         temp_dir = tempfile.gettempdir()
        #         destination_dir = os.path.join(temp_dir, "file_transfer.db")
        #         try:
        #             shutil.copy2(db_source, destination_dir)
        #             return destination_dir
        #         except Exception as e:
        #             print(f'Error copying the file {e}')
                
        def install_update():
            tmp = tempfile.gettempdir()
            
            win32api.ShellExecute(0, 'open', f'{tmp}\\{__AppName__}.msi', None, None, 10)
            parent.destroy()
            # backup_path = backup_database()
            # db_source = os.path.expanduser('~\\AppData\\Local\\')
            # if backup_path:
            #     try:
            #         shutil.copy2(backup_path,db_source)
            #         os.remove(backup_path)
            #     except Exception as e:
            #         print(f'Error {e}')
            
            

        def start_update_manager():
            with requests.get('http://localhost/suplike/socketra/'
                    'updates/ConveTransfer.msi?raw=true',stream=True) as r:
                self.progressbar['maximum'] = int(r.headers.get('Content-Length'))
                r.raise_for_status()
                tm = tempfile.gettempdir()
                tm = tm.replace("\\","/")
                with open(f'{tm}/{__AppName__}.msi', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            self.progressbar['value'] += 4096
            self.button1.config(text='Install', state=ttk.NORMAL)

        self.progressbar = ttk.Progressbar(self,
                                           orient='horizontal',
                                           length=200,
                                           mode='determinate',
                                           value=0,
                                           maximum=0,
                                           bootstyle='success-striped')
        self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # self.progressbar = ttk.Floodgauge(self,
        #                                    orient='horizontal',
        #                                    length=720,
        #                                    mode='determinate',
        #                                    value=0,
        #                                    maximum=0,
        #                                    bootstyle='success')
        #                                    
        # self.progressbar.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        self.button1 = ttk.Button(self, text='Wait!',width=9, state=ttk.DISABLED, command=install_update)
        self.button1.place(x=-119, relx=1.0, y=-46, rely=1.0)

        self.t1 = threading.Thread(target=start_update_manager)
        self.t1.start()
