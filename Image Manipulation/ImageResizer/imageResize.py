import os
from PIL import Image

def resize_image(input_path, output_path, target_size):
  """
  Resizes an image to the specified target size (width, height).

  Args:
      input_path (str): Path to the input image file.
      output_path (str): Path to save the resized image.
      target_size (tuple): A tuple containing the desired width and height of the resized image.
  """

  try:
    # Open the image with Pillow
    with Image.open(input_path) as image:
      # Maintain aspect ratio for better quality
      width, height = image.size
      aspect_ratio = width / height

      # Determine new dimensions based on target size and aspect ratio
      new_width, new_height = target_size
      if new_width / new_height > aspect_ratio:
        new_width = int(new_height * aspect_ratio)
      else:
        new_height = int(new_width / aspect_ratio)

      # Resize the image using LANCZOS filter for smoother scaling
      resized_image = image.resize((new_width, new_height), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

      # Save the resized image with the appropriate format based on output path extension
      resized_image.save(output_path, format=output_path.split('.')[-1].upper())
      print(f"Image resized successfully: {input_path} -> {output_path}")

  except FileNotFoundError:
    print(f"Error: Input file not found: {input_path}")
  except Exception as e:
    print(f"An error occurred: {e}")

def resize_images_in_directory(directory_path, target_size, output_format="UNCHANGED"):
  """
  Resizes all images in a directory to the specified target size.

  Args:
      directory_path (str): Path to the directory containing images.
      target_size (tuple): A tuple containing the desired width and height of the resized images.
      output_format (str, optional): The format to save the resized images in.
          Defaults to "UNCHANGED" (uses the original format).
  """
  for filename in os.listdir(directory_path):
    # Get full path for each image
    input_path = os.path.join(directory_path, filename)

    # Check if it's a valid image file (modify extensions as needed)
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
      # Determine output path based on output format
      if output_format == "UNCHANGED":
        output_path = os.path.join(directory_path, f"resized_{filename}")
      else:
        output_path = os.path.join(directory_path, f"resized_{filename.split('.')[:-1]}.{output_format.upper()}")

      # Resize the image using the previous function
      resize_image(input_path, output_path, target_size)

# Example usage
directory_path = "Your/Directory/Path"  # Replace with your actual directory path
target_size = (2560, 2560)  # Replace with your target width and height
output_format = "webp"  # Optional: Specify output format (e.g., "PNG", "JPEG")

resize_images_in_directory(directory_path, target_size, output_format)
