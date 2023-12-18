from pytube import YouTube, Channel, Playlist
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import sys
import subprocess
import threading

global urls
urls = []


def setup_ui(window):
    def load_image_from_url(url, max_width=390):
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))

        # Обмеження ширини та збереження пропорцій
        width, height = img.size
        aspect_ratio = height / width
        new_width = min(max_width, width)
        new_height = int(new_width * aspect_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)

        return ImageTk.PhotoImage(img)

    def extract_formats(obj):
        lst = []
        try:
            for stream in obj.streams:
                only = ''
                if not stream.is_progressive:
                    only = '-only'
                if stream.type == 'video':
                    lst.append(
                        f'{stream.type}{only}    {stream.resolution}    {stream.fps} fps    {int(stream.filesize / (1024 * 1024))} MB')
                else:
                    lst.append(f'{stream.type}{only}    {stream.abr}    {int(stream.filesize / (1024 * 1024))} MB')
            ComboBox1['values'] = lst
            cb_default_text.set(lst[0])
            thumbnail_image = load_image_from_url(obj.thumbnail_url)
            ImgLabel1.config(image=thumbnail_image)
            ImgLabel1.image = thumbnail_image
            window.geometry('400x480')
            window.eval('tk::PlaceWindow . center')
            window.title(obj.title)
        except Exception as _ex:
            window.title('URL is not valid...')

    def download_url_list(lst):
        for n, url in enumerate(lst):
            try:
                if Button1['state'] == NORMAL or ACTIVE:
                    Button1['state'] = DISABLED
                window.title(f'YouTube DownLoader {n+1}/{len(lst)} - {url}')
                yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
                i = ComboBox1.current()
                yt.streams[i].download()
                if n == len(lst)-1:
                    messagebox.showinfo(title='Done!', message='file(s) was successfully downloaded')
            except Exception as _ex:
                window.title('URL is not valid...')

    def on_paste(event):
        global urls
        url = window.clipboard_get()
        ComboBox1['values'] = []
        urls.clear()
        try:
            if url.startswith('https://www.youtube.com/c'):
                c = Channel(url)
                extract_formats(c.videos[0])
                urls = c.video_urls
            elif url.startswith('https://www.youtube.com/playlist?list='):
                p = Playlist(url)
                extract_formats(p.videos[0])
                urls = p.video_urls
            else:
                yt = YouTube(url)
                extract_formats(yt)
                urls.append(url)
        except Exception as _ex:
            window.title('URL is not valid...')

    def on_start():
        t = threading.Thread(target=download_url_list, args=(urls,), )
        t.start()

    def on_open():
        subprocess.Popen(r'explorer "{dir}"'.format(dir=os.path.dirname(sys.argv[0]).replace('/', '\\')))

    def on_complete(stream, file_path):
        current_progress.set(0)
        Button1['state'] = ACTIVE

    def on_progress(stream, chunk, bytes_remaining):
        size = stream.filesize
        p = int(float(abs(bytes_remaining - size) / size) * float(100))
        current_progress.set(p)

    def callback_select_all(event):
        # select text after 50ms
        window.after(50, lambda: event.widget.select_range(0, 'end'))

    def show_contextmenu(event, *args):
        e_widget = event.widget
        context_menu = ttk.Menu(window, tearoff=0)
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

    current_url = ttk.StringVar()
    Edit1 = ttk.Entry(window, bootstyle='default', textvariable=current_url)
    Edit1.bind("<<Paste>>", on_paste)
    Edit1.bind("<Button-3><ButtonRelease-3>", show_contextmenu)
    Edit1.bind("<Control-a>", callback_select_all)
    Edit1.pack(fill=X, padx=5, pady=(10, 5))
    cb_default_text = ttk.StringVar()
    ComboBox1 = ttk.Combobox(window, state='readonly', bootstyle='default', textvariable=cb_default_text)
    ComboBox1.pack(fill=X, padx=5, pady=5)
    ImgLabel1 = ttk.Label(window)
    ImgLabel1.pack(fill=X, padx=5)
    current_progress = ttk.IntVar()
    current_progress.set(0)
    ProgressBar1 = ttk.Floodgauge(window, bootstyle="danger", mask='{} %', variable=current_progress)
    ProgressBar1.pack(fill=X, padx=5, pady=5)
    Button1 = ttk.Button(window, text='Start', bootstyle='danger-outline', command=lambda: on_start())
    Button1.pack(side=LEFT, fill=X, padx=5, expand=True)
    Button2 = ttk.Button(window, text='Open', bootstyle='secondary-outline', command=lambda: on_open())
    Button2.pack(side=RIGHT, fill=X, padx=5, expand=True)


if __name__ == "__main__":
    app = ttk.Window()
    app.geometry('400x200')
    app.resizable(True, True)
    app.eval('tk::PlaceWindow . center')
    app.title('YouTube DownLoader')
    app.style.theme_use('darkly')
    # app.iconbitmap('mainicon.ico')
    #app.iconphoto(True, ttk.PhotoImage(file=os.path.dirname(__file__)+'/mainicon.png'))
    setup_ui(window=app)
    # app.protocol("WM_DELETE_WINDOW", on_app_closing)
    app.mainloop()


