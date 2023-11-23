# import tkinter as tk
# import requests
# import threading

# class DownloadApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Download App")

#         self.url_label = tk.Label(root, text="Enter URL:")
#         self.url_label.pack()
#         self.url_entry = tk.Entry(root)
#         self.url_entry.pack()

#         self.start_button = tk.Button(root, text="Start Download", command=self.start_download)
#         self.start_button.pack()

#         self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_download)
#         self.pause_button.pack()

#         self.resume_button = tk.Button(root, text="Resume", state=tk.DISABLED, command=self.resume_download)
#         self.resume_button.pack()

#         self.progress_label = tk.Label(root, text="")
#         self.progress_label.pack()

#         self.file_size = 0
#         self.bytes_downloaded = 0
#         self.paused = False
#         self.download_thread = None

#     def start_download(self):
#         self.url = self.url_entry.get()
#         self.file_name = self.url.split("/")[-1]
#         self.file_size = int(requests.head(self.url).headers.get('content-length', 0))
#         self.bytes_downloaded = 0
#         self.paused = False

#         self.start_button.config(state=tk.DISABLED)
#         self.pause_button.config(state=tk.NORMAL)
#         self.resume_button.config(state=tk.DISABLED)

#         self.download_thread = threading.Thread(target=self.download)
#         self.download_thread.start()

#     def download(self):
#         with requests.get(self.url, stream=True) as response:
#             with open(self.file_name, 'wb') as file:
#                 for chunk in response.iter_content(chunk_size=1024):
#                     if self.paused:
#                         break
#                     if chunk:
#                         file.write(chunk)
#                         self.bytes_downloaded += len(chunk)
#                         self.update_progress()

#         if self.paused:
#             self.progress_label.config(text="Download paused.")
#         else:
#             self.progress_label.config(text="Download completed.")
#             self.start_button.config(state=tk.NORMAL)
#             self.pause_button.config(state=tk.DISABLED)
#             self.resume_button.config(state=tk.DISABLED)

#     def pause_download(self):
#         self.paused = True
#         self.start_button.config(state=tk.NORMAL)
#         self.pause_button.config(state=tk.DISABLED)
#         self.resume_button.config(state=tk.NORMAL)

#     def resume_download(self):
#         self.paused = False
#         self.start_button.config(state=tk.DISABLED)
#         self.pause_button.config(state=tk.NORMAL)
#         self.resume_button.config(state=tk.DISABLED)
#         self.download_thread = threading.Thread(target=self.download)
#         self.download_thread.start()

#     def update_progress(self):
#         percent = (self.bytes_downloaded / self.file_size) * 100
#         self.progress_label.config(text=f"Downloaded: {percent:.2f}%")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DownloadApp(root)
#     root.mainloop()


# import tkinter as tk
# import requests
# import threading

# class DownloadApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Download App")

#         self.url_label = tk.Label(root, text="Enter URL:")
#         self.url_label.pack()
#         self.url_entry = tk.Entry(root)
#         self.url_entry.pack()

#         self.start_button = tk.Button(root, text="Start Download", command=self.start_download)
#         self.start_button.pack()

#         self.progress_labels = []

#     def start_download(self):
#         url = self.url_entry.get()
#         self.add_progress_label(url)

#         download_thread = threading.Thread(target=self.download_file, args=(url,))
#         download_thread.start()

#     def download_file(self, url):
#         file_name = url.split("/")[-1]

#         response = requests.get(url, stream=True)
#         file_size = int(response.headers.get('content-length', 0))

#         with open(file_name, 'wb') as file:
#             bytes_downloaded = 0
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     file.write(chunk)
#                     bytes_downloaded += len(chunk)
#                     self.update_progress(url, bytes_downloaded, file_size)

#         self.update_progress(url, file_size, file_size)
#         self.remove_progress_label(url)

#     def add_progress_label(self, url):
#         progress_label = tk.Label(self.root, text=f"Downloading {url}")
#         progress_label.pack()
#         self.progress_labels.append((url, progress_label))

#     def update_progress(self, url, bytes_downloaded, file_size):
#         for i, (url_label, progress_label) in enumerate(self.progress_labels):
#             if url_label == url:
#                 percent = (bytes_downloaded / file_size) * 100
#                 progress_label.config(text=f"{url}: {percent:.2f}%")

#     def remove_progress_label(self, url):
#         for i, (url_label, progress_label) in enumerate(self.progress_labels):
#             if url_label == url:
#                 progress_label.destroy()
#                 self.progress_labels.pop(i)
#                 break

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DownloadApp(root)
#     root.mainloop()




