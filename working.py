
from packages import *

connection.Database()
import json

from metadata import __version__ 
from metadata import __AppName__

Image.CUBIC = Image.BICUBIC

class Root(ttk.Window):
    def __init__(self):
        super().__init__()

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

        self.translations = load_translations(resource_path2('translations.json'))
        # Add more translations for other languages as needed

       
         # Load saved language configuration if available
        self.language_config_file = 'language_config.txt'  
        self.current_language = self.load_language_config()
        

        def setup_tooltips():
            select_button_tooltip_text = translate_notification('Click to select and send a file')
            ToolTip(self.select_button, text=select_button_tooltip_text, bootstyle=INVERSE)
            receive_button_tooltip_text = translate_notification('Click to receive a file')
            ToolTip(self.receive_button, text=receive_button_tooltip_text, bootstyle=INVERSE)
            stop_button_tooltip_text = translate_notification('Click to stop a file in transmission"')
            ToolTip(self.stop_button, text=stop_button_tooltip_text, bootstyle=INVERSE)
            update_button_tooltip_text = translate_notification('Update for new features and bug fixes')
            ToolTip(self.update_button, text=update_button_tooltip_text, bootstyle=INVERSE)
            #help = translate_notification('Help')


        
        
    
        def update_ui():
            

            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
                
                
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found
           
            # Update UI elements with translated text
            root.labelid.config(text=translation_dict.get('IP', ''))
            root.menubar.entryconfig(0, label=translation_dict.get('File', ''))
            root.menubar.entryconfig(1, label= translation_dict.get('Help',''))
            root.filemenu.entryconfig(0, label=translation_dict.get('Exit', ''))
            root.helpmenu.entryconfig(0, label=translation_dict.get('About', ''))
            root.helpmenu.entryconfig(1, label=translation_dict.get('Check for Updates', ''))
            root.helpmenu.entryconfig(2, label=translation_dict.get('How To', ''))
            root.helpmenu.entryconfig(3, label=translation_dict.get('Language', ''))
            root.labelport.config(text=translation_dict.get('Port', ''))
            root.labelloc.config(text=translation_dict.get('Receive Dir', ''))
            root.context_menu.entryconfig(0,label=translation_dict.get('Delete', ''))
            sent_received = translation_dict.get('Sent/Received','')
            root.note.add(self.tab1, text=sent_received)
            root.check.config(text=translation_dict.get('mode',''))
            root.howto_submenu.config()
            

            sent_heading = translation_dict.get('sent', '')
            date_heading = translation_dict.get('date', '')
            size_heading = translation_dict.get('size', '')
            received_heading = translation_dict.get('received', '')

            root.table.heading("sent", text=sent_heading, anchor="center")
            root.table.heading("date", text=date_heading, anchor="nw")
            root.table.heading("size", text=size_heading, anchor="nw")
            root.table.heading("received", text=received_heading, anchor="nw")
            
            
            setup_tooltips()
            
            
            

            
        
        def change_language(lang):
            self.current_language = lang
            print(lang)
            update_ui()
            self.save_language_config(lang)

        
        def translate_notification(text):
            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found
            return translation_dict.get(text, text)
            
         


        
 
        def about_me():
            DisplayAboutMe(self)

        def howto():
            DisplayHowTo(self)
        
        def check_updates():
            def translate_message_box(title_key, message_key):
                if self.current_language in self.translations:
                    translation_dict = self.translations[self.current_language]
                else:
                    translation_dict = self.translations['en']  # Fallback to English if the language is not found

                title = translation_dict.get(title_key)
                message = translation_dict.get(message_key)
                
                message_ico = resource_path(relative_path='images/unt.ico')
                self.iconbitmap(default=message_ico)
                return messagebox.showinfo(title, message)
                #return Messagebox.show_info(message, title, self)
            def translate_notification(message_key):
                if self.current_language in self.translations:
                    translation_dict = self.translations[self.current_language]
                else:
                    translation_dict = self.translations['en']  # Fallback to English if the language is not found
                return translation_dict.get(message_key, message_key)
       
            try:
                # -- Online Version File
                # -- Replace the url for your file online with the one below.
                response = requests.get(
                    'http://localhost/suplike/socketra/updates/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    translate_message_box('Software Update', 'Update Available !')
                    UPDATE = translate_notification('Update!')
                    MESSAGE = translate_notification('needs to update to version')
                    mb1 = messagebox.askyesno({UPDATE}, f'{__AppName__} {__version__} {MESSAGE} {data}')
                    if mb1 is True:
                        # -- Replace the url for your file online with the one below.
                        webbrowser.open_new_tab('http://localhost/suplike/socketra/'
                    'updates/ConveTransfer.msi?raw=true')
                        self.destroy()
                    else:
                        pass
                else:
                    translate_message_box('Software Update', 'No Updates Available')
            except Exception as e:
                translate_message_box('Software Update', 'Unable to Check for Update, No internet')
            

        
        self.title(__AppName__ + ' ' + str(__version__))
        w = 1020
        h = 520
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=True, height=True)
        # self.iconpath = resource_path(relative_path='images//unt.ico')
        # #self.iconbitmap(self.iconpath)
        self.iconpath = resource_path(relative_path='images/unt.ico')
        self.wm_iconbitmap(self.iconpath)
        #self.iconpath = Image.open(resource_path('icon.png'))
        
        #self.wm_iconwindow(self.iconpath)
        
        
        
        
        
        self.menubar = ttk.Menu(self)
        self.filemenu = ttk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label=translate_notification('Exit'),command=self.destroy)
        #self.filemenu.add_command(label=translate_notification('Send Folder'),command=self.open_file_dialog)
        self.menubar.add_cascade(label=translate_notification('File'),menu=self.filemenu)

        self.helpmenu = ttk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label=translate_notification('About'),command=about_me)
        self.helpmenu.add_command(label=translate_notification('Check for Updates'), command=check_updates)
        self.helpmenu.add_command(label=translate_notification('How To'),command=howto)

        self.howto_submenu = ttk.Menu(self.helpmenu, tearoff=0)
        
        self.howto_submenu.add_radiobutton(label='English', command=lambda: change_language('en'))
        self.howto_submenu.add_radiobutton(label='Español', command=lambda: change_language('es'))
        self.howto_submenu.add_radiobutton(label='French', command=lambda: change_language('fr'))
        self.howto_submenu.add_radiobutton(label='Japanese', command=lambda: change_language('ja'))
        self.howto_submenu.add_radiobutton(label='Korean', command=lambda: change_language('ko'))
        self.howto_submenu.add_radiobutton(label='Portugese', command=lambda: change_language('pt'))
        self.howto_submenu.add_radiobutton(label='Tamil', command=lambda: change_language('ta'))
        self.howto_submenu.add_radiobutton(label='Hindi', command=lambda: change_language('hi'))
        self.howto_submenu.add_radiobutton(label='Akan', command=lambda: change_language('ak'))
          
        
        #self.helpmenu.add_command(label='How To',command=howto)
        self.helpmenu.add_cascade(label=translate_notification('Language'), menu=self.howto_submenu)
        self.menubar.add_cascade(label=translate_notification('Help'),menu=self.helpmenu)
        

        self.config(menu=self.menubar)
        

        self.button_frame = ttk.Frame(self,borderwidth=3,relief='groove')
        self.button_frame.pack(fill='x',side='top')
        

        self.s = ttk.Style()
        self.s.configure('Link.TButton',font=('Helvetica'))
        
        #self.ima = resource_path2(relative_path='images/exit.png')
        self._select = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/sent.png')))
        self.select_button = ttk.Button(self.button_frame,image=self._select,state='normal',bootstyle='Link.Tbutton',command=self.send_file)
        self.select_button.pack(side=tk.LEFT,padx=1,pady=1)
        ToolTip(self.select_button,text=translate_notification('Click to select and send a file'),bootstyle=(INVERSE))
        self.select_button.image = self._select

        self._stop = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/stop.png')))
        self.stop_button = ttk.Button(self.button_frame, state='disabled',command=self.stop_transfer,image=self._stop,bootstyle='Link.Tbutton')
        self.stop_button.pack(side=tk.LEFT,padx=1,pady=1)
        ToolTip(self.stop_button,text=translate_notification('Click to stop a file in transmission'),bootstyle=(INVERSE))
        self.stop_button.image = self._stop
        
        self._receive = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/receive.png')))
        self.receive_button = ttk.Button(self.button_frame, image=self._receive,state='normal',bootstyle='Link.Tbutton',command=self.receive_file)
        self.receive_button.pack(side=tk.LEFT,padx=1,pady=1)
        ToolTip(self.receive_button,text=translate_notification('Click to receive a file'),bootstyle=(INVERSE))
        self.receive_button.image = self._receive

        
        self._update = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/updates.png')))
        self.update_button = ttk.Button(self.button_frame,image=self._update,bootstyle='Link.Tbutton',command=self.update_using_manager)
        self.update_button.pack(side=tk.LEFT,padx=1,pady=1)
        ToolTip(self.update_button,text=translate_notification('Update for new features and bug fixes'),bootstyle=(INVERSE))
        self.update_button.image = self._update
        

               
                
            
        self.var = ttk.IntVar()
        self.check = ttk.Checkbutton(self.button_frame,variable=self.var, bootstyle="round-toggle",onvalue=0,offvalue=1, text=translate_notification("mode"),command=self.checker)
        self.check.pack(side=tk.RIGHT)
        self.style_window = Style(theme=DEFAULT_THEME)
        
        
        


        self.host = ttk.StringVar() 
        self.port = ttk.StringVar()
        self.loc = ttk.StringVar()
        self.perce = ttk.DoubleVar(value=0)

        self.entries = ttk.Frame(self,width=70)
        self.entries.pack(fill='both',side='left',padx=(1,1),pady=1)
        
        self.labelid = ttk.Label(self.entries,text=translate_notification('IP'),font=('arial',10,'bold'))
        self.labelid.pack(side=tk.TOP,padx=(2,2),pady=2)
        self.stuff = ['127.0.0.1',f'{self.wifi}']
        self.senderid = ttk.Spinbox(self.entries,values=self.stuff,textvariable=self.host)
        self.senderid.pack(side=tk.TOP,padx=(2,2),pady=2)

        
        self.labelport = ttk.Label(self.entries,text=translate_notification('Port'),font=('arial',10,'bold'))
        self.labelport.pack(side=tk.TOP,padx=(2,2),pady=(3,3))
        self.stuff1 = [4444,8080]
        self.portid = ttk.Spinbox(self.entries,values=self.stuff1,textvariable=self.port,takefocus=4444)
        self.portid.pack(fill='y',padx=2,pady=(2,2))
        
        
        self.labelloc = ttk.Label(self.entries, text=translate_notification("Receive Dir"), font=('aria',10,'bold'))
        self.labelloc.pack(side=tk.TOP,padx=(2,2),pady=2)
        self.stuff2 = [f'{self.desktop}', f'{self.documents}', f'{self.videos}', f'{self.music}', f'{self.downloads}', f'{self.pictures}']
        self.location = ttk.Spinbox(self.entries,values=self.stuff2,textvariable=self.loc)  
        self.location.pack(fill='y',padx=2,pady=(3,3))  
        

        self.t_time = ttk.Label(self.entries, text="")
        self.t_time.pack(side=tk.TOP,padx=(2,2),pady=(4,4))

        
        self.note = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self)
        self.tab2 = ttk.Frame(self)
        self.tab3 = ttk.Frame(self)

        columns = ("sent", "date", "size","received")
    
        self.table = ttk.Treeview(self.tab1, bootstyle='success', columns=columns, show="headings")
        
        self.table.heading("sent", text=translate_notification("sent"), anchor="center")
        self.table.heading("date", text=translate_notification("date"), anchor="nw")
        self.table.heading("size", text=translate_notification("size"), anchor="nw")
        self.table.heading("received", text=translate_notification("received"), anchor="nw")
        self.table.tag_configure('evenrow', background='#F8F8F8')
        self.table.tag_configure('oddrow', background='#FFFFFF')
    
        
            
        
    
        self.table.pack(fill=tk.BOTH, expand=1)
        self.note.add(self.tab1,text=translate_notification('Sent/Received'))
        self.note.add(self.tab2,text=translate_notification('Disk Space'))
        self.note.add(self.tab3,text='Youtube Downloads')
        self.note.pack(fill=tk.BOTH, expand=1)

        
        # Create a context menu
        self.context_menu = tk.Menu(self.table, tearoff=0)
        self.context_menu.add_command(label=translate_notification("Delete"), command=self.delete_selected_item)
        #self.context_menu.add_command(label="Show Location", command=self.show_location)

        # Bind right-click event to the Treeview
        self.table.bind("<Button-3>", self.show_context_menu)

        self.transferred_files = []
        self.populateview()

        

        
        def get_drive_info():
            drive_info = []
            excluded_drive_types = ['cdrom', 'pendrive']  # Types to exclude

            for partition in ps.disk_partitions():
                drive_name = partition.device
                drive_mountpoint = partition.mountpoint
                drive_usage = ps.disk_usage(drive_mountpoint)

                # Check if the drive type is not in the excluded list
                if partition.fstype not in excluded_drive_types:
                    drive_info.append((drive_name, drive_usage))
                    
            return drive_info
        
        def update_progress_bars():
           
            drive_info = get_drive_info()
            for i, (drive_name, drive_usage) in enumerate(drive_info):
                total_capacity = drive_usage.total
                used_capacity = drive_usage.used
                free_capacity = drive_usage.free

                # Calculate the percentage used
                percentage_used = (used_capacity / total_capacity) * 100
                

                # Update the progress bar for the drive
                progress_bars[i]['value'] = percentage_used
            
       
        drive_info = get_drive_info()
        progress_bars = []
        
            
        
        for i, (drive_name, drive_usage) in enumerate(drive_info):
            ts = drive_usage.total/(1024*1024*1024)
            ts = f'{ts:.2f}'
            us = drive_usage.used/(1024*1024*1024)
            us = f'{us:.2f}'
            fr = drive_usage.free/(1024*1024*1024)
            fr = f'{fr:.2f}'
            label = tk.Label(self.tab2, text=f"Drive {drive_name} ", font=('Arial',10, 'bold'))
            label.pack(side=tk.TOP, pady=12)
            #label.grid(column=0, row=i + 1, padx=10, pady=5)
            boot = 'primary'
            progress = ttk.Floodgauge(self.tab2, mask= f"Used Space {us} | Total Space {ts} | Free Space {fr}",length=600, mode="determinate", bootstyle=boot)
            progress.pack(fill='x',padx=(5,5), pady=2)
            #progress.grid(column=1, row=len(progress_bars) + 1, padx=10, pady=5)
            progress_bars.append(progress)
            if us > str(100):
                progress.configure(bootstyle = 'danger')
            else:
                progress.configure(bootstyle = 'primary')

        updatebuttonf = ttk.Button(self.tab2, text='update', command=update_progress_bars)
        updatebuttonf.pack(pady=10)   
        #progress.configure(update_progress_bars())
        
        update_progress_bars()

        self.config_file = "config.json"
        self.load_configuration()
        
        self.profile_image_label = ttk.Label(self.entries)
        self.profile_image_label.pack(pady=10)

        #Load the profile image from the stored path and create a circular mask
        self.load_profile_image()
        self.create_circular_mask()

        #Create a button to update the profile image
        update_image_button = ttk.Button(self.entries, text="Update Image", command=self.update_profile_image)
        update_image_button.pack()

        #Create a label for the user name
        self.name_label = ttk.Label(self.entries, text=self.stats["Name"])
        self.name_label.pack()

        #Create a button to change the user name
        change_name_button = ttk.Button(self.entries, text="Change Name", command=self.change_user_name)
        change_name_button.pack()
        sent_count, received_count = connection.get_sent_received_counts()
        labelsent = translate_notification('Sent')
        sentnum = ttk.Label(self.entries,text=f'{labelsent} :{sent_count}', font=('Arial',8, 'bold'))
        sentnum.pack(pady=5)
        labelreceived = translate_notification('Received')
        receivenum = ttk.Label(self.entries,text=f'{labelreceived} :{received_count}', font=('Arial',8,'bold'))
        receivenum.pack()

        





    def load_configuration(self):
        try:
            with open(self.config_file, "r") as config_file:
                data = json.load(config_file)
                self.profile_image_path = data.get("profile_image", resource_path2(relative_path="images/default.png"))
                self.stats = data.get("stats", {"Name": "John Doe", "Age": 30, "Location": "City"})
        except FileNotFoundError:
            self.profile_image_path = resource_path2(relative_path="images/default.png")
            self.stats = {"Name": "John Doe", "Age": 30, "Location": "City"}

    def save_configuration(self):
        data = {"profile_image": self.profile_image_path, "stats": self.stats}
        with open(self.config_file, "w") as config_file:
            json.dump(data, config_file)

    def load_profile_image(self):
        image = Image.open(self.profile_image_path)
        image.thumbnail((150, 150))
        photo = ImageTk.PhotoImage(image)

        self.profile_image_label.config(image=photo)
        self.profile_image_label.image = photo

    def create_circular_mask(self):
        # Load the profile image
        image = Image.open(self.profile_image_path)
        image = image.convert("RGBA")

        # Create a circular mask with the same size as the profile image
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)

        # Calculate the bounding box for a perfect circle
        width, height = image.size
        circle_size = min(width, height)
        circle_bbox = (0, 0, circle_size, circle_size)

        # Calculate the position to center the circle within the image
        position = ((width - circle_size) // 2, (height - circle_size) // 2)

        # Draw a circle on the mask
        draw.ellipse((position[0], position[1], position[0] + circle_size, position[1] + circle_size), fill=255)

        # Ensure the mask and profile image have the same size
        if image.size != mask.size:
            mask = mask.resize(image.size, Image.ANTIALIAS)

        # Apply the circular mask to the profile image
        result = Image.new("RGBA", image.size)
        result.paste(image, (0, 0), mask)

        # Resize the result to fit the label and create a PhotoImage
        result.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(result)

        # Update the label with the circular profile image
        self.profile_image_label.config(image=photo)
        self.profile_image_label.image = photo


    def update_profile_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])

        if file_path:
            # Save the selected image path, load the new profile image, and save the configuration
            self.profile_image_path = file_path
            self.load_profile_image()
            self.create_circular_mask()
            self.save_configuration()

    def change_user_name(self):
        new_name = simpledialog.askstring("Change Name", "Enter your new name:", parent=self)
        if new_name:
            self.stats["Name"] = new_name
            self.name_label.config(text=new_name)
            self.save_configuration()







        
    from language_config import load_language_config, save_language_config
    from theme_display import checker

    

            
    
    def update_using_manager(self):
        def translate_message_box(title_key, message_key):
            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found

            title = translation_dict.get(title_key)
            message = translation_dict.get(message_key)
            
            message_ico = resource_path(relative_path='images/unt.ico')
            self.iconbitmap(default=message_ico)
            return messagebox.showinfo(title, message)
        try:
            
            # -- Online Version File
            # -- Replace the url for your file online with the one below.
            response = requests.get(
                'http://localhost/suplike/socketra/updates/version.txt')
            data = response.text

            if float(data) > float(__version__):
                translate_message_box('Software Update', 'Update Available !')
                def translate_notification(message_key):
                    if self.current_language in self.translations:
                        translation_dict = self.translations[self.current_language]
                    else:
                        translation_dict = self.translations['en']  # Fallback to English if the language is not found
                    return translation_dict.get(message_key, message_key)
                UPDATE = translate_notification('Update!')
                MESSAGE = translate_notification('needs to update to version')

                mb2 = messagebox.askyesno(f'{UPDATE}', f'{__AppName__} {__version__} {MESSAGE} {data}')
                if mb2 is True:
                    UpdateManager(self)
                elif mb2 == 'No':
                    pass
            else:
                
                translate_message_box('Software Update', 'No Updates Available')
        except Exception as e:
            print('The Error is here!')
            translate_message_box('Software Update', 'Unable to Check for Update, No internet')
    
    
    desktop, documents, videos, music, downloads, pictures = receive_loc()
    
    from table_options import show_context_menu, delete_selected_item
    
    def populateview(self):
        self.table.delete(*self.table.get_children())
        fetch = connection.get_transferred_files()
        
        for idx, data in enumerate(fetch):
            tag = 'oddrow' if idx % 2 == 1 else 'evenrow'
            self.table.insert("", 0, values=(data[1], data[2], data[3], data[4]), tags=(tag,))

    
    
    wifi = get_ip.get_ip('wlan0')

    def stop_transfer(self):
        if hasattr(self, 'client_socket') and self.client_socket:
            self.client_socket.close()
        if hasattr(self, 'server_socket') and self.server_socket:
             self.server_socket.close()
        
    
    def disable_buttons(self):
            self.select_button.configure(state='disabled')
            self.receive_button.configure(state='disabled')
            
    def enable_buttons(self):
        self.select_button.configure(state='normal')
        self.receive_button.configure(state='normal')
        
    def stop_enable(self):
        
        self.stop_button.configure(state='normal')
        
    def stop_disable(self):
        
        self.stop_button.configure(state='disabled')
    


    def open_file_dialog(self):
        file_paths = filedialog.askopenfilenames()
        self.send_file(file_paths)

    def send_files(self,file_paths):
        self.HOST = self.host.get()
        self.PORT = self.port.get()
        self.PORT = 4444
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.HOST, self.PORT))
            for file_path in file_paths:
                filename = os.path.basename(file_path)
                filesize = os.path.getsize(file_path)
                client_socket.send(f"{filename},{filesize}".encode())
                with open(file_path, "rb") as f:
                    while True:
                        data = f.read(1024)
                        if not data:
                            break
                        client_socket.send(data)
                print(f"Sent {filename}")
            print("File transfer completed.")
    

    # def send_file(self):
    #     self.disable_buttons()
        
        
    #     self.filepaths = filedialog.askopenfilenames()
        
    #     self.HOST = self.host.get()
    #     self.PORT = self.port.get()

       
     
    #     if self.PORT == "":
    #         self.PORT = 4444
    #     else:
    #         self.PORT = int(self.PORT)
        
    #     self.send_stop = False
    #     def translate_notification(message_key):
    #         if self.current_language in self.translations:
    #             translation_dict = self.translations[self.current_language]
    #         else:
    #             translation_dict = self.translations['en']  # Fallback to English if the language is not found
    #         return translation_dict.get(message_key, message_key)

        
    
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
    #         if self.HOST == '':
    #             info2 = translate_notification("The IP can't be empty")
    #             self.message = ToastNotification(title='Response',alert=True,message=f'{info2}',duration=3000,bootstyle='danger')
    #             self.message.show_toast()
    #         # elif self.HOST == self.wifi:
    #         #     info3 = translate_notification("Please use the receiver's IP not your IP")
    #         #     self.message = ToastNotification(title='Response',alert=True,message=info3,duration=3000,bootstyle='danger')
    #         #     self.message.show_toast()
    #         elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
    #             info4 = translate_notification("is a wrong IP address format")
    #             self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info4}',duration=3000,bootstyle='danger')
    #             self.message.show_toast()
    #         elif len(self.HOST) > 15 or len(self.HOST) < 8:
    #             info5 = translate_notification("is not Valid IP")
    #             self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info5}',duration=3000,bootstyle='danger')
    #             self.message.show_toast()
    #         elif not self.filepaths:
    #             # No files selected
    #             info12 = translate_notification("It seems your selection was empty")
    #             self.toast = ToastNotification(title='Response', alert=True, message=info12, duration=3000, bootstyle='danger')
    #             self.toast.show_toast()
    #             self.enable_buttons()  # Re-enable the buttons
    #             return
    #         else:
    #             self.client_socket.connect((self.HOST, self.PORT))
    #             for file_path in self.filepaths:
    #                 filename = os.path.basename(file_path)
    #                 total_size = os.path.getsize(file_path)
    #                 self.client_socket.sendall(f"{filename},{total_size}".encode())
                    

                        
    #                 convert = total_size
    #                 # convert = convert/(1024*1024)
    #                 # convert = float(f"{convert:.2F}")
    #                 if total_size < 1024:
    #                     size_units = 'B'
    #                     formatted_size = f"{convert} {size_units}"
    #                 elif total_size < 1024**2:
    #                     size_units = 'KB'
    #                     convert/= 1024
    #                     formatted_size = f"{convert:.2f} {size_units}"
    #                 elif total_size < 1024**3:
    #                     size_units = 'MB'
    #                     convert/=(1024*1024)
    #                     formatted_size = f"{convert:.2f} {size_units}"
    #                 else:
    #                     size_units = 'GB'
    #                     convert/=(1024*1024*1024)
    #                     formatted_size = f"{convert:.2f} {size_units}"
    #                 self.stop_enable()
    #                 progress_window = ProgressWindow(self, total_size)
    #                 bytes_sent = 0

    #                 def update_estimated_time_remaining(bytes_sent, total_size, start_time):
    #                     current_time = time.time()
    #                     elapsed_time = current_time - start_time
    #                     transfer_rate = bytes_sent / elapsed_time if elapsed_time > 0 else 0
    #                     remaining_bytes = total_size - bytes_sent
    #                     estimated_time_remaining = remaining_bytes / transfer_rate if transfer_rate > 0 else 0
    #                     return estimated_time_remaining
    #                 start_time = time.time()
    #                 with open(file_path, "rb") as f:
    #                     data = f.read(1024)
    #                     while data:
    #                         #data = f.read(1024)
    #                         if not data:
    #                             break
    #                         self.client_socket.sendall(data)
    #                         bytes_sent += len(data)
    #                         progress = (bytes_sent / total_size) * 100
    #                         progress_window.progress_bar['value'] = bytes_sent
    #                         self.update_idletasks()
                            

    #                         estimated_time_remaining = update_estimated_time_remaining(bytes_sent, total_size, start_time)
                            
    #                         self.t_time.configure(text=f"{int(progress)}%   {estimated_time_remaining:.1f} secs")
                            
    #                         data = f.read(1024)
    #                 print(f"Sent {filename}")
    #             print("File transfer completed.")
        
        
        
    #     self.enable_buttons()

        #threading.Thread(target=transfer_file).start()
    


    def send_file(self):
        self.disable_buttons()
        
        
        self.filepaths = filedialog.askopenfilenames()
        
        self.HOST = self.host.get()
        self.PORT = self.port.get()

       
     
        if self.PORT == "":
            self.PORT = 4444
        else:
            self.PORT = int(self.PORT)
        
        self.send_stop = False
        def translate_notification(message_key):
            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found
            return translation_dict.get(message_key, message_key)

        
    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
            if self.HOST == '':
                info2 = translate_notification("The IP can't be empty")
                self.message = ToastNotification(title='Response',alert=True,message=f'{info2}',duration=3000,bootstyle='danger')
                self.message.show_toast()
            # elif self.HOST == self.wifi:
            #     info3 = translate_notification("Please use the receiver's IP not your IP")
            #     self.message = ToastNotification(title='Response',alert=True,message=info3,duration=3000,bootstyle='danger')
            #     self.message.show_toast()
            elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                info4 = translate_notification("is a wrong IP address format")
                self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info4}',duration=3000,bootstyle='danger')
                self.message.show_toast()
            elif len(self.HOST) > 15 or len(self.HOST) < 8:
                info5 = translate_notification("is not Valid IP")
                self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info5}',duration=3000,bootstyle='danger')
                self.message.show_toast()
            elif not self.filepaths:
                # No files selected
                info12 = translate_notification("It seems your selection was empty")
                self.toast = ToastNotification(title='Response', alert=True, message=info12, duration=3000, bootstyle='danger')
                self.toast.show_toast()
                self.enable_buttons()  # Re-enable the buttons
                return
        
        def send_files_in_thread():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
                    self.client_socket.connect((self.HOST, self.PORT))
                    for file_path in self.filepaths:
                        filename = os.path.basename(file_path)
                        total_size = os.path.getsize(file_path)
                        self.client_socket.sendall(f"{filename},{total_size}".encode())
                        

                            
                        convert = total_size
                        # convert = convert/(1024*1024)
                        # convert = float(f"{convert:.2F}")
                        if total_size < 1024:
                            size_units = 'B'
                            formatted_size = f"{convert} {size_units}"
                        elif total_size < 1024**2:
                            size_units = 'KB'
                            convert/= 1024
                            formatted_size = f"{convert:.2f} {size_units}"
                        elif total_size < 1024**3:
                            size_units = 'MB'
                            convert/=(1024*1024)
                            formatted_size = f"{convert:.2f} {size_units}"
                        else:
                            size_units = 'GB'
                            convert/=(1024*1024*1024)
                            formatted_size = f"{convert:.2f} {size_units}"
                        self.stop_enable()
                        progress_window = ProgressWindow(self, total_size)
                        bytes_sent = 0

                        def update_estimated_time_remaining(bytes_sent, total_size, start_time):
                            current_time = time.time()
                            elapsed_time = current_time - start_time
                            transfer_rate = bytes_sent / elapsed_time if elapsed_time > 0 else 0
                            remaining_bytes = total_size - bytes_sent
                            estimated_time_remaining = remaining_bytes / transfer_rate if transfer_rate > 0 else 0
                            return estimated_time_remaining
                        start_time = time.time()
                        with open(file_path, "rb") as f:
                            data = f.read(1024)
                            while data:
                                #data = f.read(1024)
                                if not data:
                                    break
                                self.client_socket.sendall(data)
                                bytes_sent += len(data)
                                progress = (bytes_sent / total_size) * 100
                                progress_window.progress_bar['value'] = bytes_sent
                                self.update_idletasks()
                                

                                estimated_time_remaining = update_estimated_time_remaining(bytes_sent, total_size, start_time)
                                
                                self.t_time.configure(text=f"{int(progress)}%   {estimated_time_remaining:.1f} secs")
                                
                                data = f.read(1024)
                        print(f"Sent {filename}")
                        print("File transfer completed.")
                        progress_window.destroy()
            except Exception as e:
                # Handle exceptions and show error messages if needed
                print(f"Error: {str(e)}")
            self.enable_buttons()  # Re-enable the buttons when file transfer is completed or failed

        # Create a new thread to send files
        send_thread = threading.Thread(target=send_files_in_thread)
        send_thread.start()
           

    def receive_file(self):       

        self.stop_receive = False
        def translate_notification(message_key):
            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found
            return translation_dict.get(message_key, message_key)
        
        def receive_thread(): 
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.server_socket:
                try:
                    self.HOST = self.host.get()
                    self.PORT = self.port.get()
                    self.HOST = str(self.HOST) 
                    self.PORT = int(self.PORT)
                    self.location = self.loc.get()
                    
                    
                    if self.location == '':
                        info1 = translate_notification("The Receiving Dir path is not specified")
                        self.message = ToastNotification(title='Response',alert=True,message=info1,duration=3000,bootstyle='warning')
                        self.message.show_toast()
                        
                    else: 
                        
                        self.server_socket.bind((self.HOST, self.PORT))
                        self.server_socket.listen()

                        print("Server is waiting for connections...")

                        self.conn, self.addr = self.server_socket.accept()

                    

                    
                    
                    #self.filename = self.conn.recv(1024).decode()
                    filename_with_size = self.conn.recv(1024).decode()
                    self.filename, total_size = filename_with_size.split(':')
                    total_size = int(total_size)
                    convert = total_size
                    if total_size < 1024:
                        size_units = 'B'
                        formatted_size = f"{convert} {size_units}"
                    elif total_size < 1024**2:
                        size_units = 'KB'
                        convert/= 1024
                        formatted_size = f"{convert:.2f} {size_units}"
                    elif total_size < 1024**3:
                        size_units = 'MB'
                        convert/=(1024*1024)
                        formatted_size = f"{convert:.2f} {size_units}"
                    else:
                        size_units = 'GB'
                        convert/=(1024*1024*1024)
                        formatted_size = f"{convert:.2f} {size_units}"
                    self.disable_buttons()
                    self.stop_disable()
                    
                    self.file_path = os.path.join(self.location, self.filename)
                    with open(self.file_path, 'wb') as file:
                        data = self.conn.recv(4096)
                        while data:
                            if self.stop_receive:
                                break
                            file.write(data)
                            data = self.conn.recv(4096)

                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    max_filename_length = 20  # Adjust this value as needed
                    displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')

                    self.transferred_files.append(("",f"{current_time}",f"{formatted_size}",f"{displayed_filename}"))
                    #self.table.delete(*self.table.get_children())
                    for idx, data in enumerate(self.transferred_files):
                        tag = 'evenrow' if idx % 2 == 0 else 'oddrow'

                    self.table.insert("", 0, values=("", current_time, formatted_size, displayed_filename),tags=(tag,))
                    connection.insert_received_file(displayed_filename, current_time,formatted_size)
                    
                        
                    if not self.stop_receive:
                       #print(f"File '{self.filename}' received and saved successfully.")
                        info1 = translate_notification("received successfully")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.filename} {info1}',duration=3000,bootstyle='success')
                        self.message.show_toast()
                    else:
                        print("Transfer stopped by user.")  
                        
                    
                except:
                    if self.HOST == '':
                        info2 = translate_notification("The IP can't be empty")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{info2}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                    # elif self.HOST != self.wifi:
                    #     info3 = translate_notification("Please use your IP")
                    #     self.message = ToastNotification(title='Response',alert=True,message=f'{info3} {self.wifi}',duration=3000,bootstyle='danger')
                    #     self.message.show_toast()
                    elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                        info4 = translate_notification("is a wrong IP address format")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info4}',duration=3000,bootstyle='warning')
                        self.message.show_toast()
                    elif len(self.HOST) > 15 or len(self.HOST) < 8:
                        info5 = translate_notification("is not Valid IP")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info5}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                finally:
                    self.enable_buttons()
                           
        threading.Thread(target=receive_thread).start()




if __name__ == "__main__":
    root = Root()
    root.mainloop()
    