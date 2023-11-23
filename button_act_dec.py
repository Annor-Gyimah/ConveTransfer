
# # import os
# # import glob
# # import shutil

# # # dictionary mapping each extension with its corresponding folder
# # # For example, 'jpg', 'png', 'ico', 'gif', 'svg' files will be moved to 'images' folder
# # # feel free to change based on your needs
# # extensions = {
# #     "jpg": "images",
# #     "png": "images",
# #     "ico": "images",
# #     "gif": "images",
# #     "svg": "images",
# #     "png": "images",
# #     "sql": "sql",
# #     "exe": "programs",
# #     "msi": "programs",
# #     "pdf": "pdf",
# #     "xlsx": "excel",
# #     "csv": "excel",
# #     "rar": "archive",
# #     "zip": "archive",
# #     "gz": "archive",
# #     "tar": "archive",
# #     "docx": "word",
# #     "torrent": "torrent",
# #     "txt": "text",
# #     "ipynb": "python",
# #     "py": "python",
# #     "pptx": "powerpoint",
# #     "ppt": "powerpoint",
# #     "mp3": "audio",
# #     "wav": "audio",
# #     "mp4": "video",
# #     "m3u8": "video",
# #     "webm": "video",
# #     "ts": "video",
# #     "json": "json",
# #     "css": "web",
# #     "js": "web",
# #     "html": "web",
# #     "apk": "apk",
# #     "sqlite3": "sqlite3",
# # }


# # if __name__ == "__main__":
# #     path = r"C:Users\\DELL\\Desktop"
# #     # setting verbose to 1 (or True) will show all file moves
# #     # setting verbose to 0 (or False) will show basic necessary info
# #     verbose = 1
# #     for extension, folder_name in extensions.items():
# #         # get all the files matching the extension
# #         files = glob.glob(os.path.join(path, f"*.{extension}"))
# #         print(f"[*] Found {len(files)} files with {extension} extension")
# #         # if not os.path.isdir(os.path.join(path, folder_name)) and files:
# #         #     # create the folder if it does not exist before
# #         #     print(f"[+] Making {folder_name} folder")
# #         #     os.mkdir(os.path.join(path, folder_name))
# #         # for file in files:
# #         #     # for each file in that extension, move it to the correponding folder
# #         #     basename = os.path.basename(file)
# #         #     dst = os.path.join(path, folder_name, basename)
# #         #     if verbose:
# #         #         print(f"[*] Moving {file} to {dst}")
# #         #     shutil.move(file, dst)

# import tkinter as tk
# from tkinter import filedialog

# def open_file_explorer():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         label.config(text="Selected File: " + file_path)

# root = tk.Tk()
# root.title("File Explorer")

# frame = tk.Frame(root)
# frame.pack(pady=20)

# open_button = tk.Button(frame, text="Open File", command=open_file_explorer)
# open_button.pack()

# label = tk.Label(frame, text="")
# label.pack()

# root.mainloop()

# importing the required modules  
from tkinter import *                   # importing all the widgets and modules from tkinter  
from tkinter import messagebox as mb    # importing the messagebox module from tkinter  
from tkinter import filedialog as fd    # importing the filedialog module from tkinter  
import os                               # importing the os module  
import shutil                           # importing the shutil module  
  
# ----------------- defining functions -----------------  
# function to open a file  
def openFile():  
   # selecting the file using the askopenfilename() method of filedialog  
   the_file = fd.askopenfilename(  
      title = "Select a file of any type",  
      filetypes = [("All files", "*.*")]  
      )  
   # opening a file using the startfile() method of the os module  
   os.startfile(os.path.abspath(the_file))  
  
# function to copy a file  
def copyFile():  
   # using the filedialog's askopenfilename() method to select the file  
   fileToCopy = fd.askopenfilename(  
      title = "Select a file to copy",  
      filetypes=[("All files", "*.*")]  
      )  
   # using the filedialog's askdirectory() method to select the directory  
   directoryToPaste = fd.askdirectory(title = "Select the folder to paste the file")  
  
   # using the try-except method  
   try:  
      # using the copy() method of the shutil module to  
      # paste the select file to the desired directory  
      shutil.copy(fileToCopy, directoryToPaste)  
      # showing success message using the messagebox's showinfo() method  
      mb.showinfo(  
         title = "File copied!",  
         message = "The selected file has been copied to the selected location."  
         )  
   except:  
      # using the showerror() method to display error  
      mb.showerror(  
         title = "Error!",  
         message = "Selected file is unable to copy to the selected location. Please try again!"  
         )  
  
