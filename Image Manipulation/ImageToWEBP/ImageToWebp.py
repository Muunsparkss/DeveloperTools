import os
from PIL import Image

def convert_to_webp(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to WebP format
    webp_path = os.path.splitext(image_path)[0] + '.webp'
    image.save(webp_path, 'webp')

    # Close the image
    image.close()

def convert_directory_to_webp(directory):
    # Walk through the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has an image extension
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file)
                convert_to_webp(image_path)
                print(f"Converted {image_path} to WebP")

# Specify the directory containing the image files
directory_path = 'C:/Users/mehme/Desktop/METAVOLTA/UrunFotograflari/VT3PRO-YÜKSEK'

# Convert all image files in the specified directory and subdirectories to WebP
convert_directory_to_webp(directory_path)