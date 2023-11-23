import tkinter as tk
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.tooltip import ToolTip
from PIL import Image,ImageTk,ImageOps, ImageDraw
import webbrowser
import psutil as ps
import threading
import datetime
from tkinter import filedialog, messagebox, simpledialog
import socket
import time
import connection
from ttkbootstrap import Style
from tkinter import simpledialog
import requests
from updatemanager import UpdateManager
from resourcepath import resource_path, resource_path2
from receiveloc import receive_loc
import get_ip
from progresswin import ProgressWindow
from about import DisplayAboutMe
from how_to import DisplayHowTo
import json
from tkinter import font
from functools import cache
from ttkbootstrap.dialogs import Messagebox
import sys
from tkinterdnd2 import TkinterDnD, DND_ALL
sys.path.append("C:/Users/DELL/Desktop/socketra/Lib/site-packages/tkinterdnd2")
from ttkbootstrap.scrolled import ScrolledFrame
from wifi_name import get_wifi_ssid
import encodings
import codecs
#from get_drive import update_drive_info_and_progress_bars
from youtube3 import youtube_tab
from phonelink import Phonelink
# from pro import load_configuration,save_configuration,load_profile_image,create_circular_mask,update_profile_image,change_user_name


from http.server import SimpleHTTPRequestHandler
import socketserver
import urllib

import html
import shutil
import cgi

from PIL import Image, ImageTk

from get_ip import wifi
try:
    sys.path.append("C:/Users/DELL/Desktop/socketra/Lib/site-packages/qrcode")

    import qrcode
    
except ModuleNotFoundError:
    import qrcode
