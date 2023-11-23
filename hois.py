import tkinter as tk
import subprocess, os, sys

def start_server():
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    add = resource_path(relative_path='your_server_script.py')

    try:
        # Use subprocess to start the server in a new console window
        subprocess.Popen(["start", "cmd", "/k", "python", f"{add}"], shell=True)
    except Exception as e:
        print(f"Error starting server: {e}")

# Create your Tkinter window
root = tk.Tk()

# Create a button to start the server
start_button = tk.Button(root, text="Start Server", command=start_server)
start_button.pack()

# Run the Tkinter event loop
root.mainloop()
