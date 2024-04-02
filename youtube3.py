#from packages import *
from resourcepath import resource_path, resource_path2
from tkinter.messagebox import showinfo, showerror, askokcancel
from tkinter import filedialog
from pytube import YouTube
import threading
import ttkbootstrap as ttk
from PIL import Image,ImageTk
from tkinter import filedialog, messagebox
import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
def youtube_tab(self):
    def translate_notification(text):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(text, text)
    
    def open_directory():
        file = filedialog.askdirectory()
        savefolder_var.set(file)

    def download_video():
        # the try statement to excute the download the video code
        message_ico = resource_path(relative_path='images/unt.ico')
        self.iconbitmap(default=message_ico)
        # def translate_message_box(title_key, message_key):
        #     if self.current_language in self.translations:
        #         translation_dict = self.translations[self.current_language]
        #     else:
        #         translation_dict = self.translations['en']  # Fallback to English if the language is not found

        #     title = translation_dict.get(title_key)
        #     message = translation_dict.get(message_key)
            
        #     message_ico = resource_path(relative_path='images/unt.ico')
        #     self.iconbitmap(default=message_ico)
        #     return messagebox.showinfo(title, message)
        try:
            # getting video url from entry
            video_link = Entry_link.get()
            # getting video resolution from Combobox
            resolution = video_resolution.get()
            # getting the saved directory
            savefolder = savefolder_var.get()
            # checking if the entry and combobox is empty
            if resolution == '' and video_link == '':
                # display error message when combobox is empty
                m1 = translate_notification('Please enter both the video URL and resolution!!')
                
                showerror(title='Error', message=m1)
            # checking if the resolution is empty
            elif resolution == '':
                # display error message when combobox is empty
                m2 = 'Please select a video resolution!!'
                showerror(title='Error', message= m2)
            # checking if the comboxbox value is None  
            elif resolution == 'None':
                # display error message when combobox value is None
                m3 = translate_notification('None is an invalid video resolution!!, please select a valid video resolution')
                showerror(title='Error', message= m3)    
            # else let's download the video  
            else:
                # this try statement will run if the resolution exists for the video
                try:   
                    # this function will track the video download progress
                    def on_progress(stream, chunk, bytes_remaining):
                        # the total size of the video
                        total_size = stream.filesize    
                        # this function will get the size of the video
                        def get_formatted_size(total_size, factor=1024, suffix='B'):
                            # looping through the units
                            for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
                                if total_size < factor:
                                    return f"{total_size:.2f}{unit}{suffix}"
                                total_size /= factor
                            # returning the formatted video size
                            return f"{total_size:.2f}Y{suffix}"
                        
                        # getting the formatted video size calling the function
                        formatted_size = get_formatted_size(total_size)
                        # the size downloaded after the start
                        bytes_downloaded = total_size - bytes_remaining
                        # the percentage downloaded after the start
                        percentage_completed = round(bytes_downloaded / total_size * 100)
                        # updating the progress bar value
                        progress_bar['value'] = percentage_completed
                        # updating the empty label with the percentage value
                        progress_label.config(text=str(percentage_completed) + '%, File size:' + formatted_size)
                        # updating the main window of the app
                        self.tab2.update()
                    
                    # creating the YouTube object and passing the the on_progress function
                    video = YouTube(video_link, on_progress_callback=on_progress)
                    # downlaoding the actual video  
                    video.streams.filter(res=resolution).first().download(output_path = savefolder)
                    # popup for dispalying the video downlaoded success message
                    m4 = translate_notification('Video has been downloaded successfully.')
                    showinfo(title='Download Complete', message=m4)
                    
                    # ressetting the progress bar and the progress label
                    progress_label.config(text='')
                    progress_bar['value'] = 0
                # the except will run when the resolution is not available or invalid
                except:
                    m5 = translate_notification('Failed to download video for this resolution')
                    showerror(title='Download Error', message= m5 )
                    # ressetting the progress bar and the progress label
                    progress_label.config(text='')
                    progress_bar['value'] = 0
        # the except statement to catch errors, URLConnectError, RegMatchError  
        except:
            # popup for displaying the error message
            m6a = translate_notification('An error occurred while trying to')
            m6b = translate_notification('download the video. The following could')
            m6c = translate_notification('be the causes:')
            m6d = translate_notification('Invalid link or no internet connection.')
            m6e = translate_notification('Make sure you have stable internet connection and the video link is valid.')
            showerror(title='Download Error', message=f"{m6a}" \
                    f'{m6b}' \
                    f'{m6c}\n'\
                    f'{m6d}\n' \
                    f'{m6e}\n')
            # showerror(title='Download Error', message=f"{m6a}" \
            #             'download the video\nThe following could ' \
            #             'be the causes:\n->Invalid link\n->No internet connection\n'\
            #             'Make sure you have stable internet connection and the video link is valid')
            

            # ressetting the progress bar and the progress label
            progress_label.config(text='')
            progress_bar['value'] = 0

    # function for searching video resolutions
    def searchResolution():
        message_ico = resource_path(relative_path='images/unt.ico')
        self.iconbitmap(default=message_ico)
        # getting video url from entry
        video_link = Entry_link.get()
        # checking if the video link is empty
        if video_link == '':
            m7 = translate_notification('Provide the video link please!')
            showerror(title='Error', message= m7)
        # if video link not empty search resolution  
        else:
            try:
                # creating a YouTube object
                video = YouTube(video_link)
                # an empty list that will hold all the video resolutions
                resolutions = []
                # looping through the video streams
                for i in video.streams.filter(file_extension='mp4'):
                    # adding the video resolutions to the resolutions list
                    resolutions.append(i.resolution)
                # adding the resolutions to the combobox
                video_resolution['values'] = resolutions
                # when search is complete notify the user
                m8 = translate_notification('Resolutions are available now, check the resolution box to select a resolution to download.')
                showinfo(title='Search Complete', message=m8)
            # catch any errors if they occur  
            except:
               
                m9a = translate_notification("An error occurred while searching for video resolutions!")
                m9b = translate_notification('Below might be the causes')
                m9c = translate_notification('->Unstable internet connection')
                m9d = translate_notification('->Invalid link')
                # notify the user if errors are caught
                showerror(title='Error', message=f'{m9a}\n'\
                    f'{m9b}\n'\
                    f'{m9c}\n'\
                    f'{m9d}')
    
    def callback_select_all(event):
        # select text after 50ms
        self.link_frame.after(50, lambda: event.widget.select_range(0, 'end'))

    def show_context_menu(event, *args):
        e_widget = event.widget
        context_menu = ttk.Menu(self.link_frame, tearoff=0)
        context_menu.add_command(label="Cut")
        context_menu.add_command(label="Copy")
        context_menu.add_command(label="Paste")
        context_menu.add_separator()
        context_menu.add_command(label="Select all")
        context_menu.entryconfigure("Cut", command=lambda: e_widget.event_generate("<<Cut>>"))
        context_menu.entryconfigure("Copy", command=lambda: e_widget.event_generate("<<Copy>>"))
        context_menu.entryconfigure("Paste", command=lambda: e_widget.event_generate("<<Paste>>"))
        context_menu.entryconfigure("Select all", command=lambda: e_widget.select_range(0, 'end'))
        context_menu.tk.call("tk_popup", context_menu, event.x_root, event.y_root)
    
    

    def searchThread():
        t1 = threading.Thread(target=searchResolution)
        t1.start()
        
        
    # the function to run the download_video function as a thread   
    def downloadThread():
        t2 = threading.Thread(target=download_video)
        t2.start()

    #self.youtubeframe = ttk.Frame(self.tab2, width=700, height=500, bootstyle='light')
    self.youtubeframe = ScrolledFrame(self.tab2,width=1750, height=1500, autohide=True)
    self.youtubeframe.pack(fill='y', side='left', padx=(1, 1), pady=1)

    # Load the YouTube icon image
    youtubeico = Image.open(resource_path2('images/youtube.png'))
    youtubeico = youtubeico.resize((90,90))
    youtubeico = ImageTk.PhotoImage(youtubeico)
    self.youtubeico = youtubeico  # Keep a reference to the image object
    youtubelabel = ttk.Label(self.youtubeframe, image=youtubeico, bootstyle='light')
    youtubelabel.pack()

    self.link_frame = ttk.Frame(self.youtubeframe)
    self.link_frame.pack(padx=10, pady=(10, 0))

    self.Label_link = ttk.Label(self.link_frame, text=translate_notification("Link:"),font=('calibre', 10, 'normal'))
    self.Label_link.pack(side='left', padx=(5,39))

    link_var = ttk.StringVar()
    link_var.set("")
    Entry_link = ttk.Entry(self.link_frame, width=48, textvariable=link_var, font=('calibre', 10, 'normal'))
    Entry_link.bind("<Button-3><ButtonRelease-3>", show_context_menu)
    Entry_link.bind("<Control-a>", callback_select_all)
    Entry_link.pack(side='left')
    

    # Create a frame for the Save To label and entry
    save_folder_frame = ttk.Frame(self.youtubeframe)
    save_folder_frame.pack(padx=10, pady=10)

    self.Label_savefolder = ttk.Label(save_folder_frame, text=translate_notification("Save To:"), font=('calibre', 10, 'normal'))
    self.Label_savefolder.pack(side='left')

    savefolder_var = ttk.StringVar()
    savefolder_var.set("")
    Entry_savefolder = ttk.Entry(save_folder_frame, width=48, textvariable=savefolder_var, font=('calibre', 10, 'normal'))
    Entry_savefolder.pack(side='left')
    op = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/folder.png')))
    openbutton = ttk.Button(save_folder_frame,command=open_directory, image=op, width=10, bootstyle='link')
    openbutton.pack(side='left', padx=(4,30))
    openbutton.image = op

    resolution_frame = ttk.Frame(self.youtubeframe)
    resolution_frame.pack(padx=10, pady=10)

    self.vid_resolution_label = ttk.Label(resolution_frame, text=translate_notification('Resolution'), font=('calibre', 10, 'normal'))
    self.vid_resolution_label.pack(side='left')

    video_resolution = ttk.Combobox(resolution_frame, width=10)
    video_resolution.pack(side='left', padx=(4, 20))

    oq = Image.open(resource_path2(relative_path='images/search.png'))
    oq = oq.resize((29,29))
    oq = ImageTk.PhotoImage(oq)
    vid_resolution_but = ttk.Button(resolution_frame, image=oq, width=2, command=searchThread, bootstyle='link')
    vid_resolution_but.pack(side='left')
    vid_resolution_but.image = oq

    progress_frame = ttk.Frame(self.youtubeframe)
    progress_frame.pack(padx=10, pady=10)

    progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', length=450, mode='determinate', bootstyle='success-striped')
    progress_bar.pack(side='left')

    progress_label = ttk.Label(progress_frame, text='')
    progress_label.pack(side='left', padx=(4, 15))

    control_buttons = tk.Frame(self.youtubeframe)
    control_buttons.pack(padx=10, pady=10)
    self.youtube_download_butt = ttk.Button(control_buttons,text=translate_notification("Download"), command=downloadThread)
    self.youtube_download_butt.pack()

    #    9&5ba6&XyYwtZ#M