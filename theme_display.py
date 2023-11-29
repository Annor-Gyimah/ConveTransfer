import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys, os
from ttkbootstrap import Style
import subprocess
import json
from resourcepath import resource_path, resource_path2
def checker(self):
    if self.var.get() == 0:
        themename = 'darkly'
        # Apply the new theme to the style
        self.style_window.theme_use(themename)
        self.table.tag_configure('evenrow', background='#05060a')#A36D8C
        self.table.tag_configure('oddrow', background='#171a2b')#6D73A3
        print('changed to darkly')
        
        
    else:
        themename = DEFAULT_THEME

        # Apply the new theme to the style
        self.style_window.theme_use(themename)
        self.table.tag_configure('evenrow', background='#F8F8F8')
        self.table.tag_configure('oddrow', background='#FFFFFF')
        print('changed to whitely')


# def checker(self):
#     if self.var.get() == 0:
#         themename = 'darkly'
#          # Apply the new theme to the style
#         self.style_window.theme_use(themename)
#         self.table.tag_configure('evenrow', background='#05060a')#A36D8C
#         self.table.tag_configure('oddrow', background='#171a2b')#6D73A3
#         print('changed to darkly')
#         with open('thema.txt', 'w') as w:
#             pass
#         self.them = resource_path2(relative_path='thema.txt')
#         with open(self.them, 'w') as df:
#             df.write('darktheme')
#         df.close()
#         python_executable = sys.executable
#         script_path = os.path.abspath(sys.argv[0])

#         # Close the current instance
#         self.destroy()

#         # Start a new instance of the application
#         subprocess.Popen([python_executable, script_path])
#         sys.exit(0)
        
                
#     else:
        
#         themename = DEFAULT_THEME
#         # Apply the new theme to the style
#         self.style_window.theme_use(themename)
#         self.table.tag_configure('evenrow', background='#F8F8F8')
#         self.table.tag_configure('oddrow', background='#FFFFFF')
#         self.them = resource_path2(relative_path='thema.txt')
#         with open(self.them, 'w') as df:
#             df.write('light')
#         df.close()

    

    
    
    
    