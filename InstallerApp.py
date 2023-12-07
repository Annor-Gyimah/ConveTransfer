# import tempfile
# import win32api
# import os
# import tkinter as tk
# from tkinter import messagebox
# from metadata import __AppName__
# from metadata import __version__
# import time

# exe_directory = os.path.expanduser(f'~\\AppData\\Local\\convetransfer\\')


# def install_update():
#     tmp = tempfile.gettempdir()
#     updated_file_path = f'{tmp}/{__AppName__}.exe'
#     print(updated_file_path)

#     # Assuming the .exe file has the same name as __AppName__.exe
#     destination_directory = exe_directory
#     destination_path = os.path.join(destination_directory, f'{__AppName__}.exe')

#     try:
#         win32api.CopyFile(updated_file_path, destination_path, 0)  # 0 flag for normal copy
#         messagebox.showinfo("Update Installed", "Update installed successfully!")
#     except Exception as e:
#         print(f"Error copying file: {e}")
#         messagebox.showerror("Error", f"Error installing update: {e}")


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window

#     def ask_install_update():
#         result = messagebox.askquestion("Install Update", "Do you want to install the update?")
#         if result == "yes":
#             install_update()
#             time.sleep(5)
#             root.destroy()
#         else:
#             root.destroy()

#     ask_install_update()
#     root.mainloop()
import tempfile
import win32api
import os
import tkinter as tk
from tkinter import messagebox
from metadata import __AppName__
from metadata import __version__
import time
import psutil

exe_directory = os.path.expanduser(f'~\\AppData\\Local\\convetransfer\\')


def install_update():
    tmp = tempfile.gettempdir()
    updated_file_path = f'{tmp}/{__AppName__}.exe'
    print(updated_file_path)

    # Assuming the .exe file has the same name as __AppName__.exe
    destination_directory = exe_directory
    destination_path = os.path.join(destination_directory, f'{__AppName__}.exe')

    try:
        # Terminate ConveTransfer process
        terminate_convetransfer()

        # Copy the updated file
        win32api.CopyFile(updated_file_path, destination_path, 0)  # 0 flag for normal copy
        messagebox.showinfo("Update Installed", "Update installed successfully!")

    except Exception as e:
        print(f"Error copying file: {e}")
        messagebox.showerror("Error", f"Error installing update: {e}")


def terminate_convetransfer():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'ConveTransfer.exe':
            try:
                pid = process.info['pid']
                p = psutil.Process(pid)
                p.terminate()
                p.wait(timeout=5)
            except psutil.NoSuchProcess:
                pass
            except psutil.TimeoutExpired:
                p.kill()
                p.wait()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    def ask_install_update():
        result = messagebox.askquestion("Install Update", "Do you want to install the updates?")
        if result == "yes":
            install_update()
            time.sleep(2)
            tmp = os.path.expanduser(f'~\\AppData\Local\\convetransfer\\')
            win32api.ShellExecute(0, 'open', f'{tmp}\\{__AppName__}.exe', None, None, 10)
            root.destroy()
        else:
            root.destroy()

    ask_install_update()
    root.mainloop()
