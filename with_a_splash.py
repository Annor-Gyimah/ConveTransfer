
import ctypes.wintypes
from packages import *
import random


connection.Database()
import json

from metadata import __version__ 
from metadata import __AppName__




class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Splash Screen")
        self.attributes("-topmost", 1)

        width_of_window = 427
        height_of_window = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.geometry("%dx%d+%d+%d" %(width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.overrideredirect(1)  # for hiding titlebar

        bbc = '#1b1f1d'
        style = ttk.Style()
        style.configure("Splash.TFrame", background=bbc)

        splashframe = ttk.Frame(self, width=427, height=250, style="Splash.TFrame")  # Use the style
        splashframe.pack(fill='both', expand=True)
        
        self.after(4000, self.destroy)  # Adjust the duration as needed
        conveframe = ttk.Frame(splashframe, width=30, style="Splash.TFrame")
        conveframe.pack(pady=20)
        faunt = ('Helvetica',15,'italic')
        labelC=ttk.Label(conveframe, text='CON', foreground='#03fc7f', background=bbc ,font=faunt)
        labelC.pack(side=tk.LEFT,padx=1,pady=1) #decorate it 
        labelV=ttk.Label(conveframe, text='VE', foreground='#d7fc03', background=bbc ,font=faunt)
        labelV.pack(side=tk.LEFT,padx=1,pady=1)
        labelT=ttk.Label(conveframe, text='TRANS', foreground='#036ffc', background=bbc ,font=faunt)
        labelT.pack(side=tk.LEFT,padx=1,pady=1)
        labelF=ttk.Label(conveframe, text='FER', foreground='#fc0362', background=bbc ,font=faunt)
        labelF.pack(side=tk.LEFT,padx=1,pady=1)
        # label4=ttk.Label(conveframe, text='O', foreground='yellow', font=faunt)
        # label4.pack(side=tk.LEFT,padx=1,pady=1) #decorate it 

        
        progress_label=ttk.Label(splashframe, text='Loading...', foreground='#108cff', background=bbc) #decorate it 
        #label2.configure(font=("Calibri", 11))
        progress_label.pack(pady=45)
        

        progress = ttk.Progressbar(splashframe, orient=HORIZONTAL,length=400, mode= 'determinate', bootstyle='danger')#, style='red.Horizontal.TProgressbar')
        progress.pack()
        

        self.i = 0
        def load():
            global i
            if self.i <= 10:
                txt = 'Loading...' + (str(10*self.i)+'%')
                progress_label.config(text=txt)
                progress_label.after(330, load)
                progress['value'] = 10 * self.i
                # if progress['value'] == 30:
                #     progress.configure(bootstyle='primary')
                # else:
                #     #progress.configure(bootstyle='success')
                #     pass
                
                self.i += 1
            else:
                pass

        load()

class Root(ttk.Window, TkinterDnD.DnDWrapper):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        # Splash screen duration (in milliseconds)
        splash_duration = 6000

        # Create and display the splash screen
        splash = SplashScreen(self)
        splash.grab_set()
        self.title(__AppName__ + ' ' + str(__version__))
        w = 1060
        h = 690  # 780
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=True, height=True)
        self.iconpath = resource_path(relative_path='images/unt.ico')
        self.wm_iconbitmap(self.iconpath)

        # Hide the main window during splash screen display
        self.withdraw()

        # Destroy the splash screen and show the main window after the specified duration
        self.after(splash_duration, self.show_main_window)
    def show_main_window(self):
        self.deiconify()
        self.send_file_count = 0
        self.receive_file_count = 0
        if os.path.exists('ips'):
            pass
        else:
            os.makedirs('ips')
        
        if os.path.exists('language_config.txt'):
            pass
        else:
            with open('language_config.txt', 'w') as fi:
                fi.write('en')
            fi.close()
        

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
            stop_button_tooltip_text = translate_notification('Click to stop a file in transmission')
            ToolTip(self.stop_button, text=stop_button_tooltip_text, bootstyle=INVERSE)
            update_button_tooltip_text = translate_notification('Update for new features and bug fixes')
            ToolTip(self.update_button, text=update_button_tooltip_text, bootstyle=INVERSE)
           


        
        
    
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
            root.labelloc.config(text=translation_dict.get('Receive Folder', ''))
            root.labelpath.config(text=translation_dict.get('Receive Path', ''))
            root.context_menu.entryconfig(0,label=translation_dict.get('Open', ''))
            root.context_menu.entryconfig(1,label=translation_dict.get('Delete', ''))
            root.context_menu.entryconfig(2,label=translation_dict.get('Remove', ''))
            root.context_menu.entryconfig(3,label=translation_dict.get('Properties', ''))
            sent_received = translation_dict.get('Sent/Received','')
            youtu = translation_dict.get('Youtube Downloads','')
            profile = translation_dict.get('Profile','')
            drandrop = translation_dict.get("Drag 'n' Drop", '')
            phonelink = translation_dict.get("Phone Link", '')
            root.note.add(self.tab1, text=sent_received)
            root.note.add(self.tab2, text=youtu)
            root.note.add(self.tab3, text=profile)
            root.note.add(self.tab4, text=drandrop)
            root.note.add(self.tab5, text=phonelink)
            root.check.config(text=translation_dict.get('mode',''))
            root.howto_submenu.config()
            root.sentnum.config(text=translation_dict.get('sent:', '') + f'{sent_count}')
            root.receivenum.config(text=translation_dict.get('received:', '') + f'{received_count}')
            root.Label_link.config(text=translation_dict.get('Link:', ''))
            root.Label_savefolder.config(text=translation_dict.get('Save To:', ''))
            root.vid_resolution_label.config(text=translation_dict.get('Resolution',''))
            root.youtube_download_butt.config(text=translation_dict.get('Download',''))
            drag_label.config(text=translation_dict.get('Drag and drop to transfer files',''))
            root.push_button.config(text=translation_dict.get('Turn On', ''))
            root.step1_label.config(text=translation_dict.get("Connect both phone and pc to the same network.",''))
            root.step2_label.config(text=translation_dict.get("Click on the 'Turn On' to start sharing.",''))
            root.step3_label.config(text=translation_dict.get("Open up your phone's camera or your qrcode scanner to scan the qrcode.",''))
            root.step4_label.config(text=translation_dict.get("A link will be generated on your phone via the qrcode scanner.",''))
            root.ss1.config(text=translation_dict.get("Click on it to go to your browser.",''))
            root.other_steps_label.config(text=translation_dict.get("Or Alternatively, open your web browser on your phone.", ''))
            root.oo2.config(text=translation_dict.get("Then you type in this address",''))
            root.step5_label.config(text=translation_dict.get("Choose a file to upload",''))
            root.step6_label.config(text=translation_dict.get("Select a destination",''))
            root.step7_label.config(text=translation_dict.get("Click on Upload.",''))
            
            #root.button_pic.config(text=translation_dict.get('Send',''))

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
            

        
        # self.title(__AppName__ + ' ' + str(__version__))
        # w = 1060
        # h = 690#780
        # sw = self.winfo_screenwidth()
        # sh = self.winfo_screenheight()
        # x = (sw - w) / 2
        # y = (sh - h) / 2
        # self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        # self.resizable(width=True, height=True)
        # # self.iconpath = resource_path(relative_path='images//unt.ico')
        # # #self.iconbitmap(self.iconpath)
        # self.iconpath = resource_path(relative_path='images/unt.ico')
        # self.wm_iconbitmap(self.iconpath)
        # #self.iconpath = Image.open(resource_path('icon.png'))
        
        # #self.wm_iconwindow(self.iconpath)
        # #self.bind("<Configure>", self.on_resize)

        
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

        # self.tu = ttk.Button(self.button_frame, text='turn on',command=self.Phonelink)
        # self.tu.pack(side=tk.LEFT,padx=1,pady=1)

        
            
        self.var = ttk.IntVar()
        self.check = ttk.Checkbutton(self.button_frame,variable=self.var, bootstyle="round-toggle",onvalue=0,offvalue=1, text=translate_notification("mode"),command=self.checker)
        self.check.pack(side=tk.RIGHT)
        
        
        

        
        

        self.host = ttk.StringVar() 
        self.port = ttk.StringVar()
        self.loc = ttk.StringVar()
        self.perce = ttk.DoubleVar(value=0)

        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(fill='both', side='left', padx=(1, 1), pady=1)


        self.entries = ttk.Frame(self.container_frame,width=70)
        self.entries.pack(fill='both',side='left',padx=(1,1),pady=1)
        
        

        

        
        
        self.labelid = ttk.Label(self.entries,text=translate_notification('IP'),font=('arial',10,'bold'))
        self.labelid.pack(side=tk.TOP,padx=(2,2),pady=2)
        self.stuff = ['127.0.0.1',f'{self.wifi}']
        self.senderid = ttk.Spinbox(self.entries,values=self.stuff,textvariable=self.host)
        self.senderid.pack(side=tk.TOP,padx=(2,2),pady=2)

        
        self.labelport = ttk.Label(self.entries,text=translate_notification('Port'),font=('arial',10,'bold'))
        self.labelport.pack(side=tk.TOP,padx=(2,2),pady=(3,3))
        self.stuff1 = [4444]
        self.portid = ttk.Spinbox(self.entries,values=self.stuff1,textvariable=self.port,takefocus=4444)
        self.portid.pack(padx=2,pady=(2,2))
        
        
        self.labelloc = ttk.Label(self.entries, text=translate_notification("Receive Folder"), font=('arial',10,'bold'))
        self.labelloc.pack(side=tk.TOP,padx=(2,2),pady=2)
        self.folder_nam = ttk.StringVar()
        self.folder_name = ttk.Entry(self.entries, textvariable=self.folder_nam, width=23)
        # self.stuff2 = [f'{self.desktop}', f'{self.documents}', f'{self.videos}', f'{self.music}', f'{self.downloads}', f'{self.pictures}']
        # self.folder_name = ttk.Spinbox(self.entries,values=self.stuff2)
        self.folder_name.pack(fill='y',padx=2,pady=(3,3))

       
        self.t_time = ttk.Label(self.button_frame, text="")
        self.t_time.pack(side=tk.RIGHT,padx=(3,12))
        
        self.radiobuttons_frame = ttk.Frame(self.entries)
        self.radiobuttons_frame.pack(pady=3)
        self.receive_path_label = ttk.Frame(self.radiobuttons_frame)
        self.receive_path_label.pack(pady=3)
        self.labelpath = ttk.Label(self.receive_path_label,text=translate_notification('Receive Path'), font=('arial',10,'bold'))
        self.labelpath.pack()

        self.des = ttk.Radiobutton(self.radiobuttons_frame, bootstyle='danger',text=translate_notification('Desktop'),value=self.desktop,variable=self.loc).pack(padx=(1,85),pady=3)
        self.dow = ttk.Radiobutton(self.radiobuttons_frame, bootstyle='danger',text=translate_notification('Downloads'),value=self.downloads,variable=self.loc).pack(padx=(1,63),pady=3)
        self.doc = ttk.Radiobutton(self.radiobuttons_frame, bootstyle='danger',text=translate_notification('Document'),value=self.documents,variable=self.loc).pack(padx=(2,70),pady=3)
        self.pic = ttk.Radiobutton(self.radiobuttons_frame, bootstyle='danger',text=translate_notification('Pictures'),value=self.pictures,variable=self.loc).pack(padx=(1,92),pady=3)
        self.mus = ttk.Radiobutton(self.radiobuttons_frame, bootstyle='danger',text=translate_notification('Music'),value=self.music,variable=self.loc).pack(padx=(1,105),pady=3)
        self.vid = ttk.Radiobutton(self.radiobuttons_frame, bootstyle='danger',text=translate_notification('Videos'),value=self.videos,variable=self.loc).pack(padx=(1,97),pady=3)
        
        

        
        self.note = ttk.Notebook(self, bootstyle='info')
        self.tab1 = ttk.Frame(self)
        self.tab2 = ttk.Frame(self)
        self.tab3 = ttk.Frame(self)
        self.tab4 = ttk.Frame(self)
        self.tab5 = ttk.Frame(self)

        

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
        self.note.add(self.tab2,text=translate_notification('Youtube Downloads'))
        self.note.add(self.tab3,text=translate_notification('Profile'))
        self.note.add(self.tab4,text=translate_notification("Drag 'n' Drop"))
        self.note.add(self.tab5,text=translate_notification("Phone Link"))
        self.note.pack(fill=tk.BOTH, expand=1)

        
        # Create a context menu
        self.context_menu = ttk.Menu(self.table, tearoff=0)#,activebackground = "#286F63",activeforeground = "#D0FEF7",)
        font = ('Arial',9)
        self.context_menu.add_command(label=translate_notification("Open"),font=font,command=self.open_selected_item)
        self.context_menu.add_command(label=translate_notification("Delete"),font=font,command=self.delete_selected_item)
        self.context_menu.add_command(label=translate_notification("Remove"),font=font,command=self.remove_selected_item)
        self.context_menu.add_command(label=translate_notification("Properties"),font=font,command=self.properties_selected_item)
        

        # Bind right-click event to the Treeview
        self.table.bind("<Button-3>", self.show_context_menu)

        self.transferred_files = []
        self.populateview()
        
        
        # try:
        #     self.them = resource_path2(relative_path='thema.txt')
        #     with open(self.them,'r') as fds:
        #         news = fds.readline()
            
        #     if news == 'darktheme':

        #         self.style_window = Style(theme='darkly')
        #         self.table.tag_configure('evenrow', background='#05060a')#A36D8C
        #         self.table.tag_configure('oddrow', background='#171a2b')#6D73A3
        #     elif news == 'light':
        #         self.style_window = Style(theme=DEFAULT_THEME)
        # except FileNotFoundError:
            
            
        self.style_window = Style(theme=DEFAULT_THEME)

        
        
         
        
        self.config_file = "config.json"
        self.load_configuration()
        self.entries2 = ScrolledFrame(self.tab3,width=1750, autohide=True)
       
        self.entries2.pack(fill='both', side='left', padx=(1, 1), pady=1)

       
        profile_frame_1 = ttk.Frame(self.entries2)
        profile_frame_1.pack()
        
        self.profile_image_label = ttk.Label(profile_frame_1)
        self.profile_image_label.pack(pady=5)

        #Load the profile image from the stored path and create a circular mask
        self.load_profile_image()
        self.create_circular_mask()

        #Create a button to update the profile image
        update_image_button = ttk.Button(profile_frame_1, text="Edit Image", command=self.update_profile_image, width=13, bootstyle='success')
        update_image_button.pack()

        name_frame = ttk.Frame(profile_frame_1)
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
        self.sentnum = ttk.Label(self.entries2,text=f"{self.labelsent} {sent_count}", font=('Arial',8,'bold'))
        self.sentnum.pack(pady=5)
        self.labelreceived = translate_notification("received:") 
        self.receivenum = ttk.Label(self.entries2,text=f'{self.labelreceived} {received_count}', font=('Arial',8,'bold'))
        self.receivenum.pack(pady=5)

        self.sep = ttk.Separator(self.entries2, bootstyle='danger', orient='horizontal')
        self.sep.pack(fill='x',pady=3, padx=50)
        
        
        def generate_tip():
            
            tips = [
                
                ("Tip 1: On your first attempt to transfer files if it doesnt work, please check whether you are connected to the network or not."),
                ("Tip 2: Make sure you regularly check for updates."),
                ("Tip 3: For new users, go to 'Help Menu' and click on 'How To' to know how to send and receive a file."),
                ("Tip 4: If sending a file or receiving a file seems not to work upon all conditions satisfied, go to your task manager, quit the 'ConveTransfer' App and launch it again."),
                ("Tip 5: There a several ways to transfer files. Try the main 'Send' button, the 'Drag 'n' Drop' tab or via the 'Profile' tab."),
                ("Tip 6: A receiver can send files via the 'Profile' tab without having to type in the sender's ip address in the 'IP' field."),
                ("Tip 7: To change language, go to the 'Help' menu, click on 'Languages' and select the language of your choice.")


            ]
            return random.choice(tips)

        
        def show_tip():
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
            tip = generate_tip()
            translate_message_box("Tip of the Day",tip)
        self.after(4000, show_tip)
        

        
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

        def show_images_in_rows(image_paths, images_per_row=4):
            row_frame = None

            for i, image_path in enumerate(image_paths):
                if i % images_per_row == 0:
                    if row_frame is not None:
                        row_frame.pack(fill='x', padx=10, pady=5)
                    row_frame = ttk.Frame(self.entries2)
                    row_frame.pack(fill='x', padx=10, pady=5)

                # previ = ttk.Label(row_frame, text='Previous Contacts', font=('Arial',12,'italic'))#, foreground='#8557a8')
                # previ.pack()
                img = create_circular_image(image_path)
                img_tk = ImageTk.PhotoImage(img)
                label_pic = ttk.Label(row_frame, image=img_tk)
                label_pic.image = img_tk
                label_pic.pack(side='left', padx=5)
                button_pic = ImageTk.PhotoImage(Image.open(resource_path2(relative_path='images/sent.png')))
                self.button_pic = ttk.Button(row_frame, image=button_pic, command=self.send_by_profile(image_path), bootstyle='T.Link')
                self.button_pic.pack(side='left', padx=5)
                self.button_pic.image = button_pic

            if row_frame is not None:
                row_frame.pack(fill='x', padx=10, pady=5)

        # directory = "C:/Users/DELL/Desktop/pics/"  # Replace with your image directory path
        # image_paths = get_image_paths(directory)
        # print(image_paths)
        # show_images_in_rows(image_paths)

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
        
 


        
        youtube_tab(self)
        #ttk.Frame(self.tab4, width=500, border=15,padding=65).pack()
        dragg_frame = ttk.Frame(self.tab4, width=480, height=540)#relief='raised', bootstyle='secondary')
        dragg_frame.pack(fill='both',ipadx=130, padx=40, pady=20,ipady=400)
        
        plus_label = ttk.Label(dragg_frame, text='+', font=('bold',24))
        plus_label.pack(anchor='center',padx=100,pady=160)

        # Add a Label with the drag and drop text
        drag_label = ttk.Label(dragg_frame, text=translate_notification('Drag and drop to transfer files'), font=('Helvetica',12))
        drag_label.pack(anchor='center',padx=100)
        dragg_frame.drop_target_register(DND_ALL)
        dragg_frame.dnd_bind("<<Drop>>", self.get_path)
        
        Phonelink(self)
       



    # def on_resize(self,event):
    #     width = self.winfo_width()
    #     height = self.winfo_height()
    #     print(f"Window size is {width} x {height}")   
  
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
        try:
            image = Image.open(self.profile_image_path)
            image.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            self.profile_image_path = resource_path2(relative_path="images/default.png")
            image = Image.open(self.profile_image_path)
            image.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(image)

        self.profile_image_label.config(image=photo)
        self.profile_image_label.image = photo

    def create_circular_mask(self):
        # Load the profile image
        try:

            image = Image.open(self.profile_image_path)
            image = image.convert("RGBA")
        except FileNotFoundError:
           self.profile_image_path = resource_path2(relative_path="images/default.png")
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
    
    from table_options import show_context_menu, delete_selected_item, open_selected_item 
    from table_options import remove_selected_item, properties_selected_item
    
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
        self.update_button.configure(state='disabled')
            
    def enable_buttons(self):
        self.select_button.configure(state='normal')
        self.receive_button.configure(state='normal')
        self.update_button.configure(state='normal')

    
    def stop_enable(self):
        
        self.stop_button.configure(state='normal')
        
    def stop_disable(self):
        
        self.stop_button.configure(state='disabled')

    # def open_file_dialog(self):
    #     file_paths = filedialog.askopenfilenames()
    #     self.send_files(file_paths)

    # def send_files(self,file_paths):
    #     self.HOST = self.host.get()
    #     self.PORT = self.port.get()
    #     self.PORT = 4444
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    #         client_socket.connect((self.HOST, self.PORT))
    #         for file_path in file_paths:
    #             filename = os.path.basename(file_path)
    #             filesize = os.path.getsize(file_path)
    #             client_socket.send(f"{filename},{filesize}".encode())
    #             with open(file_path, "rb") as f:
    #                 while True:
    #                     data = f.read(1024)
    #                     if not data:
    #                         break
    #                     client_socket.send(data)
    #             print(f"Sent {filename}")
    #         print("File transfer completed.")
    from dragndrop import get_path

    def translate_notification(self,message_key):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(message_key, message_key)
    chunk = 65536

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
            info12 = self.translate_notification("It seems your selection was empty")
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
                        self.data = self.file.read(self.chunk)
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
                            
                            self.data = self.file.read(self.chunk)
                            
                    print("File sent successfully.")
                    
                    self.send_file_count += 1
                    

                    
                    info1 = self.translate_notification("sent successfully")
                    self.message = ToastNotification(title='Response',alert=True,message=f'{self.filename} {info1}',duration=3000,bootstyle='success')
                    self.message.show_toast()


                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    max_filename_length = 200  # Adjust this value as needed
                    displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')
                    #displayed_filename = self.filename
                    self.transferred_files.append((f"{displayed_filename}",f"{current_time}",f"{formatted_size}"))
                    #self.table.delete(*self.table.get_children())
                    for idx, data in enumerate(self.transferred_files):
                        tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
                    self.table.insert("", 0, values=(f"{displayed_filename}",f"{current_time}",f"{formatted_size}"),tags=(tag,))
                    connection.insert_sent_file(displayed_filename, current_time, formatted_size, self.filepath)
                    
                
                    
                    
                    

                    

            except Exception as e:
                #print(f'This is the reason {e}')
                if self.HOST == '':
                    info2 = self.translate_notification("The IP can't be empty")
                    self.message = ToastNotification(title='Response',alert=True,message=f'{info2}',duration=3000,bootstyle='danger')
                    self.message.show_toast()
                # elif self.HOST == self.wifi:
                #     info3 = translate_notification("Please use the receiver's IP not your IP")
                #     self.message = ToastNotification(title='Response',alert=True,message=info3,duration=3000,bootstyle='danger')
                #     self.message.show_toast()
                elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                    info4 = self.translate_notification("is a wrong IP address format")
                    self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info4}',duration=3000,bootstyle='danger')
                    self.message.show_toast()
                elif len(self.HOST) > 15 or len(self.HOST) < 8:
                    info5 = self.translate_notification("is not Valid IP")
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
        
        
        def receive_thread(): 
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.server_socket:
                try:
                    self.HOST = self.host.get()
                    self.PORT = self.port.get()
                    self.HOST = str(self.HOST) 
                    self.PORT = int(self.PORT)
                    self.folder_name = self.folder_nam.get()
                    self.des = self.loc.get()
                    self.doc = self.loc.get()
                    self.vid = self.loc.get()
                    self.mus = self.loc.get()
                    self.pic = self.loc.get()
                    self.dow = self.loc.get()
                   
                
                    all_loc = [self.des, self.doc, self.vid, self.mus, self.pic, self.dow]
                    if all(location == '' for location in all_loc) and self.folder_name == '':
                        info1 = self.translate_notification("The Receive Path must be selected at least")
                        self.message = ToastNotification(title='Response', alert=True, message=info1, duration=3000, bootstyle='warning')
                        self.message.show_toast()
                        return
                    
                    folder_exist = any(os.path.exists(os.path.join(location, self.folder_name)) for location in all_loc)

                    if not folder_exist:
                        f1 = self.translate_notification('The folder')
                        f2 = self.translate_notification("doesn't exist in any specified Receive Path")
                        info2 = f" {f1} '{self.folder_name}' {f2}"
                        self.message = ToastNotification(title='Response', alert=True, message=info2, duration=3000, bootstyle='warning')
                        self.message.show_toast()
                        return
                    else:
                    
                        for i in all_loc:
                            if i == self.des and self.folder_name != '':
                                self.final_folder = os.path.join(self.des, self.folder_name)
                            elif i == self.des and self.folder_name == '':
                                self.final_folder = self.des
                            elif i == self.doc and self.folder_name != '':
                                self.final_folder = os.path.join(self.doc, self.folder_name)
                            elif i == self.doc and self.folder_name == '':
                                self.final_folder = self.doc
                            elif i == self.vid and self.folder_name != '':
                                self.final_folder = os.path.join(self.vid, self.folder_name)
                            elif i == self.vid and self.folder_name == '':
                                self.final_folder = self.vid
                            elif i == self.pic and self.folder_name != '':
                                self.final_folder = os.path.join(self.pic, self.folder_name)
                            elif i == self.pic and self.folder_name == '':
                                self.final_folder = self.pic
                            elif i == self.dow and self.folder_name != '':
                                self.final_folder = os.path.join(self.dow, self.folder_name)
                            elif i == self.dow and self.folder_name == '':
                                self.final_folder = self.dow
                            elif i == self.mus and self.folder_name != '':
                                self.final_folder = os.path.join(self.mus, self.folder_name)
                            elif i == self.mus and self.folder_name == '':
                                self.final_folder = self.mus
                       
                    # if not os.path.exists(self.default_loc) or not os.path.isdir(self.default_loc):
                    #     info2 = "The specified receiving directory does not exist or is not valid"
                    #     self.message = ToastNotification(title='Response', alert=True, message=info2, duration=3000, bootstyle='warning')
                    #     self.message.show_toast()
                    #     return    

                
                    # if self.folder_name == '':
                    #     info1 = "The Receiving Dir path is not specified"
                    #     self.message = ToastNotification(title='Response',alert=True,message=info1,duration=3000,bootstyle='warning')
                    #     self.message.show_toast()
                    
                        
                    #else: 
                    
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
                    progress_window = ProgressWindow(self, total_size)

                    
                    self.file_path = os.path.join(self.final_folder, self.filename)
                    filee = self.file_path
                    with open(self.file_path, 'wb') as file:
                        received_bytes = 0
                        data = self.conn.recv(self.chunk)
                        while data:
                            if self.stop_receive:
                                break
                            file.write(data)
                            received_bytes += len(data)
                            progress = (received_bytes / total_size) * 100
                            progress_window.progress_bar['value'] = received_bytes
                            self.update_idletasks()  # Update receiving progress
                            self.t_time.configure(text=f"{int(progress)}% ")
                            data = self.conn.recv(self.chunk)
                            
                    self.receive_file_count += 1
                                          
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    max_filename_length = 200  # Adjust this value as needed
                    displayed_filename = self.filename[:max_filename_length] + (self.filename[max_filename_length:] and '...')

                    self.transferred_files.append(("",f"{current_time}",f"{formatted_size}",f"{displayed_filename}"))
                    #self.table.delete(*self.table.get_children())
                    for idx, data in enumerate(self.transferred_files):
                        tag = 'evenrow' if idx % 2 == 0 else 'oddrow'

                    self.table.insert("", 0, values=("", current_time, formatted_size, displayed_filename),tags=(tag,))
                    connection.insert_received_file(displayed_filename, current_time, formatted_size, filee)
                    print(self.file_path)
                        
                    if not self.stop_receive:
                        #print(f"File '{self.filename}' received and saved successfully.")
                        info1 = self.translate_notification("received successfully")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.filename} {info1}',duration=3000,bootstyle='success')
                        self.message.show_toast()
                        # Destroy the progress window
                        progress_window.destroy()
                    else:
                        print("Transfer stopped by user.")
                    
                    
                    
                      
                        
                    
                except:
                    if self.HOST == '':
                        info2 = self.translate_notification("The IP can't be empty")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{info2}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                    # elif self.HOST != self.wifi:
                    #     info3 = self.translate_notification("Please use your IP")
                    #     self.message = ToastNotification(title='Response',alert=True,message=f'{info3} {self.wifi}',duration=3000,bootstyle='danger')
                    #     self.message.show_toast()
                    elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                        info4 = self.translate_notification("is a wrong IP address format")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info4}',duration=3000,bootstyle='warning')
                        self.message.show_toast()
                    elif len(self.HOST) > 15 or len(self.HOST) < 8:
                        info5 = self.translate_notification("is not Valid IP")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info5}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                    # elif self.folder_name == '':
                    #     info1 = "The Receiving Dir path is not specified"
                    #     self.message = ToastNotification(title='Response',alert=True,message=info1,duration=3000,bootstyle='warning')
                    #     self.message.show_toast()
                    
                finally:
                    
                    self.enable_buttons()
                    self.t_time.configure(text='')
            #self.server_socket.close()

                    
        threading.Thread(target=receive_thread).start()
        if self.receive_file_count == 4:
            threading.Thread(target=self.receive_image).start()    
        
        
        
    from send_receive_image import send_image
    from send_receive_image import receive_image
    

    
    

    
    
    
    def send_by_profile(self,image_path):
        def on_button_click():
            self.disable_buttons()

            self.filepath = filedialog.askopenfilename()
            self.filename = os.path.basename(self.filepath)

            self.HOST = os.path.splitext(os.path.basename(image_path))[0]

            
            self.PORT = 4444
            

            self.send_stop = False
            
            try:
                total_size = os.path.getsize(self.filepath)
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
                self.stop_enable()
            except:
                
                                
                #self.message = Messagebox.show_info('Response', "It seems your selection was empty")
                info12 = self.translate_notification("It seems your selection was empty")
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
                        self.button_pic.configure(state='disabled')
                        
                        with open(self.filepath, 'rb') as self.file:
                            self.data = self.file.read(self.chunk)
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
                                
                                self.data = self.file.read(self.chunk)
                                
                        print("File sent successfully.")
                        
                        self.send_file_count += 1
                        

                        
                        info1 = self.translate_notification("sent successfully")
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
                        connection.insert_sent_file(displayed_filename, current_time, formatted_size, self.filepath)
                    
                        
                        
                        

                        

                except Exception as e:
                    #print(f'This is the reason {e}')
                    if self.HOST == '':
                        info2 = self.translate_notification("The IP can't be empty")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{info2}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                    # elif self.HOST == self.wifi:
                    #     info3 = translate_notification("Please use the receiver's IP not your IP")
                    #     self.message = ToastNotification(title='Response',alert=True,message=info3,duration=3000,bootstyle='danger')
                    #     self.message.show_toast()
                    elif any(c.isalpha() or c in "!@#$%^&*()_=[]:;?/><+-|" for c in self.HOST):
                        info4 = self.translate_notification("is a wrong IP address format")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info4}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                    elif len(self.HOST) > 15 or len(self.HOST) < 8:
                        info5 = self.translate_notification("is not Valid IP")
                        self.message = ToastNotification(title='Response',alert=True,message=f'{self.HOST}{info5}',duration=3000,bootstyle='danger')
                        self.message.show_toast()
                finally:
                    # Destroy the progress window
                    progress_window.destroy()
                    # Reactivate the button once cdthe event is completed or an error occurs
                    
                    self.enable_buttons()
                    self.button_pic.configure(state='normal')
                    self.stop_disable()
                    self.t_time.configure(text='')
                    
                
                    

            # Start the file transfer in a separate thread
            threading.Thread(target=transfer_file).start()
        return on_button_click


if __name__ == "__main__":
    root = Root()
    root.mainloop()
