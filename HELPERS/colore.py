# from tkinter import *

# import ttkbootstrap as tb
# from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog


# root = tb.Window()
# root.title('color choser')
# root.geometry('740x432')

# def cc():
#     my_color = ColorChooserDialog()
#     my_color.show()
#     colors = my_color.result
#     my_label.config(text=colors)



# my_button = tb.Button(root, text='click', bootstyle='danger', command=cc)
# my_button.pack(pady=40)

# my_label = tb.Label(root, text='', font=('Helvetica', 18))

# root.mainloop()
from rembg import remove

from PIL import Image

input_path = 'pddf.png'
output_path = 'output.png'
inn = Image.open(input_path)
out = remove(inn)
out.save(output_path)