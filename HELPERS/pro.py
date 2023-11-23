# from packages import *

# # def profile_set(self):
# #     self.config_file = "config.json"
# #     self.load_configuration()

# def load_configuration(self):
#     try:
#         with open(self.config_file, "r") as config_file:
#             data = json.load(config_file)
#             self.profile_image_path = data.get("profile_image", resource_path2(relative_path="images/default.png"))
#             self.stats = data.get("stats", {"Name": "John Doe", "Age": 30, "Location": "City"})
#     except FileNotFoundError:
#         self.profile_image_path = resource_path2(relative_path="images/default.png")
#         self.stats = {"Name": "John Doe", "Age": 30, "Location": "City"}

# def save_configuration(self):
#     data = {"profile_image": self.profile_image_path, "stats": self.stats}
#     with open(self.config_file, "w") as config_file:
#         json.dump(data, config_file)

# def load_profile_image(self):
#     image = Image.open(self.profile_image_path)
#     image.thumbnail((150, 150))
#     photo = ImageTk.PhotoImage(image)

#     self.profile_image_label.config(image=photo)
#     self.profile_image_label.image = photo

# def create_circular_mask(self):
#     # Load the profile image
#     image = Image.open(self.profile_image_path)
#     image = image.convert("RGBA")

#     # Create a circular mask with the same size as the profile image
#     mask = Image.new("L", image.size, 0)
#     draw = ImageDraw.Draw(mask)

#     # Calculate the bounding box for a perfect circle
#     width, height = image.size
#     circle_size = min(width, height)
#     circle_bbox = (0, 0, circle_size, circle_size)

#     # Calculate the position to center the circle within the image
#     position = ((width - circle_size) // 2, (height - circle_size) // 2)

#     # Draw a circle on the mask
#     draw.ellipse((position[0], position[1], position[0] + circle_size, position[1] + circle_size), fill=255)

#     # Ensure the mask and profile image have the same size
#     if image.size != mask.size:
#         mask = mask.resize(image.size, Image.ANTIALIAS)

#     # Apply the circular mask to the profile image
#     result = Image.new("RGBA", image.size)
#     result.paste(image, (0, 0), mask)

#     # Resize the result to fit the label and create a PhotoImage
#     result.thumbnail((200, 200))
#     photo = ImageTk.PhotoImage(result)

#     # Update the label with the circular profile image
#     self.profile_image_label.config(image=photo)
#     self.profile_image_label.image = photo


# def update_profile_image(self):
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])

#     if file_path:
#         # Save the selected image path, load the new profile image, and save the configuration
#         self.profile_image_path = file_path
#         self.load_profile_image()
#         self.create_circular_mask()
#         self.save_configuration()

# def change_user_name(self):
#     new_name = simpledialog.askstring("Change Name", "Enter your new name:", parent=self)
#     if new_name:
#         self.stats["Name"] = new_name
#         self.name_label.config(text=new_name)
#         self.save_configuration()

import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageThumbnailViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Thumbnail Viewer")

        self.image_list = []
        self.current_image_index = 0

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(root, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.load_button = tk.Button(root, text="Load Images", command=self.load_images)
        self.load_button.pack()

    def load_images(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_list = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            self.current_image_index = 0
            self.show_current_image()
    
    def show_current_image(self):
        if self.image_list:
            image_path = self.image_list[self.current_image_index]
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)

            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

    def show_previous_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_list)
            self.show_current_image()

    def show_next_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
            self.show_current_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageThumbnailViewer(root)
    root.mainloop()
