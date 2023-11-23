
from packages import *



connection.Database()
import json

from metadata import __version__ 
from metadata import __AppName__

Image.CUBIC = Image.BICUBIC

class Root(ttk.Window):
    def __init__(self):
        super().__init__()

        self.send_file_count = 0
        self.receive_file_count = 0
        if os.path.exists('ips'):
            pass
        else:
            os.makedirs('ips')
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
            root.filemenu.entryconfig(1, label=translation_dict.get('Send', ''))
            root.filemenu.entryconfig(2, label=translation_dict.get('Receive', ''))
            root.helpmenu.entryconfig(0, label=translation_dict.get('About', ''))
            root.helpmenu.entryconfig(1, label=translation_dict.get('Check for Updates', ''))
            root.helpmenu.entryconfig(2, label=translation_dict.get('How To', ''))
            root.helpmenu.entryconfig(3, label=translation_dict.get('Language', ''))
            root.labelport.config(text=translation_dict.get('Port', ''))
            root.labelloc.config(text=translation_dict.get('Receive Dir', ''))
            root.context_menu.entryconfig(0,label=translation_dict.get('Delete', ''))
            sent_received = translation_dict.get('Sent/Received','')
            youtu = translation_dict.get('Youtube Downloads','')
            root.note.add(self.tab1, text=sent_received)
            root.note.add(self.tab2, text=youtu)
            root.check.config(text=translation_dict.get('mode',''))
            root.howto_submenu.config()
            root.sentnum.config(text=translation_dict.get('sent:', '') + f'{sent_count}')
            root.receivenum.config(text=translation_dict.get('received:', '') + f'{received_count}')
            root.Label_link.config(text=translation_dict.get('Link:', ''))
            root.Label_savefolder.config(text=translation_dict.get('Save To:', ''))
            root.vid_resolution_label.config(text=translation_dict.get('Resolution',''))
            root.youtube_download_butt.config(text=translation_dict.get('Download',''))

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
        w = 1060
        h = 650#780
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=True, height=True)
        # self.iconpath = resource_path(relative_path='images//unt.ico')
        # #self.iconbitmap(self.iconpath)
        self.iconpath = resource_path(relative_path='images/unt1.ico')
        self.wm_iconbitmap(self.iconpath)
        #self.iconpath = Image.open(resource_path('icon.png'))
        
        #self.wm_iconwindow(self.iconpath)
        
        
        def translate_notification(text):
            if self.current_language in self.translations:
                translation_dict = self.translations[self.current_language]
            else:
                translation_dict = self.translations['en']  # Fallback to English if the language is not found
            return translation_dict.get(text, text)
        
        
        self.menubar = ttk.Menu(self)
        self.filemenu = ttk.Menu(self.menubar, tearoff=0)
        
        self.filemenu.add_command(label=translate_notification('Exit'),command=self.destroy)
        self.filemenu.add_command(label=translate_notification('Send'),command=self.send_file)
        self.filemenu.add_command(label=translate_notification('Receive'),command=self.receive_file)
        
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
        #self.howto_submenu.add_radiobutton(label='Tamil', command=lambda: change_language('ta'))
        self.howto_submenu.add_radiobutton(label='Hindi', command=lambda: change_language('hi'))
        self.howto_submenu.add_radiobutton(label='Akan', command=lambda: change_language('ak'))
          
        
        #self.helpmenu.add_command(label='How To',command=howto)
        self.helpmenu.add_cascade(label=translate_notification('Language'), menu=self.howto_submenu)
        self.menubar.add_cascade(label=translate_notification('Help'),menu=self.helpmenu)
        #self.menubar.add_cascade(label='Settings')
        

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

        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(fill='both', side='left', padx=(1, 1), pady=1)


        self.entries = ttk.Frame(self.container_frame,width=70)
        self.entries.pack(fill='both',side='left',padx=(1,1),pady=1)
        
        self.entries2 = ScrolledFrame(self.container_frame,width=250, autohide=True)
       
        self.entries2.pack(fill='both', side='left', padx=(1, 1), pady=1)
        self.first_frame = ttk.Frame(self.entries2)
        self.first_frame.pack(padx=(1,1),pady=1)
        # My_Profile = ttk.Label(self.entries, text='My Profile', font=('Arial',9,'bold'))
        # My_Profile.pack(side='right',padx=(2,62))
        self.second_frame = ttk.Frame(self.entries2)
        self.second_frame.pack()
        self.third_frame = ttk.Frame(self.entries2)
        self.third_frame.pack(fill='x',pady=5)
        self.fourth_frame = ttk.Frame(self.entries2)
        self.fourth_frame.pack(pady=6)



        self.entries2.pack_forget()
        

        

        
        
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
        
        
        self.t_time = ttk.Label(self.button_frame, text="")
        self.t_time.pack(side=tk.RIGHT,padx=(3,12))

        
        

        
        self.note = ttk.Notebook(self, bootstyle='info')
        self.tab1 = ttk.Frame(self)
        self.tab2 = ttk.Frame(self)
        #self.tab3 = ttk.Frame(self)

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
        #self.note.add(self.tab3,text=translate_notification('Disk Space'))
        self.note.add(self.tab2,text=translate_notification('Youtube Downloads'))
        self.note.pack(fill=tk.BOTH, expand=1)

        
        # Create a context menu
        self.context_menu = tk.Menu(self.table, tearoff=0)
        self.context_menu.add_command(label=translate_notification("Delete"), command=self.delete_selected_item)
        #self.context_menu.add_command(label="Show Location", command=self.show_location)

        # Bind right-click event to the Treeview
        self.table.bind("<Button-3>", self.show_context_menu)

        self.transferred_files = []
        self.populateview()

        
        
        #update_drive_info_and_progress_bars(self.tab3)

         
        
        self.config_file = "config.json"
        self.load_configuration()

        image_frame = ttk.Frame(self.second_frame)
        image_frame.pack()
        
        self.profile_image_label = ttk.Label(image_frame)
        self.profile_image_label.pack()

        #Load the profile image from the stored path and create a circular mask
        self.load_profile_image()
        self.create_circular_mask()

        #Create a button to update the profile image
        update_image_button = ttk.Button(image_frame, text="Edit Image", command=self.update_profile_image, width=13, bootstyle='success')
        update_image_button.pack()

        name_frame = ttk.Frame(self.second_frame)
        name_frame.pack(pady=2)

        #Create a label for the user name
        self.name_label = ttk.Label(name_frame, text=self.stats["Name"])
        self.name_label.pack(side='left',padx=(55,2))

        

        #Create a button to change the user name
        edit_name = ImageTk.PhotoImage(Image.open(resource_path2('images/edit.png')))
        change_name_button = ttk.Button(name_frame, image=edit_name, command=self.change_user_name, bootstyle='Link.Tbutton')
        change_name_button.pack(side='left',padx=5)
        change_name_button.image = edit_name
        
        sent_count, received_count = connection.get_sent_received_counts()
        self.labelsent = translate_notification("sent:") 
        self.sentnum = ttk.Label(self.second_frame,text=f"{self.labelsent} {sent_count}", font=('Arial',8,'bold'))
        self.sentnum.pack(pady=5)
        self.labelreceived = translate_notification("received:") 
        self.receivenum = ttk.Label(self.second_frame,text=f'{self.labelreceived} {received_count}', font=('Arial',8,'bold'))
        self.receivenum.pack(pady=5)

        self.sep = ttk.Separator(self.third_frame, bootstyle='danger', orient='horizontal')
        self.sep.pack(fill='x',pady=3, padx=50)

       

        def get_image_paths(directory):
            image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
            return image_paths

        def create_circular_image(image_path, size=(70, 70)):
            img = Image.open(image_path)
            img = img.resize(size)
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + size, fill=255)
            img.putalpha(mask)
            return img

        def show_images_in_rows(image_paths):

            for image_path in image_paths:
                
                    

                img = create_circular_image(image_path)
                img_tk = ImageTk.PhotoImage(img)
                label_pic = ttk.Label(self.fourth_frame, image=img_tk)
                label_pic.image = img_tk
                label_pic.pack()

                button_pic = ttk.Button(self.fourth_frame, text="Click Me",command=self.button_click(image_path))
                button_pic.pack(padx=5,pady=8)
        folder_wifi = get_wifi_ssid()

        # folder_wifi = 'Physics Lab'
        if os.path.exists('ips') and os.path.isdir('ips'):
            dir_cont = os.listdir('ips')
           
        for dir in dir_cont:
            if dir == folder_wifi:
                #userr = os.path.expanduser(f'~\\AppData\\Local\\ConveTransfer\\ips\\{folder_wifi}')
                directory = f'ips/{folder_wifi}'
                #userr = os.path.expanduser(f'C:/Users/DELL/Desktop/socketra/ConveTransfer2/ips/{folder_wifi}/')
               
        
                image_paths = get_image_paths(directory)
                show_images_in_rows(image_paths)
            # else:
            #     label_pic.config(state='disabled')
            #     button_pic.config(state='disabled')
                
        # directory = "C:/Users/DELL/Desktop/pics/"  # Replace with your image directory path
        # image_paths = get_image_paths(directory)
        # print(image_paths)
        # show_images_in_rows(image_paths)
        

        def show_entries2():
            self.entries.pack_forget()
            self.entries2.pack(fill='both', side='left', padx=(1, 1), pady=1)
        self.entries_button = ttk.Button(self.entries, text='Show Stats', command=show_entries2)
        self.entries_button.pack(pady=5)

        def show_entries():
            self.entries2.pack_forget()
            self.entries.pack(fill='both', side='left', padx=(1, 1), pady=1)
        
        im = ImageTk.PhotoImage(Image.open(resource_path2('images/back.png')))
        self.entries2_button = ttk.Button(self.first_frame,image=im,bootstyle='Link.Tbutton', command=show_entries)
        self.entries2_button.pack(padx=(1,180))
        self.entries2_button.image = im


       
        youtube_tab(self)

        
        
    # def toggle_frames(self):
    #     if self.entries.winfo_ismapped():  # Check if the first frame is currently visible
    #         self.entries.pack_forget()  # Hide the first frame
    #         self.second_frame.pack(fill='both', side='left', padx=(1, 1), pady=1)  # Show the second frame
    #     else:
    #         self.second_frame.pack_forget()  # Hide the second frame
    #         self.entries.pack(fill='both', side='left', padx=(1, 1), pady=1)  # Show the first frame

    from language_config import load_language_config, save_language_config
    from theme_display import checker

    
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
        name_ico = resource_path(relative_path='images/unt.ico')
        self.iconbitmap(default=name_ico)
        new_name = simpledialog.askstring("Change Name", "Enter your new name:", parent=self)
        if new_name:
            self.stats["Name"] = new_name
            self.name_label.config(text=new_name)
            self.save_configuration()







        
    

    

            
    
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
        self.send_files(file_paths)

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


    def send_file(self):
        self.disable_buttons()
        
        
        self.filepath = filedialog.askopenfilename()
        self.filename = os.path.basename(self.filepath)

        
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

        
        try:
            total_size = os.path.getsize(self.filepath)
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
        except:
            
                            
            #self.message = Messagebox.show_info('Response', "It seems your selection was empty")
            info12 = translate_notification("It seems your selection was empty")
            self.toast = ToastNotification(title='Response',alert=True,message=info12,duration=3000,bootstyle='danger')
            self.toast.show_toast()
            # If unable to get total size, re-enable the buttons and return
            self.enable_buttons()
            return
            
        
        progress_window = ProgressWindow(self, total_size)

        def transfer_file():
           
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
                    self.client_socket.connect((self.HOST, self.PORT))
                    #self.client_socket.sendall(self.filename.encode())
                    
                    

                    
                    
                    filename_with_size = f"{self.filename}:{total_size}"

                    # Send the filename_with_size to the receive_file method
                    self.client_socket.sendall(filename_with_size.encode())

                    
                    

                    bytes_sent = 0

                    # def update_estimated_time_remaining(bytes_sent, total_size, start_time):
                    #     current_time = time.time()
                    #     elapsed_time = current_time - start_time
                    #     transfer_rate = bytes_sent / elapsed_time if elapsed_time > 0 else 0
                    #     remaining_bytes = total_size - bytes_sent
                    #     estimated_time_remaining = remaining_bytes / transfer_rate if transfer_rate > 0 else 0
                    #     return estimated_time_remaining
                    # start_time = time.time() 
                    
                    with open(self.filepath, 'rb') as self.file:
                        self.data = self.file.read(4096)
                        while self.data:
                            
                            if self.send_stop:
                                break
                            self.client_socket.sendall(self.data)
                            bytes_sent += len(self.data)
                            progress = (bytes_sent / total_size) * 100
                            progress_window.progress_bar['value'] = bytes_sent
                            self.update_idletasks()
                            
                    
                            # estimated_time_remaining = update_estimated_time_remaining(bytes_sent, total_size, start_time)
                            
                            # self.t_time.configure(text=f"{int(progress)}%   {estimated_time_remaining:.1f} secs")
                            self.t_time.configure(text=f"{int(progress)}% ")
                            
                            self.data = self.file.read(4096)
                            
                    print("File sent successfully.")
                    
                    self.send_file_count += 1
                    

                    
                    info1 = translate_notification("sent successfully")
                    self.message = ToastNotification(title='Response',alert=True,message=f'{self.filename}{info1}',duration=3000,bootstyle='success')
                    self.message.show_toast()


                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    max_filename_length = 30  # Adjust this value as needed
                    displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')
    
                    self.transferred_files.append((f"{displayed_filename}",f"{current_time}",f"{formatted_size}"))
                    #self.table.delete(*self.table.get_children())
                    for idx, data in enumerate(self.transferred_files):
                        tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
                    self.table.insert("", 0, values=(f"{displayed_filename}",f"{current_time}",f"{formatted_size}"),tags=(tag,))
                    connection.insert_sent_file(displayed_filename, current_time, formatted_size)
                
                    
                    
                    

                    

            except Exception as e:
                #print(f'This is the reason {e}')
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
            finally:
                # Destroy the progress window
                progress_window.destroy()
                # Reactivate the button once cdthe event is completed or an error occurs
                
                self.enable_buttons()
                self.stop_disable()
                self.t_time.configure(text='')
                
               
                

        # Start the file transfer in a separate thread
        threading.Thread(target=transfer_file).start()
        if self.send_file_count == 4:
            threading.Thread(target=self.send_image).start()
        
        
    
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
                        info1 = "The Receiving Dir path is not specified"
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
                        
                    self.receive_file_count += 1
                                          
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
                    elif self.location == '':
                        info1 = "The Receiving Dir path is not specified"
                        self.message = ToastNotification(title='Response',alert=True,message=info1,duration=3000,bootstyle='warning')
                        self.message.show_toast()
                        
                finally:
                    self.enable_buttons()
            self.server_socket.close()

                    
        threading.Thread(target=receive_thread).start()
        if self.receive_file_count == 4:
            threading.Thread(target=self.receive_image).start()    
        
        
        
    def send_image(self):
        self.HOST = self.host.get()
        #self.PORT = self.port.get()
        self.PORT = 8080
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.HOST, self.PORT))

            
            try:
                with open('config.json','r') as fj:
                    con = json.load(fj)
                img = con.get("profile_image", '')
                #ts = os.path.getsize(img)
                user = con.get("stats", {}).get('Name', '')
                if os.path.exists(img):
                    imga = os.path.basename(img)
                    ip_addr1 = get_ip.get_ip('wlan0')
                    if imga.endswith('.png'):
                        ip_addr = f"{ip_addr1}.png"
                    elif imga.endswith('.jpg'):
                        ip_addr = f"{ip_addr1}.jpg"
                    elif imga.endswith('jpeg'):
                        ip_addr = f"{ip_addr1}.jpg" 
                    # ts = os.path.getsize(img)
                else:
                    print('couldnt find anything')
            except FileNotFoundError:
                img = resource_path2(relative_path="images/default.png")
                ip_addr1 = get_ip.get_ip('wlan0')
                ip_addr = f"{ip_addr1}.png"
                

            client_socket.send(f"{ip_addr}".encode())
            with open(img, "rb") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    client_socket.send(data)
            print(f"Sent {img}")
        print("File transfer completed.")

    

    
    def receive_image(self):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            self.HOST = self.host.get()
            #self.PORT = self.port.get()
            self.PORT = 8080
            server_socket.bind((self.HOST, self.PORT))
            server_socket.listen()
            
            conn, addr = server_socket.accept()

            filename_e = conn.recv(1024).decode()
            
            
            
            wifinam = get_wifi_ssid()
            if wifinam is None:
                # Set a default folder name when the SSID is not available
                folder = 'ips/default'
            else:
                folder = f'ips/{wifinam}'

            if not os.path.exists(folder):
                os.makedirs(folder)

            # Extract the filename without the extension
            filename_base, file_extension = os.path.splitext(filename_e)
            
            # Construct the full file path using the filename without extension
            old_filename = os.path.join(folder, filename_base)
            new_filename = os.path.join(folder,filename_e)

            # Remove existing files with different extensions but the same base filename
            for ext in ['.png', '.jpg', '.jpeg']:
                existing_file = old_filename + ext
                if os.path.exists(existing_file):
                    os.remove(existing_file)


            with open(new_filename, 'wb') as file:
                data = conn.recv(1024)
                while data:
                    file.write(data)
                    data = conn.recv(1024)
            server_socket.close()            
    
    def button_click(self,image_path):
        def on_button_click():
            host = os.path.splitext(os.path.basename(image_path))[0]
            print(type(host))
            print(f'{host}')
            print(f"Clicked on button for image: {image_path}")
            # Add your logic to handle the click action here
        return on_button_click
    
    
if __name__ == "__main__":
    root = Root()
    root.mainloop()
        
