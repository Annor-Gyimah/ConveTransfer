import tkinter as tk
from resourcepath import resource_path
import ttkbootstrap as ttk
class ProgressWindow(tk.Toplevel):
    def __init__(self, parent, total_size):
        super().__init__(parent)
        self.geometry("300x50")
        self.title("Progress")
        self.resizable(False,False)
        # App Icon
        self.iconpath = resource_path(relative_path='images/unt.ico')
        self.iconbitmap(self.iconpath)
        
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate', maximum=total_size,bootstyle='success-striped')
        self.progress_bar.pack()
        
        


        self.protocol("WM_DELETE_WINDOW", lambda: None)  # Prevent closing the progress window
       