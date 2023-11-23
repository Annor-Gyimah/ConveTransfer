import tkinter as tk
from PIL import Image, ImageOps, ImageTk
from tkinter import font
import ttkbootstrap as ttk
import webbrowser
from resourcepath import resource_path, resource_path2

from metadata import __version__ 
from metadata import __AppName__

class DisplayAboutMe(ttk.Toplevel):
    def __init__(self, parent):
        ttk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 480
        h = 450
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('About')
        self.about_ico = resource_path(relative_path='images/unt.ico')
        self.wm_iconbitmap(self.about_ico)

        # Load and resize the image
        self.image = Image.open(resource_path2(relative_path='images/Anno.png'))
        self.size = (150, 150)  # Adjust the size as needed
        self.thumb = ImageOps.fit(self.image, self.size)
        self.photo = ImageTk.PhotoImage(self.thumb)

        # Center the image
        logo_frame = tk.Frame(self)
        logo_frame.pack(side=tk.TOP, pady=30)
        logo_label = tk.Label(logo_frame, image=self.photo)
        logo_label.pack()

        f1 = tk.Frame(self)
        f1.pack()
        f2 = tk.Frame(self)
        f2.pack(pady=10)
        f3 = tk.Frame(f2)
        f3.pack()

        def call_link(*args):
            webbrowser.open_new_tab('https://www.youtube.com/c/mechanizecode')

        tk.Label(f1, text=__AppName__ + ' ' + str(__version__)).pack()
        tk.Label(f1, text='Copyright (C) 2023 Annorion').pack()
        tk.Label(f1, text='All rights reserved').pack()

        f = font.Font(size=10, slant='italic', underline=True)
        label1 = tk.Label(f3, text='Annorion', font=f, cursor='hand2')
        label1['foreground'] = 'blue'
        label1.pack(side=tk.LEFT)
        label1.bind('<Button-1>', call_link)
        label2 = tk.Label(self, text="Imagine and Build", font=f)
        label2.pack()
        ttk.Button(self, text='OK', command=self.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = DisplayAboutMe(root)
    root.mainloop()
