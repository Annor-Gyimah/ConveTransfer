import tkinter as tk
from tkinter import scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText
from resourcepath import resource_path, resource_path2
import json
from metadata import __AppName__
from metadata import __version__

class ChangelogWindow(ttk.Toplevel):
    def __init__(self, parent):
        ttk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 695
        h = 398
        
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.title('ChangeLogs')
        self.icon = resource_path('images/unt.ico')
        self.iconbitmap(self.icon)
        #self.bind("<Configure>", self.on_resize)

        changelog_text = f"""
        Version {__version__}:
        New GUI created with the beautiful ttkbootstrap framework, featuring:

        - Sending one file at a time using the main 'Send' button.
        - Drag-and-drop functionality for easy file selection (one file at a time).
        - Support for saved profiles of senders and receivers, streamlining file transfer 
            without the need to type the receiver's IP address each time.
        - Capability to receive files from a sender with remarkable speed.
        - Inclusion of a progress bar to visualize the file transfer progress.
        - Ability to link your phone and PC effortlessly by scanning the QR code.
        - Simple process for downloading YouTube videos with just a few clicks.
        - Support for both light and dark modes.
        - Multilingual support for a user-friendly experience.

        """
        
        self.sc = ttk.Text(self,bg="#f8f8f8",wrap='word',spacing1=2)
        self.sc.insert(ttk.END, changelog_text)
        self.sc.config(state=ttk.DISABLED)

        # # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, bootstyle='danger',  command=self.sc.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sc.config(yscrollcommand=scrollbar.set)
        self.sc.pack(expand=True, fill=ttk.BOTH)
        
        # tree_scroll = ttk.Scrollbar(self, orient="vertical", command=self.sc.yview)
        # self.sc.configure(yscrollcommand=tree_scroll.set)
        # tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        

        # self.sc = ScrolledText(self,autohide=True, bootstyle='danger', wrap='word',spacing1=2)
        # self.sc.insert(ttk.END, changelog_text)
        # #self.sc.config(state=ttk.DISABLED)
        # self.sc.pack(expand=True, fill=ttk.BOTH)
    # def on_resize(self,event):
    #     width = self.winfo_width()
    #     height = self.winfo_height()
    #     print(f"Window size for how to is {width} x {height}")



        