# import socket
# import os
# import get_ip
# import json
# from resourcepath import resource_path2
# from wifi_name import get_wifi_ssid
# def send_image(self):
#     self.HOST = self.host.get()
#     self.PORT = 8080
#     ip_addr = ""  # Initialize ip_addr with an empty string
    
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((self.HOST, self.PORT))

#         ip_addr1 = get_ip.get_ip('wlan0')
#         try:
#             with open('config.json') as fj:
#                 con = json.load(fj)
#             img = con.get('profile_image', '')
#             if os.path.exists(img):
#                 imga = os.path.basename(img)
#                 if imga.endswith('.png'):
#                     ip_addr = f"{ip_addr1}.png"
#                 elif imga.endswith('.jpg'):
#                     ip_addr = f"{ip_addr1}.jpg"
#                 elif imga.endswith('.jpeg'):
#                     ip_addr = f"{ip_addr1}.jpeg"
#             # Encode the filename as bytes before sending
#             client_socket.sendall(ip_addr.encode())        
#             print(f"ip_addr: {ip_addr}")
#         except FileNotFoundError:
#             img = resource_path2(relative_path="images/default.png")
#             ip_addr = f"{ip_addr1}.png"
#             # Encode the filename as bytes before sending
#             client_socket.sendall(ip_addr.encode())

        
        
#         print(f"ip_addr1: {ip_addr1}")

#         with open(img, "rb") as f:
#             while True:
#                 data = f.read(1024)
#                 if not data:
#                     break
#                 client_socket.send(data)
#         print(f"Sent {img}")
#     print("File transfer completed.")


    

# def receive_image(self):
    
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        
#         self.PORT = 8080
#         server_socket.bind((self.HOST, self.PORT))
#         server_socket.listen()
        
#         conn, addr = server_socket.accept()

#         filename_e = conn.recv(1024).decode('utf-8')
        
        
        
#         wifinam = get_wifi_ssid()
#         if wifinam is None:
#             # Set a default folder name when the SSID is not available
#             folder = 'ips/default'
#         else:
#             folder = f'ips/{wifinam}'

#         if not os.path.exists(folder):
#             os.makedirs(folder)

#         # Extract the filename without the extension
#         filename_base, file_extension = os.path.splitext(filename_e)
        
#         # Construct the full file path using the filename without extension
#         old_filename = os.path.join(folder, filename_base)
#         print(old_filename)
#         new_filename = os.path.join(folder,filename_e)
#         print(new_filename)

#         # Remove existing files with different extensions but the same base filename
#         for ext in ['.png', '.jpg', '.jpeg']:
#             existing_file = old_filename + ext
#             print(existing_file)
#             if os.path.exists(existing_file):
#                 os.remove(existing_file)


#         with open(new_filename, 'wb') as file:
#             data = conn.recv(1024)
#             while data:
#                 file.write(data)
#                 data = conn.recv(1024)
#         server_socket.close()      

import socket
import os
import get_ip
import json
from resourcepath import resource_path2
from wifi_name import get_wifi_ssid
def send_image(self):
    self.HOST = self.host.get()
    self.PORT = 8080
    ip_addr = ""  # Initialize ip_addr with an empty string
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((self.HOST, self.PORT))

        ip_addr1 = socket.gethostname()
        try:
            with open('config.json') as fj:
                con = json.load(fj)
            img = con.get('profile_image', '')
            if os.path.exists(img):
                imga = os.path.basename(img)
                if imga.endswith('.png'):
                    ip_addr = f"{ip_addr1}.png"
                elif imga.endswith('.jpg'):
                    ip_addr = f"{ip_addr1}.jpg"
                elif imga.endswith('.jpeg'):
                    ip_addr = f"{ip_addr1}.jpeg"
            # Encode the filename as bytes before sending
            client_socket.sendall(ip_addr.encode())        
            print(f"ip_addr: {ip_addr}")
        except FileNotFoundError:
            img = resource_path2(relative_path="images/default.png")
            ip_addr = f"{ip_addr1}.png"
            # Encode the filename as bytes before sending
            client_socket.sendall(ip_addr.encode())

        
        
        print(f"ip_addr1: {ip_addr1}")

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
        
        self.PORT = 8080
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen()
        
        conn, addr = server_socket.accept()

        filename_e = conn.recv(1024).decode('utf-8')
        
        
        
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
        print(old_filename)
        new_filename = os.path.join(folder,filename_e)
        print(new_filename)

        # Remove existing files with different extensions but the same base filename
        for ext in ['.png', '.jpg', '.jpeg']:
            existing_file = old_filename + ext
            print(existing_file)
            if os.path.exists(existing_file):
                os.remove(existing_file)


        with open(new_filename, 'wb') as file:
            data = conn.recv(1024)
            while data:
                file.write(data)
                data = conn.recv(1024)
        server_socket.close()      