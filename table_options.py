import connection
from ttkbootstrap.toast import ToastNotification
import os
from tkinter import messagebox
from resourcepath import resource_path2, resource_path
import ttkbootstrap as ttk
from PIL import Image, ImageOps, ImageTk
from tkinter import PhotoImage
def show_context_menu(self, event):
    item = self.table.identify_row(event.y)
    if item:
        self.table.selection_set(item)
        self.context_menu.post(event.x_root, event.y_root)

# def open_selected_item(self):
#     def translate_notification(message_key):
#         if self.current_language in self.translations:
#             translation_dict = self.translations[self.current_language]
#         else:
#             translation_dict = self.translations['en']  # Fallback to English if the language is not found
#         return translation_dict.get(message_key, message_key)
#     selected_item = self.table.selection()
#     if selected_item:
#         transferred_files = connection.get_files()
        

#         for record in transferred_files:
#             sent, date, size, received, sent_location, received_location = record
#             if sent == self.table.item(selected_item)["values"][0]:
#                 # You've found the selected sent file
#                 sent_location = sent_location
#                 filename = self.table.item(selected_item)["values"][0]
#                 datetime = self.table.item(selected_item)["values"][1]
#                 size = self.table.item(selected_item)["values"][2]
#                 os.startfile(os.path.abspath(sent_location))
            
#             # elif received == self.table.item(selected_item)["values"][3]:
#             #     received_location = received_location
#             #     filename = self.table.item(selected_item)["values"][3]
#             #     datetime = self.table.item(selected_item)["values"][2]
#             #     size = self.table.item(selected_item)["values"][1]
#             #     os.startfile(os.path.abspath(received_location))



def open_selected_item(self):
    def translate_notification(message_key):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(message_key, message_key)

    selected_item = self.table.selection()
    if selected_item:
        transferred_files = connection.get_files()

        for record in transferred_files:
            sent, date, size, received, sent_location, received_location = record
            try:
                if (sent and sent == self.table.item(selected_item)["values"][0]) or (received and received == self.table.item(selected_item)["values"][3]):
                    file_location = sent_location if sent else received_location
                    filename = self.table.item(selected_item)["values"][0] if sent else self.table.item(selected_item)["values"][3]
                    print(file_location)
                    print(filename)
                    os.startfile(os.path.abspath(file_location))
                    break
                
            except IndexError:
                pass
            except FileNotFoundError:
                message = translate_notification('file not found or has been moved.')
                self.message = ToastNotification(title='Response', message=f'{filename} {message}',duration=3000,alert=True,bootstyle='success')
                self.message.show_toast()
           

def delete_selected_item(self):
    def translate_notification(message_key):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(message_key, message_key)

    selected_item = self.table.selection()
    
    if selected_item:
        # Get the location of the selected item and display it
        # You can use self.table.item(selected_item)["values"] to access the data
        #location = self.table.item(selected_item)["values"][3]  # Assuming "received" contains the location
        #try:
        filename = self.table.item(selected_item)["values"][0] or self.table.item(selected_item)["values"][3]
        datetime = self.table.item(selected_item)["values"][1] or self.table.item(selected_item)["values"][2]
        size = self.table.item(selected_item)["values"][2] or self.table.item(selected_item)["values"][1]
        
        if connection.delete_item(filename, datetime, size):
            self.table.delete(selected_item)
            message = translate_notification('has been deleted')
            self.message = ToastNotification(title='Response',message=f'{filename} {message}',duration=3000,alert=True,bootstyle='success')
            self.message.show_toast()
            connection.delete_item_rec(filename, datetime, size)
            message = translate_notification('has been deleted')
            self.message = ToastNotification(title='Response',message=f'{filename} {message}',duration=3000,alert=True,bootstyle='success')
            self.message.show_toast()
           
        else:
            self.message = ToastNotification(title='Response',message=translate_notification(f'Unable to delete {filename}'),duration=3000,alert=True,bootstyle='danger')
            self.message.show_toast()
            connection.get_sent_received_counts()


def remove_selected_item(self):
    def translate_notification(message_key):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(message_key, message_key)

    selected_item = self.table.selection()
    message_ico = resource_path(relative_path='images/unt.ico')
    self.iconbitmap(default=message_ico)
    message = translate_notification('Do you want to completely delete the file?')
    mb1 = messagebox.askyesno(title='Response',message=message)
    if mb1 is True:
    
        if selected_item:
            
            transferred_files = connection.get_files()
            for record in transferred_files:
                sent, date, size, received, sent_location, received_location = record
                try:
                    if (sent and sent == self.table.item(selected_item)["values"][0]) or (received and received == self.table.item(selected_item)["values"][3]):
                        file_location = sent_location if sent else received_location
                        filename = self.table.item(selected_item)["values"][0] if sent else self.table.item(selected_item)["values"][3]
                        datetime = self.table.item(selected_item)["values"][1] or self.table.item(selected_item)["values"][2]
                        if connection.delete_item(filename, datetime, size):
                            self.table.delete(selected_item)
                            connection.delete_item_rec(filename, datetime, size)
                        os.remove(os.path.abspath(file_location))
                        message = translate_notification('has been removed completely.')
                        self.message = ToastNotification(title='Response', message=f'{filename} {message}',duration=3000,alert=True,bootstyle='success')
                        self.message.show_toast()
                        break
                
                except FileNotFoundError:
                    
                    message = translate_notification('file not found or has been moved.')
                    self.message = ToastNotification(title='Response', message=f'{filename} {message}',duration=3000,alert=True,bootstyle='success')
                    self.message.show_toast()

            
            else:
                # self.message = ToastNotification(title='Response',message=translate_notification(f'Unable to delete {filename}'),duration=3000,alert=True,bootstyle='danger')
                # self.message.show_toast()
                connection.get_sent_received_counts()
                pass
    else:
        pass



