

from PIL import Image, ImageTk

def create_icon(image_path, output_path, sizes):
    # Load the image
    img = Image.open(image_path)

    # Create an empty ICO file
    ico = img.convert("RGBA")
    Icon_sizes = [(16, 16), (32, 32), (48,48)]
    imc = [ico.resize(size) for size in Icon_sizes]

    # Save the ICO file
    imc[1].save(output_path, format="ICO", sizes=[(s, s) for s in sizes])

if __name__ == "__main__":
    input_image_path = "C:\\Users\\DELL\\Desktop\\socketra\\ConveTransfer2\\images\\udd.png"  # Replace with your input image path
    output_icon_path = "udd.ico"  # Replace with your desired output icon path
    icon_sizes = [16,32,64]  # Add the desired sizes for the icon

    create_icon(input_image_path, output_icon_path, icon_sizes)





