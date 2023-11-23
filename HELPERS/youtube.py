import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox
# from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from resourcepath import resource_path, resource_path2

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
class wintube(ttk.Window):
    folder_image = None
    def __init__(self):
        super().__init__()
        
        def open_directory():
            file = filedialog.askdirectory()
            savefolder_var.set(file)

        
        
        def download_video():
            file_type = Combo_filetype.get()
            print(file_type)
            link = Entry_link.get()
            savefolder = savefolder_var.get()
            yt = YouTube(link)
            ytresolution = Combo_fileres.get()
            if('mp4' in file_type):
                print(f"Youtube Link  : {link}")
                print(f"File Saved In : {savefolder}")
                try:
                    yt.streams.filter(progressive = True, 
                file_extension = "mp4").first().download(output_path = savefolder, 
                filename = (yt.title + '.mp4'))
                    messagebox.showinfo('PavK YouTube Video Downloader','File Downloaded!\nCheck the given directory.')
                except:
                    print("Error!")
                    messagebox.showerror("Download",'Error!\nCheck your internet connection.')
            elif('mp3' in file_type):
                try:
                    video = yt.streams.filter(only_audio=True).first()
                    out_file = video.download(output_path=savefolder)
                    file_name = yt.title
                    new_file = file_name + '.mp3'
                    os.rename(out_file, new_file)
                    messagebox.showinfo('PavK YouTube Video Downloader','File Downloaded!\nCheck the given directory.')
                except:
                    print("Error!")
                    messagebox.showerror("Download",'Error!\nCheck your internet connection.')


        app_title = 'PavK YouTube Video Downloader'
        app_geometry = '900x450'
        # if wintube.folder_image is None:
        #     wintube.folder_image = ImageTk.PhotoImage(Image.open(resource_path('Assests\\folder.png')))

        #folder_image = ImageTk.PhotoImage(file='Assests\\folder.png')
        self.title(app_title)
        self.geometry(app_geometry)
        self.resizable(False,False)
        #self.wm_iconphoto(default='Assests\pavk.png')

        # Frame_full = ttk.Frame(self)
        # Frame_full.place(x=0,y=0)
        tk.Label(self,text="ConveTransfer Youtube DL",font="arial 12").pack(padx=10)

        link_frame = tk.Frame(self)
        link_frame.pack(padx=10, pady=(10, 0))

        Label_link = tk.Label(link_frame, text="Link:")
        Label_link.pack(side='left')

        link_var = ttk.StringVar()
        link_var.set("")
        Entry_link = ttk.Entry(link_frame, width=48, textvariable=link_var, font=('calibre', 10, 'normal'))
        Entry_link.pack(side='left',padx=(30,4))
       
        # Create a frame for the Save To label and entry
        save_folder_frame = tk.Frame(self)
        save_folder_frame.pack(padx=10, pady=10)

        Label_savefolder = tk.Label(save_folder_frame, text="Save To:")
        Label_savefolder.pack(side='left')

        savefolder_var = ttk.StringVar()
        savefolder_var.set("")
        Entry_savefolder = ttk.Entry(save_folder_frame, width=48, textvariable=savefolder_var, font=('calibre', 10, 'normal'))
        Entry_savefolder.pack(side='left')
        #op = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/folder.png')))
        openbutton = ttk.Button(save_folder_frame,command=open_directory, text='Open', width=10)
        openbutton.pack(side='left', padx=(4,30))
        #openbutton.image = op
        
        Label_filetype_frame = tk.Frame(self)
        Label_filetype_frame.pack(padx=10, pady=10)
        Label_filetype = tk.Label(Label_filetype_frame,text= "File Type:")
        Label_filetype.pack(side='left')
        Combo_filetype = ttk.Combobox(Label_filetype_frame,width=48,values=("mp4 (video)",
        "mp3 (audio)"))
        Combo_filetype.set("mp4 (video)")
        Combo_filetype.pack(side='left')

        Label_fileres_frame = tk.Frame(self)
        Label_fileres_frame.pack(padx=10, pady=10)
        Label_fileres = tk.Label(Label_fileres_frame,text= "Resolution:")
        Label_fileres.pack(side='left')
        Combo_fileres = ttk.Combobox(Label_fileres_frame,width=48,values=('144p','240p','360p',
        '480p','720p','1080p'))
        Combo_fileres.set('480p')
        Combo_fileres.pack(side='left')

        control_buttons = tk.Frame(self)
        control_buttons.pack(padx=10, pady=10)
        ttk.Button(control_buttons,command=download_video,text="Download").pack()
        


