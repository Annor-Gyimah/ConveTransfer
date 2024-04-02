import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from progresswin import ProgressWindow
import socket
import connection
import datetime
import threading

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
def get_path(self, event):
    self.disable_buttons()
    self.filepath = event.data.replace("{","").replace("}", "")
    self.filename = os.path.basename(self.filepath)
    #print(self.filename)

    
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
        info12 = translate_notification("Drag and drop currently support only one file transfer")
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
                    self.data = self.file.read(65536)
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
                        
                        self.data = self.file.read(65536)
                        
                print("File sent successfully.")
                
                self.send_file_count += 1
                

                
                info1 = translate_notification("sent successfully")
                self.message = ToastNotification(title='Response',alert=True,message=f'{self.filename}{info1}',duration=3000,bootstyle='success')
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