# function to delete a file  
def deleteFile():  
   # selecting the file using the filedialog's askopenfilename() method  
   the_file = fd.askopenfilename(  
      title = "Choose a file to delete",  
      filetypes = [("All files", "*.*")]  
      )  
   # deleting the file using the remove() method of the os module  
   os.remove(os.path.abspath(the_file))  
   # displaying the success message using the messagebox's showinfo() method  
   mb.showinfo(title = "File deleted!", message = "The selected file has been deleted.")  
  
# function to rename a file  
def renameFile():  
   # creating another window  
   rename_window = Toplevel(win_root)  
   # setting the title  
   rename_window.title("Rename File")  
   # setting the size and position of the window  
   rename_window.geometry("300x100+300+250")  
   # disabling the resizable option  
   rename_window.resizable(0, 0)  
   # setting the background color of the window to #F6EAD7  
   rename_window.configure(bg = "#F6EAD7")  
     
   # creating a label  
   rename_label = Label(  
      rename_window,  
      text = "Enter the new file name:",  
      font = ("verdana", "8"),  
      bg = "#F6EAD7",  
      fg = "#000000"  
      )  
   # placing the label on the window  
   rename_label.pack(pady = 4)  
     
   # creating an entry field  
   rename_field = Entry(  
      rename_window,  
      width = 26,  
      textvariable = enteredFileName,  
      relief = GROOVE,  
      font = ("verdana", "10"),  
      bg = "#FFFFFF",  
      fg = "#000000"  
      )  
   # placing the entry field on the window  
   rename_field.pack(pady = 4, padx = 4)  
  
   # creating a button  
   submitButton = Button(  
      rename_window,  
      text = "Submit",  
      command = submitName,  
      width = 12,  
      relief = GROOVE,  
      font = ("verdana", "8"),  
      bg = "#C8F25D",  
      fg = "#000000",  
      activebackground = "#709218",  
      activeforeground = "#FFFFFF"  
      )  
   # placing the button on the window  
   submitButton.pack(pady = 2)  
  
# defining a function get the file path  
def getFilePath():  
   # selecting the file using the filedialog's askopenfilename() method  
   the_file = fd.askopenfilename(title = "Select the file to rename", filetypes = [("All files", "*.*")])  
   # returning the file path  
   return the_file  
  
# defining a function that will be called when submit button is clicked  
def submitName():  
   # getting the entered name from the entry field  
   renameName = enteredFileName.get()  
   # setting the entry field to empty string  
   enteredFileName.set("")  
   # calling the getFilePath() function  
   fileName = getFilePath()  
   # creating a new file name for the file  
   newFileName = os.path.join(os.path.dirname(fileName), renameName + os.path.splitext(fileName)[1])  
   # using the rename() method to rename the file  
   os.rename(fileName, newFileName)  
   # using the showinfo() method to display a message box to show the success message  
   mb.showinfo(title = "File Renamed!", message = "The selected file has been renamed.")  
     
# defining a function to open a folder  
def openFolder():  
   # using the filedialog's askdirectory() method to select the folder  
   the_folder = fd.askdirectory(title = "Select Folder to open")  
   # using the startfile() of the os module to open the selected folder  
   os.startfile(the_folder)  
  
# defining a function to delete the folder  
def deleteFolder():  
   # using the filedialog's askdirectory() method to select the folder  
   folderToDelete = fd.askdirectory(title = 'Select Folder to delete')  
   # using the rmdir() method of the os module to delete the selected folder  
   os.rmdir(folderToDelete)  
   # displaying a success message using the showinfo() method  
   mb.showinfo("Folder Deleted!", "The selected folder has been deleted!")  
  
# defining a function to move the folder  
def moveFolder():  
   # using the askdirectory() method to select the folder  
   folderToMove = fd.askdirectory(title = 'Select the folder you want to move')  
   # using the showinfo() method to dislay  
   mb.showinfo(message = 'Folder has been selected to move. Now, select the desired destination.')  
   # using the askdirectory() method to select the destination  
   des = fd.askdirectory(title = 'Destination')  
  
   #using the try-except method  
   try:  
      # using the move() method of the shutil module to move the folder to the requested location  
      shutil.move(folderToMove, des)  
      # displaying the success message using the messagebox's showinfo() method  
      mb.showinfo("Folder moved!", 'The selected folder has been moved to the desired Location')  
   except:  
      # displaying the failure message using the messagebox's showerror() method  
      mb.showerror('Error!', 'The Folder cannot be moved. Make sure that the destination exists')  
  