if __name__ == "__main__":
    root = wintube()
    root.mainloop()


        # self.youtubeframe = ttk.Frame(self.tab3, width=700, height=500)
        # self.youtubeframe.pack(pady=10)

        # # Load the YouTube icon image
        # youtubeico = ImageTk.PhotoImage(Image.open(resource_path2('images/youtube.png')))
        # self.youtubeico = youtubeico  # Keep a reference to the image object
        # youtubelabel = ttk.Label(self.youtubeframe, image=youtubeico)
        # youtubelabel.pack()


        # def open_directory():
        #     file = filedialog.askdirectory()
        #     savefolder_var.set(file)

        
        
        # def download_video():
            
        #     try:
                
                
        #         link = Entry_link.get()
        #         savefolder = savefolder_var.get()
        #         yt = YouTube(link, on_progress_callback=on_progress)
        #         video = yt.streams.get_lowest_resolution()
        #         video.download()
        #     except:
        #         print('no internet')
        #     print('completed')
        # logo = Image.open('images/youtube.png')
        # logo = logo.resize((50,50))
        # logo = ImageTk.PhotoImage(logo)

        # fd = ttk.Label(self.tab3,image=logo,font="arial 12")
        # fd.pack(padx=10,pady=5)
        # def on_progress(stream, chunk, bytes_remaining):
        #     total_size = stream.filesize()
        #     bytes_downloaded = total_size - bytes_remaining
        #     percentage_of_completion = bytes_downloaded / total_size * 100
        #     print(percentage_of_completion)

        # link_frame = tk.Frame(self.tab3)
        # link_frame.pack(padx=10, pady=(10, 0))

        # Label_link = tk.Label(link_frame, text="Link:")
        # Label_link.pack(side='left')

        # link_var = ttk.StringVar()
        # link_var.set("")
        # Entry_link = ttk.Entry(link_frame, width=48, textvariable=link_var, font=('calibre', 10, 'normal'))
        # Entry_link.pack(side='left',padx=(30,4))
       
        # # Create a frame for the Save To label and entry
        # save_folder_frame = tk.Frame(self.tab3)
        # save_folder_frame.pack(padx=10, pady=10)

        # Label_savefolder = tk.Label(save_folder_frame, text="Save To:")
        # Label_savefolder.pack(side='left')

        # savefolder_var = ttk.StringVar()
        # savefolder_var.set("")
        # Entry_savefolder = ttk.Entry(save_folder_frame, width=48, textvariable=savefolder_var, font=('calibre', 10, 'normal'))
        # Entry_savefolder.pack(side='left')
        # op = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/folder.png')))
        # openbutton = ttk.Button(save_folder_frame,command=open_directory, image=op, width=10)
        # openbutton.pack(side='left', padx=(4,30))
        # openbutton.image = op
        
    

        # control_buttons = tk.Frame(self.tab3)
        # control_buttons.pack(padx=10, pady=10)
        # ttk.Button(control_buttons,command=download_video,text="Download").pack()

        # pp = ttk.Label(control_buttons, text='0%')
        # pp.pack(pady=5)
        # progr = ttk.Progressbar(control_buttons, length = 300, mode = DETERMINATE)
        # progr.pack(pady=5)