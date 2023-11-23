import ttkbootstrap as ttk
from ttkbootstrap.constants import *
def checker(self):
    if self.var.get() == 0:
        themename = 'darkly'
        # Apply the new theme to the style
        self.style_window.theme_use(themename)
        self.table.tag_configure('evenrow', background='#05060a')#A36D8C
        self.table.tag_configure('oddrow', background='#171a2b')#6D73A3
        
    else:
        themename = DEFAULT_THEME

        # Apply the new theme to the style
        self.style_window.theme_use(themename)
        self.table.tag_configure('evenrow', background='#F8F8F8')
        self.table.tag_configure('oddrow', background='#FFFFFF')