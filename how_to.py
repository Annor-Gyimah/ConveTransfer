import tkinter as tk
import ttkbootstrap as ttk
from tkinter import font
import json


from resourcepath import resource_path, resource_path2

class DisplayHowTo(ttk.Toplevel):
    def __init__(self,parent):
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
        self.icon = resource_path('images/unt.ico')
        self.iconbitmap(self.icon)

       
        # self.minsize(width=w,height=h)
        # self.maxsize(width=w,height=h)
        #self.geometry('970x420')

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

        
        
        
        self.title(translate_notification('How To'))

        f = font.Font(size=10, slant='italic', underline=True)
        self.head = ttk.Label(self, text=translate_notification('How To Send and Receive Files'),font=f)
        self.head.pack()
        text_frame = ttk.Frame(self)
        text_frame.pack()
        f1 = font.Font(size=10, slant='italic')
        text1 = translate_notification("This is no rocket science it is as simple as it can get")
        ttk.Label(text_frame,text=text1, font=f1).pack()
        # text2 = "1. Create a network"
        # ff = font.Font(size=10, underline=True, weight='bold')
        # ttk.Label(text_frame,text=text2,font=ff).pack(side=ttk.LEFT,padx=(151,5),pady=(35,3))
        # text3 = "Going easy is simple right. Why don't you use your create a hotspot with your phone.\n And Oh, you don't need to turn on your data."
        # ttk.Label(text_frame, text=text3, font=f1).pack(side=ttk.LEFT,padx=3,pady=(35,3))


        #f2 = font.Font(size=10, slant='italic',weight='bold')
        self.note = ttk.Notebook(text_frame, bootstyle='info')

        self.tab = ttk.Frame(self.note)
        sending = ttk.Text(self.tab,bg="#f8f8f8",wrap='word',spacing1=2)
        create_network = translate_notification('1. Create a Network')
        some_text = f"{create_network}\n"
        first_step = translate_notification("To do this, you can turn On your mobile phone's or laptop's hotspot. But for convenience sake, use a mobile phone hotspot. Creating the network can be done by either the one sending or  the one receiving. The idea is that they must be on the same network.")
        some_text2 = f"{first_step}\n"
        ip_address = translate_notification("2. IP Address & Port Number")
        some_text3 = f"{ip_address}\n"
        second_step = translate_notification("Now in order to send the file, you need the receiver's IP Address. As the one sending, type in the receiver's address in the IP field. This IP address is the second ip address on receiver's end. This IP Address will be displayed when the receiver click on the arrow signs on the IP field. Now concerning the PORT, you can use the arrow sign on the Port field to select port 4444 or type in the Port field 4444.")
        some_text4 = f"{second_step}\n"
        selecting_sending = translate_notification('3. Selecting and Sending')
        some_text5 = f"{selecting_sending}\n"
        third_step = translate_notification("Now before selecting and sending do make sure that the same IP and Port number is what the receiver is using else it won't work. As the one sending, do not concern yourself with the 'Receive Folder' or the 'Receive Path'. Now click on the 'Send' button to select a file and send it.")
        some_text6 = f"{third_step}"
        sending.pack()
        sending.insert("1.0", some_text, ("bold",))
        sending.insert(tk.END,some_text2)
        sending.tag_configure("bold",font=("Helvetica",9,"bold"),underline=True)
        sending.insert(tk.END,some_text3,("bold"))
        sending.insert(tk.END, some_text4)
        sending.insert(tk.END, some_text5, ("bold"))
        sending.insert(tk.END, some_text6)

        sending.config(state='disabled')


        self.tab1 = ttk.Frame(self.note)
        receiving = ttk.Text(self.tab1,bg="#f8f8f8",wrap='word',spacing1=2)
        create_network = translate_notification('1. Create a Network')
        some_text_r = f"{create_network}\n"
        first_step = translate_notification("To do this, you can turn On your mobile phone's or laptop's hotspot. But for convenience sake, use a mobile phone hotspot. Creating the network can be done by either the one sending or  the one receiving. The idea is that they must be on the same network.")
        some_text2_r = f"{first_step}\n"
        ip_address_port = translate_notification("2. IP Address, Port Number & Receive Dir")
        some_text3_r = f"{ip_address_port}\n"
        second_step = translate_notification("Now in order to receive the file, you need your own IP Address. And you can get it by clicking on the arrow signs in the IP field. If it is not displaying, make sure you PC is connected to the network close the application and open it up again. Concerning the PORT, you can use the arrow sign on the Port field to select port 4444  or type in 4444. Also, the receiver has to select a 'Receive Path' and enter a folder's name at the 'Receive Folder'. And this is going to be where the receiver wants to receive the file. The 'Receive Path' can only be Desktop, Document, Pictures, Videos, Music and Downloads. If  the 'Receive Path' is not selected and the 'Receive Folder' field is empty, it won't work. But if the 'Receive Path' is selected and the 'Receive Folder' is empty, the receiver will receive the file at the selected 'Receive Path'.")
        some_text4_r = f"{second_step}\n"
        receivings = translate_notification("3. Receiving") 
        some_text5_r = f"{receivings}\n"
        some_text6_r = translate_notification("Now before receiving the file, make sure the one sending the file has correctly typed your IP address at the end of his or her IP field and you both are using the same port number. Once the Sender selects and the file and is about to send, the receiver can now click on receive to receive the file. For the first time, firewall on windows will prompt you with a pop-up asking you to tick the private network on the pop-up. Please tick it and make sure the public network is ticked too. If not, you will be able to send files but you wont be able to receive files. There is one way to fix it if you missed the chance. Contact the developer on how to do this on 'eannor707@gmail.com'")
        receiving.pack()
        receiving.insert("1.0", some_text_r, ("bold",))
        receiving.insert(tk.END,some_text2_r)
        receiving.tag_configure("bold",font=("Helvetica",9,"bold"),underline=True)
        receiving.insert(tk.END,some_text3_r,("bold"))
        receiving.insert(tk.END, some_text4_r)
        receiving.insert(tk.END, some_text5_r, ("bold"))
        receiving.insert(tk.END, some_text6_r)
        receiving.config(state='disabled')



    
        self.note.add(self.tab,text='Send')
        self.note.add(self.tab1,text='Receive')
        self.note.pack(fill=tk.BOTH, expand=1)
        
    

