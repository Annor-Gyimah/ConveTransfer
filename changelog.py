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
        w = 785
        h = 520
        
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.title('ChangeLogs')
        #self.icon = resource_path('images/unt.ico')
        self.iconbitmap(default='images/unt.ico')

        changelog_text = f"""
        Version {__version__}:
        - New GUI made with beautiful ttkbootstrap
        - Sending a file at a time with the major 'Send' button.
        - Supports drag and drop system to make things easier (A file at a time)
        - Support saved profiles of senders and receivers making it easier to send a file 
            without typing in the IP of the receiver in the IP field.
        - Ability to receive a file from a sender with ease at an amazing speed.
        - A progress bar to show the progress of the file transfer.
        - Ability to link your phone and PC together by just scanning the QRCode.
        - An easy way to download your Youtube videos with just some clicks.
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



        