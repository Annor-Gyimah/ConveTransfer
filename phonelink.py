
import os
import ttkbootstrap as ttk
import tkinter as tk
import threading
import sys
import json
import types
import subprocess
from PIL import Image, ImageTk
import webbrowser

import encodings
import codecs
from ttkbootstrap.scrolled import ScrolledFrame
from resourcepath import resource_path, resource_path2
from get_ip import wifi
#import qrcode
try:
    sys.path.append("C:/Users/DELL/Desktop/socketra/Lib/site-packages/qrcode")
    import qrcode
except ModuleNotFoundError:
    import qrcode
def Phonelink(self):
    def load_translations(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                translations = json.load(json_file)
            return translations
        except FileNotFoundError:
            print("Translations file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding translations JSON file.")
            return {}
        
       
       
    self.language_config_file = 'language_config.txt'
    try:
        with open(self.language_config_file, 'r', encoding='utf-8') as config_file:
            #print(config_file.read().strip())
            
            self.current_language= config_file.read().strip()
        
            
    except FileNotFoundError:
        return 'en'
    self.translations = load_translations(resource_path2('translations.json'))

    
    def translate_notification(message_key):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(message_key, message_key)
    
    PORT = 8000

    ipadd = wifi
    def generate_qr_code():
        # Generate a QR code with the server URL
        server_url = f"http://{ipadd}:{PORT}/"  # Replace with your server's IP address
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(server_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert the PIL Image to a PhotoImage
        img = ImageTk.PhotoImage(img)

        # Create a label to display the QR code
        label.config(image=img)
        label.image = img  # Update reference to avoid garbage collection


    pc_to_phone = ScrolledFrame(self.tab5,width=1750, autohide=True)
    pc_to_phone.pack(fill='both', side='left', padx=(1, 1), pady=1)
    label = ttk.Label(pc_to_phone)
    label.pack(padx=20, pady=20)


    

    # Generate and display the initial QR code
    generate_qr_code()
    def start_server():

        

        def resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            return os.path.join(base_path, relative_path)
        
        add = resource_path(relative_path='httpserver.py')
        
        try:
            # Get the path to the Python interpreter within the packaged executable
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                python_path = os.path.join(sys._MEIPASS, "python.exe")
            else:
                python_path = sys.executable  # Use the current Python interpreter
            
            # Use subprocess to start the server in a new console window
            subprocess.Popen(["start", "cmd", "/k", python_path, f"{add}"], shell=True)
        except Exception as e:
            print(f"Error starting server: {e}")


    

    self.push_button = ttk.Button(pc_to_phone, text=translate_notification('Turn On'), command=start_server)
    self.push_button.pack(pady=10)

    

    text_frame = ttk.Frame(pc_to_phone)
    text_frame.pack()

    step1_frame = ttk.Frame(text_frame)
    step1_frame.pack(padx=10, pady=10)

    step1_image = Image.open(resource_path(relative_path='images/step1.png'))
    step1_image = step1_image.resize((60,30))
    step1_image = ImageTk.PhotoImage(step1_image)
    self.step1_image = step1_image
    ttk.Label(step1_frame, image=step1_image).pack(side='left', padx=(4,30))
    self.step1_label = ttk.Label(step1_frame, text=translate_notification("Connect both phone and pc to the same network."))
    self.step1_label.pack(pady=5)

    

    
    step2_frame = ttk.Frame(text_frame)
    step2_frame.pack(padx=10, pady=10)
    step2_image = Image.open(resource_path(relative_path='images/step2.png'))
    step2_image = step2_image.resize((60,30))
    step2_image = ImageTk.PhotoImage(step2_image)
    self.step2_image = step2_image
    ttk.Label(step2_frame, image=step2_image).pack(side='left', padx=(4,30))
    self.step2_label = ttk.Label(step2_frame, text=translate_notification("Click on the 'Turn On' to start sharing."))
    self.step2_label.pack(pady=5)
    


    step3_frame = ttk.Frame(text_frame)
    step3_frame.pack(padx=10, pady=10)
    step3_image = Image.open(resource_path(relative_path='images/step3.png'))
    step3_image = step3_image.resize((60,30))
    step3_image = ImageTk.PhotoImage(step3_image)
    self.step3_image = step3_image
    ttk.Label(step3_frame, image=step3_image).pack(side='left', padx=(4,30))
    self.step3_label = ttk.Label(step3_frame, text=translate_notification("Open up your phone's camera or your qrcode scanner to scan the qrcode."))
    self.step3_label.pack(pady=5)

    step4_frame = ttk.Frame(text_frame)
    step4_frame.pack(padx=10, pady=10)
    step4_image = Image.open(resource_path(relative_path='images/step4.png'))
    step4_image = step4_image.resize((60,30))
    step4_image = ImageTk.PhotoImage(step4_image)
    self.step4_image = step4_image
    ttk.Label(step4_frame, image=step4_image).pack(side='left', padx=(4,30))
    
    
    self.step4_label = ttk.Label(step4_frame, text=translate_notification("A link will be generated on your phone via the qrcode scanner."))
    self.step4_label.pack(pady=5)
    self.ss1 = ttk.Label(step4_frame,text=translate_notification("Click on it to go to your browser."))
    self.ss1.pack()

    ipadd = wifi
    if ipadd == "":
        ipadd = '127.0.0.1'
    else:
        ipadd = wifi
    self.server_url = f"http://{ipadd}:{PORT}/"
    def call_link(event):
        webbrowser.open_new_tab(self.server_url)
    # oo1 = translate_notification("Or Alternatively, open your web browser on your phone.")
    # oo2 = translate_notification("Then you type in this address")
    self.other_steps_label = ttk.Label(text_frame, text=translate_notification(f"Or Alternatively, open your web browser on your phone."))
    self.other_steps_label.pack(pady=5)
    self.oo2 = ttk.Label(text_frame, text=translate_notification(f"Then you type in this address"))
    self.oo2.pack()
    self.urll = ttk.Label(text_frame, text=f'{self.server_url}', cursor='hand2', foreground='green')
    self.urll.pack()
    self.urll.bind('<Button-1>', call_link)
    

    step5_frame = ttk.Frame(text_frame)
    step5_frame.pack(padx=10, pady=10)
    step5_image = Image.open(resource_path(relative_path='images/step5.png'))
    step5_image = step5_image.resize((60,30))
    step5_image = ImageTk.PhotoImage(step5_image)
    self.step5_image = step5_image
    ttk.Label(step5_frame, image=step5_image).pack(side='left', padx=(4,30))
    self.step5_label = ttk.Label(step5_frame, text=translate_notification("Choose a file to upload"))
    self.step5_label.pack(pady=5)

    step6_frame = ttk.Frame(text_frame)
    step6_frame.pack(padx=10, pady=10)
    step6_image = Image.open(resource_path(relative_path='images/step6.png'))
    step6_image = step6_image.resize((60,30))
    step6_image = ImageTk.PhotoImage(step6_image)
    self.step6_image = step6_image
    ttk.Label(step6_frame, image=step6_image).pack(side='left', padx=(4,30))
    self.step6_label = ttk.Label(step6_frame, text=translate_notification("Select a destination"))
    self.step6_label.pack(pady=5)

    step7_frame = ttk.Frame(text_frame)
    step7_frame.pack(padx=10, pady=10)
    step7_image = Image.open(resource_path(relative_path='images/step7.png'))
    step7_image = step7_image.resize((60,30))
    step7_image = ImageTk.PhotoImage(step7_image)
    self.step7_image = step7_image
    ttk.Label(step7_frame, image=step7_image).pack(side='left', padx=(4,30))
    self.step7_label = ttk.Label(step7_frame, text=translate_notification("Click on Upload."))
    self.step7_label.pack(pady=5)















