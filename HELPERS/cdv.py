import tkinter as tk
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from PIL import Image,ImageTk,ImageOps
import webbrowser
from tkinter import font
import psutil as ps
import threading
import datetime
from tkinter import filedialog, messagebox
import socket
import time
import connection
from ttkbootstrap import Style
from tkinter import simpledialog
import ctypes
import requests
from updatemanager import UpdateManager
from resourcepath import resource_path, resource_path2
from receiveloc import receive_loc
import get_ip

from progresswin import ProgressWindow
from about import DisplayAboutMe

from metadata import __version__ 
from metadata import __AppName__
connection.Database()

from metadata import __version__ 
from metadata import __AppName__

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        def about_me():
            DisplayAboutMe(self)

        self.title(__AppName__ + ' ' + str(__version__))
        w = 980
        h = 400
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=True, height=True)
        self.iconpath = resource_path('images/unt.ico')
        
        self.iconbitmap(self.iconpath)

        self.menubar = ttk.Menu(self)
        self.filemenu = ttk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Exit',command=self.destroy)
        self.filemenu.add_command(label='open',command=self.destroy)
        self.menubar.add_cascade(label='File',menu=self.filemenu)

        self.helpmenu = ttk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='About',command=about_me)
        self.menubar.add_cascade(label='Help',menu=self.helpmenu)
        self.config(menu=self.menubar)

        self.button_frame = ttk.Frame(self,borderwidth=3,relief='groove')
        self.button_frame.pack(fill='x',side='top')
        
        self.button_frame = ttk.Frame(self,borderwidth=3,relief='groove')
        self.button_frame.pack(fill='x',side='top')

        self.s = ttk.Style()
        self.s.configure('Link.TButton',font=('Helvetica'))

        self._select = ImageTk.PhotoImage(Image.open('images/exit.png'))
        self.select_button = ttk.Button(self.button_frame,image=self._select,state='normal',bootstyle='Link.Tbutton',command=self.send_file)
        self.select_button.pack(side=tk.LEFT,padx=1,pady=1)
        self.select_button.image = self._select
        
        self._receive = ImageTk.PhotoImage(Image.open('images/exit.png'))
        self.receive_button = ttk.Button(self.button_frame, image=self._receive,state='normal',bootstyle='Link.Tbutton',command=self.receive_file)
        self.receive_button.pack(side=tk.LEFT,padx=1,pady=1)
        self.receive_button.image = self._receive

        self._stop = ImageTk.PhotoImage(Image.open('images/exit.png'))
        self.stop_button = ttk.Button(self.button_frame, state='disabled',command=self.stop_transfer,image=self._stop,bootstyle='Link.Tbutton')
        self.stop_button.pack(side=tk.LEFT,padx=1,pady=1)
        self.stop_button.image = self._stop
        self._update = ImageTk.PhotoImage(Image.open('images/exit.png'))
        self.update_button = ttk.Button(self.button_frame,image=self._update,bootstyle='Link.Tbutton',command=self.update_using_manager)
        self.update_button.pack(side=tk.LEFT,padx=1,pady=1)
        self.update_button.image = self._update
        
        


        self.host = ttk.StringVar() 
        self.port = ttk.StringVar()
        self.loc = ttk.StringVar()
        self.perce = ttk.DoubleVar(value=0)

        self.entries = ttk.Frame(self)
        self.entries.pack(fill='y',side='left',padx=5,pady=4)
        
        self.labelid = ttk.Label(self.entries,text='IP',font=('arial',10,'bold'),background='#FFFFFF')
        self.labelid.pack(side=tk.TOP,padx=(2,2),pady=2)
        self.stuff = ['127.0.0.1',f'{self.wifi}']
        self.senderid = ttk.Spinbox(self.entries,values=self.stuff,textvariable=self.host)
        self.senderid.pack(side=tk.TOP,padx=(2,2),pady=2)

        
        self.labelport = ttk.Label(self.entries,text='Port',font=('arial',10,'bold'),background='#FFFFFF')
        self.labelport.pack(side=tk.TOP,padx=(2,2),pady=(3,3))
        self.stuff1 = [4444,8080]
        self.portid = ttk.Spinbox(self.entries,values=self.stuff1,textvariable=self.port,takefocus=4444)
        self.portid.pack(fill='y',padx=2,pady=(2,2))
        
        self.labelloc = ttk.Label(self.entries, text="Receive Dir:", font=('aria',10,'bold'))
        self.labelloc.pack(side=tk.TOP,padx=(2,2),pady=2)
        self.stuff2 = [f'{self.desktop}', f'{self.documents}', f'{self.videos}', f'{self.music}', f'{self.downloads}', f'{self.pictures}']
        self.location = ttk.Spinbox(self.entries,values=self.stuff2,textvariable=self.loc)  
        self.location.pack(fill='y',padx=2,pady=(3,3))  
        

        self.t_time = ttk.Label(self.entries, text="")
        self.t_time.pack(side=tk.TOP,padx=(2,2),pady=(4,4))

        self.note = ttk.Notebook(self)
        self.tab = ttk.Frame(self.note)

        columns = ("sent", "date", "size","received")
    
        self.table = ttk.Treeview(self.tab, bootstyle='info', columns=columns, show="headings")
        
        self.table.heading("sent", text="sent", anchor="center")
        self.table.heading("date", text="date", anchor="center")
        self.table.heading("size", text="size", anchor="center")
        self.table.heading("received", text="recieved", anchor="center")
        
        # self.tree.column("name", anchor="center")
        # self.tree.column("finished", anchor="center")
        # self.tree.column("time", anchor="center")

        self.table.pack(fill=tk.BOTH, expand=1)
        self.note.add(self.tab)
        self.note.pack(fill=tk.BOTH, expand=1)

        
        
        self.transferred_files = []
        #self.populateview()
    
    def update_using_manager(self):
        try:
            # -- Online Version File
            # -- Replace the url for your file online with the one below.
            response = requests.get(
                'http://localhost/suplike/socketra/updates/version.txt')
            data = response.text

            if float(data) > float(__version__):
                messagebox.showinfo('Software Update', 'Update Available!')
                mb2 = messagebox.askyesno('Update!', f'{__AppName__} {__version__} needs to update to version {data}')
                if mb2 is True:
                    UpdateManager(self)
                elif mb2 == 'No':
                    pass
            else:
                messagebox.showinfo('Software Update', 'No Updates are Available.')
        except Exception as e:
            print('The Error is here!')
            messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))
    
    desktop, documents, videos, music, downloads, pictures = receive_loc()
    
    def populateview(self):
        self.table.delete(*self.table.get_children())
        fetch = connection.get_transferred_files()
        # for data in fetch:
        #     self.table.insert("", "end", values=(data[1],data[2],data[3]))
        for idx, data in enumerate(fetch):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.table.insert("", 0, values=(data[1], data[2], data[3], data[4]), tags=(tag,))

    wifi = get_ip.get_ip('wlan0')

    def stop_transfer(self):
        if hasattr(self, 'client_socket') and self.client_socket:
            self.client_socket.close()
        if hasattr(self, 'server_socket') and self.server_socket:
             self.server_socket.close()
        
    
    def disable_buttons(self):
        self.select_button.configure(state='disabled')
        self.receive_button.configure(state='disabled')
    
    def enable_buttons(self):
        self.select_button.configure(state='normal')
        self.receive_button.configure(state='normal')
    def stop_enable(self):
        
        self.stop_button.configure(state='normal')

    def stop_disable(self):
        
        self.stop_button.configure(state='disabled')




    def send_file(self):
        self.disable_buttons()
        
        self.filepath = filedialog.askopenfilename()
        self.filename = os.path.basename(self.filepath)
        self.HOST = self.host.get()
        self.PORT = self.port.get()
        
        if self.PORT == "":
            self.PORT = 4444
        else:
            self.PORT = int(self.PORT)

        self.send_stop = False

        
        try:
            total_size = os.path.getsize(self.filepath)
            convert = total_size
            # convert = convert/(1024*1024)
            # convert = float(f"{convert:.2F}")
            if total_size < 1024:
                size_units = 'B'
                formatted_size = f"{convert} {size_units}"
            elif total_size < 1024**2:
                size_units = 'KB'
                convert/= 1024
                formatted_size = f"{convert:.2f} {size_units}"
            elif total_size < 1024**3:
                size_units = 'MB'
                convert/=(1024*1024)
                formatted_size = f"{convert:.2f} {size_units}"
            else:
                size_units = 'GB'
                convert/=(1024*1024*1024)
                formatted_size = f"{convert:.2f} {size_units}"
            self.stop_enable()
        except:
            
            self.message = messagebox.showinfo('Response', "It seems your selection was empty")
            # If unable to get total size, re-enable the buttons and return
            self.enable_buttons()
            return
        
        progress_window = ProgressWindow(self, total_size)

        def transfer_file():
           
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
                    self.client_socket.connect((self.HOST, self.PORT))
                    #self.client_socket.sendall(self.filename.encode())
                    
                    filename_with_size = f"{self.filename}:{total_size}"

                    # Send the filename_with_size to the receive_file method
                    self.client_socket.sendall(filename_with_size.encode())


                    bytes_sent = 0

                    def update_estimated_time_remaining(bytes_sent, total_size, start_time):
                        current_time = time.time()
                        elapsed_time = current_time - start_time
                        transfer_rate = bytes_sent / elapsed_time if elapsed_time > 0 else 0
                        remaining_bytes = total_size - bytes_sent
                        estimated_time_remaining = remaining_bytes / transfer_rate if transfer_rate > 0 else 0
                        return estimated_time_remaining
                    start_time = time.time() 

                    with open(self.filepath, 'rb') as self.file:
                        self.data = self.file.read(4096)
                        while self.data:
                            
                            if self.send_stop:
                                break
                            self.client_socket.sendall(self.data)
                            bytes_sent += len(self.data)
                            progress = (bytes_sent / total_size) * 100
                            progress_window.progress_bar['value'] = bytes_sent
                            self.update_idletasks()
                            
                    
                            estimated_time_remaining = update_estimated_time_remaining(bytes_sent, total_size, start_time)
                            
                            self.t_time.configure(text=f"{int(progress)}%   {estimated_time_remaining:.1f} secs")
                            
                            self.data = self.file.read(4096)
                    
                        

                    print("File sent successfully.")
                    self.message = messagebox.showinfo('Response', f"File {self.filename} sent successfully")
                    # Get the current timestamp
                    # current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # max_filename_length = 20  # Adjust this value as needed
                    # displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')
    
                    # self.transferred_files.append((f"{displayed_filename}",f"{current_time}"))
                    # self.table.insert("", "end", values=(f"{displayed_filename}",f"{current_time}"))


                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    max_filename_length = 30  # Adjust this value as needed
                    displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')
    
                    self.transferred_files.append((f"{displayed_filename}",f"{current_time}",f"{formatted_size}"))
                    #self.table.delete(*self.table.get_children())
                    for idx, data in enumerate(self.transferred_files):
                        tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
                    self.table.insert("", 0, values=(f"{displayed_filename}",f"{current_time}",f"{formatted_size}"),tags=(tag,))
                    connection.insert_sent_file(displayed_filename, current_time, formatted_size)

                   



                    



                    
                    
                    # self.table.delete(*self.table.get_children()) 
                    # for item, item2 in self.transferred_files:
                    #     if progress != 100:
                    #         self.table.insert("", "end", values=(item,item2,))
                    #     else:
                    #         self.table.insert("", "end", values=(item,item2,))

                    
                    

            except Exception as e:
                #print(f'This is the reason {e}')
                if self.HOST == '':
                    self.message = messagebox.showerror('Response', "The IP can\'t be empty")
                elif self.HOST == self.wifi:
                    self.message = messagebox.showerror('Response', "Please use the receiver's IP not your IP")
                elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                    self.message = messagebox.showerror('Response', f"{self.HOST} is a wrong IP address format")
                elif len(self.HOST) > 15 or len(self.HOST) < 8:
                    self.message = messagebox.showinfo('Response', f"{self.HOST} is not Valid IP \n cool: 192.168.134.12 \n not cool: 192.168.134.12.1")

            finally:
                # Destroy the progress window
                progress_window.destroy()
                # Reactivate the button once the event is completed or an error occurs
                self.enable_buttons()
                self.stop_disable()
                self.t_time.configure(text='')
               
                

        # Start the file transfer in a separate thread
        threading.Thread(target=transfer_file).start()
    
    def receive_file(self):       

        self.stop_receive = False
        
        def receive_thread(): 
            # self.PORT = self.port.get()
            # if self.PORT == "":
            #     self.PORT = 4444
            # else:
            #     self.PORT = int(self.PORT)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.server_socket:
                try:
                    self.HOST = self.host.get()
                    self.PORT = self.port.get()
                    self.HOST = str(self.HOST) 
                    self.PORT = int(self.PORT)
                    self.location = self.loc.get()
                    
                    
                    if self.location == '':
                        self.message = messagebox.showwarning('Response', 'The Receiving Dir path is not specified')
                    else: 
                        
                        self.server_socket.bind((self.HOST, self.PORT))
                        self.server_socket.listen()

                        print("Server is waiting for connections...")

                        self.conn, self.addr = self.server_socket.accept()

                    

                    
                    
                    #self.filename = self.conn.recv(1024).decode()
                    filename_with_size = self.conn.recv(1024).decode()
                    self.filename, total_size = filename_with_size.split(':')
                    total_size = int(total_size)
                    convert = total_size
                    if total_size < 1024:
                        size_units = 'B'
                        formatted_size = f"{convert} {size_units}"
                    elif total_size < 1024**2:
                        size_units = 'KB'
                        convert/= 1024
                        formatted_size = f"{convert:.2f} {size_units}"
                    elif total_size < 1024**3:
                        size_units = 'MB'
                        convert/=(1024*1024)
                        formatted_size = f"{convert:.2f} {size_units}"
                    else:
                        size_units = 'GB'
                        convert/=(1024*1024*1024)
                        formatted_size = f"{convert:.2f} {size_units}"
                    self.disable_buttons()
                    self.stop_disable()
                    
                    self.file_path = os.path.join(self.location, self.filename)
                    with open(self.file_path, 'wb') as file:
                        data = self.conn.recv(4096)
                        while data:
                            if self.stop_receive:
                                break
                            file.write(data)
                            data = self.conn.recv(4096)

                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    max_filename_length = 20  # Adjust this value as needed
                    displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')

                    self.transferred_files.append(("",f"{current_time}",f"{formatted_size}",f"{displayed_filename}"))
                    #self.table.delete(*self.table.get_children())
                    for idx, data in enumerate(self.transferred_files):
                        tag = 'evenrow' if idx % 2 == 0 else 'oddrow'

                    self.table.insert("", 0, values=("", current_time, formatted_size, displayed_filename),tags=(tag,))
                    connection.insert_received_file(displayed_filename, current_time,formatted_size)
                    
                        
                    if not self.stop_receive:
                        print(f"File '{self.filename}' received and saved successfully.")
                        self.message = messagebox.showinfo('Response', f"File {self.filename} received successfully")
                        
                    else:
                        print("Transfer stopped by user.")  
                        
                    
                except:
                    if self.HOST == '':
                        self.message = messagebox.showerror('Response', "The IP can\'t be empty")
                    elif self.HOST == self.wifi:
                        self.message = messagebox.showerror('Response', "Please use the receiver's IP not your IP")
                    elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                        self.message = messagebox.showerror('Response', f"{self.HOST} is a wrong IP address format")
                    elif len(self.HOST) > 15 or len(self.HOST) < 8:
                        self.message = messagebox.showinfo('Response', f"{self.HOST} is not Valid IP \n cool: 192.168.134.12 \n not cool: 192.168.134.12.1")
                finally:
                    self.enable_buttons()
                           
        threading.Thread(target=receive_thread).start()









