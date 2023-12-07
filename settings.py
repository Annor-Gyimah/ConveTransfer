import tkinter as tk
from tkinter import font
from PIL import Image, ImageOps, ImageTk
import ttkbootstrap as ttk
import webbrowser
from resourcepath import resource_path, resource_path2
import os
from ttkbootstrap.constants import *
from tkinter import *
import json
class SomeSettings(ttk.Toplevel):
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
        
        self.about_ico = resource_path(relative_path='images/unt.ico')
        self.wm_iconbitmap(self.about_ico)

        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # icon_path = os.path.join(script_dir, 'images', 'unt.ico')

        # self.about_ico = icon_path
        # self.wm_iconbitmap(self.about_ico)
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
        def translate_notification(text):
            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found
            return translation_dict.get(text, text)
        
        self.title(translate_notification('Settings'))
        self.startup_text = translate_notification("Startup Settings")
        self.startup = ttk.Labelframe(self, text=self.startup_text, padding=29)
        self.startup.pack(fill=BOTH, anchor=N, padx=(25,25))
        # type_lbl = ttk.Label(self.startup, text="Unchecked", width=8)
        # type_lbl.pack(side=LEFT, padx=(15, 0), anchor=N)
        # Read initial state from the configuration file
        self.config_file = "config.json"
        try:
            with open(self.config_file, "r") as config_file:
                data = json.load(config_file)
            initial_state = data.get("Tips", "OFF")
        except FileNotFoundError:
            initial_state = "OFF"

        self.type_var = IntVar()
        self.yesnotick = ttk.Checkbutton(
            master=self.startup,
            text=translate_notification('Show tips'),
            variable=self.type_var,
            onvalue=1,
            offvalue=0,
            command=self.tips_on_off
        )
        self.yesnotick.pack(side=LEFT)

        # Set the initial state of the checkbox
        self.type_var.set(1 if initial_state == "ON" else 0)
    
    def save_configuration(self):
        try:
            # Read existing data
            with open(self.config_file, "r") as config_file:
                data = json.load(config_file)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty data dictionary
            data = {}

        # Update the data with the new information
        data["Tips"] = "ON" if self.type_var.get() == 1 else "OFF"

        # Write the updated data back to the file
        with open(self.config_file, "w") as config_file:
            json.dump(data, config_file)

    def tips_on_off(self):
        self.save_configuration()
        



    
if __name__ == "__main__":
    root = tk.Tk()
    app = SomeSettings(root)
    root.mainloop()