# import tkinter as tk
# import requests
# import threading

# class DownloadApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Download App")

#         self.url_label = tk.Label(root, text="Enter URL:")
#         self.url_label.pack()
#         self.url_entry = tk.Entry(root)
#         self.url_entry.pack()

#         self.start_button = tk.Button(root, text="Start Download", command=self.start_download)
#         self.start_button.pack()

#         self.pause_button = tk.Button(root, text="Pause All", state=tk.DISABLED, command=self.pause_all_downloads)
#         self.pause_button.pack()

#         self.resume_button = tk.Button(root, text="Resume All", state=tk.DISABLED, command=self.resume_all_downloads)
#         self.resume_button.pack()

#         self.progress_labels = []
#         self.download_threads = []
#         self.paused_downloads = []

#     def start_download(self):
#         url = self.url_entry.get()
#         self.add_progress_label(url)

#         download_thread = threading.Thread(target=self.download_file, args=(url,))
#         self.download_threads.append(download_thread)
#         download_thread.start()

#     def download_file(self, url):
#         file_name = url.split("/")[-1]

#         response = requests.get(url, stream=True)
#         file_size = int(response.headers.get('content-length', 0))

#         with open(file_name, 'wb') as file:
#             bytes_downloaded = 0
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     while url in self.paused_downloads:
#                         pass  # Pause the download (wait until resumed)
                    
#                     if url not in self.progress_labels:
#                         break  # Cancel the download if removed from the list
                    
#                     file.write(chunk)
#                     bytes_downloaded += len(chunk)
#                     self.update_progress(url, bytes_downloaded, file_size)

#         self.update_progress(url, file_size, file_size)
#         self.remove_progress_label(url)
#         self.download_threads.remove(threading.current_thread())

#     def add_progress_label(self, url):
#         progress_label = tk.Label(self.root, text=f"Downloading {url}")
#         progress_label.pack()
#         self.progress_labels.append(url)

#     def update_progress(self, url, bytes_downloaded, file_size):
#         for i, progress_label_url in enumerate(self.progress_labels):
#             if progress_label_url == url:
#                 percent = (bytes_downloaded / file_size) * 100
#                 self.progress_labels[i] = f"{url}: {percent:.2f}%"

#     def remove_progress_label(self, url):
#         for i, progress_label_url in enumerate(self.progress_labels):
#             if progress_label_url == url:
#                 progress_label = self.progress_labels.pop(i)
#                 progress_label.destroy()
#                 break

#     def pause_all_downloads(self):
#         for thread in self.download_threads:
#             self.paused_downloads.extend(threading.enumerate())
#             thread.join()

#         self.download_threads = []
#         self.start_button.config(state=tk.NORMAL)
#         self.pause_button.config(state=tk.DISABLED)
#         self.resume_button.config(state=tk.NORMAL)

#     def resume_all_downloads(self):
#         self.start_button.config(state=tk.DISABLED)
#         self.pause_button.config(state=tk.NORMAL)
#         self.resume_button.config(state=tk.DISABLED)
#         for url in self.progress_labels:
#             download_thread = threading.Thread(target=self.download_file, args=(url,))
#             self.download_threads.append(download_thread)
#             download_thread.start()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DownloadApp(root)
#     root.mainloop()



# import tkinter as tk
# import requests
# import threading
# import os

# class DownloadApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Download App")

#         self.url_label = tk.Label(root, text="Enter URL:")
#         self.url_label.pack()
#         self.url_entry = tk.Entry(root)
#         self.url_entry.pack()

#         self.start_button = tk.Button(root, text="Start Download", command=self.start_download)
#         self.start_button.pack()

#         self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_download)
#         self.pause_button.pack()

#         self.resume_button = tk.Button(root, text="Resume", state=tk.NORMAL, command=self.resume_download)
#         self.resume_button.pack()

#         self.progress_labels = {}
#         self.download_threads = {}
#         self.paused_downloads = set()

#         self.load_download_state()  # Load download state when the app starts

#     def start_download(self):
#         url = self.url_entry.get()
#         progress_label = self.add_progress_label(url)

#         download_thread = threading.Thread(target=self.download_file, args=(url, progress_label))
#         self.download_threads[url] = download_thread
#         download_thread.start()

#     def download_file(self, url, progress_label):
#         file_name = url.split("/")[-1]

#         response = requests.get(url, stream=True)
#         file_size = int(response.headers.get('content-length', 0))

#         with open(file_name, 'wb') as file:
#             bytes_downloaded = 0
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     while url in self.paused_downloads:
#                         pass  # Pause the download (wait until resumed)