# defining a function to list all the files available in a folder  
def listFilesInFolder():  
   # declaring a variable with initial value 0  
   i = 0  
   # using the askdirectory() method to select the folder  
   the_folder = fd.askdirectory(title = "Select the Folder")  
   # using the listdir() method to list all the files in the directory  
   the_files = os.listdir(os.path.abspath(the_folder))  
  
   # creating an object of Toplevel class  
   listFilesWindow = Toplevel(win_root)  
   # specifying the title of the pop-up window  
   listFilesWindow.title(f'Files in {the_folder}')  
   # specifying the size and position of the window  
   listFilesWindow.geometry("300x500+300+200")  
   # disabling the resizable option  
   listFilesWindow.resizable(0, 0)  
   # setting the background color of the window to #EC2FB1  
   listFilesWindow.configure(bg = "#EC2FB1")  
  
   # creating a list box  
   the_listbox = Listbox(  
      listFilesWindow,  
      selectbackground = "#F24FBF",  
      font = ("Verdana", "10"),  
      background = "#FFCBEE"  
      )  
   # placing the list box on the window  
   the_listbox.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)  
     
   # creating a scroll bar  
   the_scrollbar = Scrollbar(  
      the_listbox,  
      orient = VERTICAL,  
      command = the_listbox.yview  
      )  
   # placing the scroll bar to the right side of the window  
   the_scrollbar.pack(side = RIGHT, fill = Y)  
  
   # setting the yscrollcommand parameter of the listbox's config() method to the scrollbar  
   the_listbox.config(yscrollcommand = the_scrollbar.set)  
  
   # iterating through the files in the folder  
   while i < len(the_files):  
      # using the insert() method to insert the file details in the list box  
      the_listbox.insert(END, "[" + str(i+1) + "] " + the_files[i])  
      i += 1  
   the_listbox.insert(END, "")  
   the_listbox.insert(END, "Total Files: " + str(len(the_files)))  
  
# main function  
if __name__ == "__main__":  
   # creating an object of the Tk() class  
   win_root = Tk()  
   # setting the title of the main window  
   win_root.title("File Explorer - JAVATPOINT")  
   # set the size and position of the window  
   win_root.geometry("300x500+650+250")  
   # disabling the resizable option  
   win_root.resizable(0, 0)  
   # setting the background color to #D8E9E6  
   win_root.configure(bg = "#D8E9E6")  
  
   # creating the frames using the Frame() widget  
   header_frame = Frame(win_root, bg = "#D8E9E6")  
   buttons_frame = Frame(win_root, bg = "#D8E9E6")  
  
   # using the pack() method to place the frames in the window  
   header_frame.pack(fill = "both")  
   buttons_frame.pack(expand = TRUE, fill = "both")  
  
   # creating a label using the Label() widget  
   header_label = Label(  
      header_frame,  
      text = "File Explorer",  
      font = ("verdana", "16"),  
      bg = "#D8E9E6",  
      fg = "#1A3C37"  
      )  
  
   # using the pack() method to place the label in the window  
   header_label.pack(expand = TRUE, fill = "both", pady = 12)  
  
   # creating the buttons using the Button() widget  
   # open button  
   open_button = Button(  
      buttons_frame,  
      text = "Open a File",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = openFile  
      )  
  
   # copy button  
   copy_button = Button(  
      buttons_frame,  
      text = "Copy a File",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = copyFile  
      )  
  
   # delete button  
   delete_button = Button(  
      buttons_frame,  
      text = "Delete a File",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = deleteFile  
      )  
  
   # rename button  
   rename_button = Button(  
      buttons_frame,  
      text = "Rename a File",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = renameFile  
      )  
  
   # open folder button  
   open_folder_button = Button(  
      buttons_frame,  
      text = "Open a Folder",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = openFolder  
      )  
  
   # delete folder button  
   delete_folder_button = Button(  
      buttons_frame,  
      text = "Delete a Folder",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = deleteFolder  
      )  
  
   # move folder button  
   move_folder_button = Button(  
      buttons_frame,  
      text = "Move a Folder",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = moveFolder  
      )  
  
   # list all files button  
   list_button = Button(  
      buttons_frame,  
      text = "List all files in Folder",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#6AD9C7",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = listFilesInFolder  
      )  
  
   # using the pack() method to place the buttons in the window  
   open_button.pack(pady = 8)  
   copy_button.pack(pady = 8)  
   delete_button.pack(pady = 8)  
   rename_button.pack(pady = 8)  
   open_folder_button.pack(pady = 8)  
   delete_folder_button.pack(pady = 8)  
   move_folder_button.pack(pady = 8)  
   list_button.pack(pady = 8)  
  
   # creating an object of the StringVar() class  
   enteredFileName = StringVar()  
  
   # running the window  
   win_root.mainloop()  