def properties_selected_item(self):
    def translate_notification(message_key):
        if self.current_language in self.translations:
            translation_dict = self.translations[self.current_language]
        else:
            translation_dict = self.translations['en']  # Fallback to English if the language is not found
        return translation_dict.get(message_key, message_key)

    selected_item = self.table.selection()
    if selected_item:
        transferred_files = connection.get_files()

        for record in transferred_files:
            sent, date, size, received, sent_location, received_location = record
            try:
                if (sent and sent == self.table.item(selected_item)["values"][0]) or (received and received == self.table.item(selected_item)["values"][3]):
                    file_location = sent_location if sent else received_location
                    filename = self.table.item(selected_item)["values"][0] if sent else self.table.item(selected_item)["values"][3]
                    sized = self.table.item(selected_item)["values"][2] if sent else self.table.item(selected_item)["values"][2]
                
                    class display(ttk.Toplevel):
                        def __init__(self,extt):
                            ttk.Toplevel.__init__(self)
                            #self.transient(parent)
                    
                            self.grab_set()
                            w = 785
                            h = 520
                    
                            sw = self.winfo_screenwidth()
                            sh = self.winfo_screenheight()
                            x = (sw - w) / 2
                            y = (sh - h) / 2
                            self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
                            self.icon = resource_path(relative_path='images/unt.ico')
                            self.iconbitmap(self.icon)
                            self.resizable(False,False)
                            self.title(translate_notification('File Properties'))
                            # Filename and image frame
                            filename_label = ttk.Frame(self, borderwidth=10)
                            filename_label.pack(fill='x',pady=4)
                            # for ext in ['.png', '.jpg', '.jpeg']:
                            extt = os.path.splitext(os.path.basename(filename))[1]
                            
                            

                            # Define a dictionary to map file extensions to image paths
                            extension_image_map = {
                                '.png': 'png_file.png',
                                '.jpg': 'jpg_file.png',
                                '.pdf': 'pdf_file.png',
                                '.mp3': 'mp3_file.png',
                                '.mp4': 'mp4_file.png',
                                '.mkv': 'mkv_file.png',
                                '.wmv': 'wmv_file.png',
                                '.mov': 'mov_file.png',
                                '.csv': 'csv_file.png',
                                '.doc': 'doc_file.png',
                                '.docx': 'docx_file.png',
                                '.tex': 'tex_file.png',
                                '.xlsx': 'excel_file.png',
                                '.xls': 'xls_file.png',
                                '.pptx': 'pptx_file.png',
                                '.ppt': 'ppt_file.png',
                                '.zip': 'zip_file.png',
                                '.iso': 'iso_file.png',
                                '.exe': 'exe_file.png',
                                '.txt': 'txt_file.png',
                            }

                            # Get the image path based on the file extension
                            image_path = extension_image_map.get(extt)

                            if image_path:
                                self.image = Image.open(resource_path2(relative_path=f'images/{image_path}'))
                                self.size = (100, 100)
                                self.thumb = ImageOps.fit(self.image, self.size)
                                self.file_image = ImageTk.PhotoImage(self.thumb)
                            else:
                                self.image = Image.open(resource_path2(relative_path='images/unknown.png'))
                                self.size = (100, 100)
                                self.thumb = ImageOps.fit(self.image, self.size)
                                self.file_image = ImageTk.PhotoImage(self.thumb)  


                            filename_label = ttk.Frame(self)
                            filename_label.pack(padx=10, pady=(10, 0))
                            filename_image = ttk.Label(filename_label, image=self.file_image)
                            filename_image.pack(side='left', padx=(5,10))
                            filename_prop = ttk.Label(filename_label, text=f'{translate_notification("File")}: {filename}')
                            filename_prop.pack(side='left')
                            self.sep = ttk.Separator(self, orient='horizontal')
                            self.sep.pack(fill='x',pady=3, padx=50)
                            
                            tss_frame = ttk.Frame(self)
                            tss_frame.pack(padx=10, pady=(10, 0))
                            ttype = translate_notification('Type')
                            type_label = ttk.Label(tss_frame,text=f'{ttype} {extt}', font=('Arial',8,'bold'))
                            type_label.pack(pady=5)

                            ssize = translate_notification('Size')
                            size_label = ttk.Label(tss_frame, text=f'{ssize} {sized}', font=('Arial',8,'bold'))
                            size_label.pack(pady=5)
                            directory_path = os.path.dirname(file_location)
                            
                            fl = translate_notification('File Location:')
                            saved_to = ttk.Label(self, text= f'{fl} {directory_path}',font=('Arial',8,'bold'))
                            saved_to.pack(padx=(2, 10),pady=5)
                    
                    
                    extt = ['.png','.mp3','.jpeg','.mp4',
                            '.jpg','.pdf','.doc','.docx',
                            '.csv','.xlsx','.pptx','.zip',
                            '.exe','.iso','.txt','.wmv',
                            '.tex','.xls','.ppt'
                            ]
                    display(extt=extt)
                    break
            except IndexError:
                pass
            except FileNotFoundError:
                message = translate_notification('file not found or has been moved.')
                self.message = ToastNotification(title='Response', message=f'{filename} {message}',duration=3000,alert=True,bootstyle='success')
                self.message.show_toast()