#                     file.write(chunk)
#                     bytes_downloaded += len(chunk)
#                     self.update_progress(progress_label, bytes_downloaded, file_size)

#         self.update_progress(progress_label, file_size, file_size)
#         self.remove_progress_label(url)

#     def add_progress_label(self, url):
#         progress_label = tk.Label(self.root, text=f"Downloading {url}")
#         progress_label.pack()
#         self.progress_labels[url] = progress_label
#         self.pause_button.config(state=tk.NORMAL)
#         self.start_button.config(state=tk.DISABLED)
#         return progress_label

#     def update_progress(self, progress_label, bytes_downloaded, file_size):
#         percent = (bytes_downloaded / file_size) * 100
#         self.root.after(100, lambda: progress_label.config(text=f"{progress_label['text']}: {percent:.2f}%"))

#     def remove_progress_label(self, url):
#         if url in self.progress_labels:
#             progress_label = self.progress_labels.pop(url)
#             progress_label.destroy()
#         if url in self.download_threads:
#             self.download_threads.pop(url)

#     def pause_download(self):
#         url = self.url_entry.get()
#         if url in self.download_threads:
#             download_thread = self.download_threads[url]
#             self.paused_downloads.add(url)
#             self.pause_button.config(state=tk.DISABLED)
#             self.resume_button.config(state=tk.NORMAL)
#             download_thread.join()
#             self.save_download_state()  # Save download state when pausing

#     def resume_download(self):
#         url = self.url_entry.get()
#         if url in self.download_threads:
#             self.paused_downloads.remove(url)
#             self.resume_button.config(state=tk.DISABLED)
#             self.pause_button.config(state=tk.NORMAL)
#             download_thread = threading.Thread(target=self.download_file, args=(url, self.progress_labels[url]))
#             self.download_threads[url] = download_thread
#             download_thread.start()

#     def save_download_state(self):
#         with open("download_state.txt", "w") as state_file:
#             for url in self.paused_downloads:
#                 state_file.write(f"PAUSED:{url}\n")

#     def load_download_state(self):
#         if os.path.exists("download_state.txt"):
#             with open("download_state.txt", "r") as state_file:
#                 lines = state_file.readlines()
#                 for line in lines:
#                     parts = line.strip().split(":")
#                     if len(parts) == 2 and parts[0] == "PAUSED":
#                         paused_url = parts[1]
#                         self.paused_downloads.add(paused_url)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DownloadApp(root)
#     root.mainloop()


# import tkinter as tk
# import socket

# HOST = '127.0.0.1'
# PORT = 12345

# def receive_files():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((HOST, PORT))
#         server_socket.listen()
#         status_label.config(text=f"Listening on {HOST}:{PORT}")
#         conn, addr = server_socket.accept()
#         with conn:
#             status_label.config(text=f"Connected by {addr}")
#             while True:
#                 file_info = conn.recv(1024).decode()
#                 if not file_info:
#                     break
#                 filename, filesize = file_info.split(",")
#                 filesize = int(filesize)
#                 with open(filename, "wb") as f:
#                     while filesize > 0:
#                         data = conn.recv(1024)
#                         f.write(data)
#                         filesize -= len(data)
#                     status_label.config(text=f"Received {filename}")
#             status_label.config(text="File transfer completed.")

# def start_server():
#     receive_files()

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("File Receiver")

#     start_button = tk.Button(root, text="Start Server", command=start_server)
#     start_button.pack()

#     status_label = tk.Label(root, text="")
#     status_label.pack()

#     root.mainloop()
import time
import threading
import logging

import tkinter as tk # Python 3.x
import tkinter.scrolledtext as ScrolledText

class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class myGUI(tk.Frame):

    # This class defines the graphical user interface 

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()

    def build_gui(self):                    
        # Build GUI
        self.root.title('TEST')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        st = ScrolledText.ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='w', columnspan=4)

        # Create textLogger
        text_handler = TextHandler(st)

        # Logging configuration
        logging.basicConfig(filename='test.log',
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s')        

        # Add the handler to logger
        logger = logging.getLogger()        
        logger.addHandler(text_handler)

def worker():
    # Skeleton worker function, runs in separate thread (see below)   
    while True:
        # Report time / date at 2-second intervals
        time.sleep(2)
        timeStr = time.asctime()
        msg = 'Current time: ' + timeStr
        logging.info(msg) 

def main():

    root = tk.Tk()
    myGUI(root)

    t1 = threading.Thread(target=worker, args=[])
    t1.start()

    root.mainloop()
    t1.join()

main()