# class DisplayAboutMe(tk.Toplevel):
#     def __init__(self, parent):
#         tk.Toplevel.__init__(self, parent)

#         self.transient(parent)
#         self.result = None
#         self.grab_set()
#         w = 285
#         h = 273
#         sw = self.winfo_screenwidth()
#         sh = self.winfo_screenheight()
#         x = (sw - w) / 2
#         y = (sh - h) / 2
#         self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
#         self.resizable(width=False, height=False)
#         self.title('About')
#         self.wm_iconbitmap('images/Graphicloads-Android-Settings-Contact.ico')

#         self.image = Image.open('images/vs.png')
#         self.size = (100, 100)
#         self.thumb = ImageOps.fit(self.image, self.size)
#         self.photo = ImageTk.PhotoImage(self.thumb)
#         logo_label = tk.Label(self, image=self.photo)
#         logo_label.pack(side=tk.TOP, pady=10)

#         f1 = tk.Frame(self)
#         f1.pack()
#         f2 = tk.Frame(self)
#         f2.pack(pady=10)
#         f3 = tk.Frame(f2)
#         f3.pack()

#         def call_link(*args):
#             webbrowser.open_new_tab('https://www.youtube.com/c/mechanizecode')

#         tk.Label(f1, text=__AppName__ + ' ' + str(__version__)).pack()
#         tk.Label(f1, text='Copyright (C) 2020 Victor Santiago').pack()
#         tk.Label(f1, text='All rights reserved').pack()

#         f = font.Font(size=10, slant='italic', underline=True)
#         label1 = tk.Label(f3, text='MechanizeCode', font=f, cursor='hand2')
#         label1['foreground'] = 'blue'
#         label1.pack(side=tk.LEFT)
#         label1.bind('<Button-1>', call_link)
#         ttk.Button(self, text='OK', command=self.destroy).pack(pady=5)




if __name__ == "__main__":
    root = Root()
    root.mainloop()

