from PIL import Image
import os

def add_white_background(image_path, output_path):
    try:
        img = Image.open(image_path)
        if img.mode == 'RGBA':
            # Create a white background image of the same size
            bg = Image.new('RGB', img.size, (255, 255, 255))
            # Paste the transparent image onto the white background
            bg.paste(img, mask=img.split()[3])
            bg.save(output_path, 'WEBP')
            print(f"Converted {image_path} to non-transparent and saved as {output_path}")
        else:
            print(f"{image_path} is not a transparent .webp image, skipping...")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.webp'):
                image_path = os.path.join(root, file)
                output_path = os.path.join(root, file.split('.')[0] + '_non_transparent.webp')
                add_white_background(image_path, output_path)

# Replace 'path_to_directory' with the path to the directory containing your images
process_directory('Your/Directory/Path')