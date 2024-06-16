from rembg import remove
from PIL import Image

def remove_background(input_image_path, output_image_path):
    """
    Remove the background from an image and save the result.

    Args:
    - input_image_path (str): Path to the input image.
    - output_image_path (str): Path to save the output image.
    """
    # Open the input image
    input_image = Image.open(input_image_path)
    print(f"Opened image: {input_image_path}")

    # Remove the background
    output_image = remove(input_image)
    print("Background removed successfully.")

    # Save the output image
    output_image.save(output_image_path)
    print(f"Saved output image: {output_image_path}")

# Specify the input and output paths
input_image_path = '/Users/path/toyour/file'  # Replace with the path to your image
output_image_path = '/Users/path/toyour/file'   # Replace with the desired output path

# Call the function to remove the background
remove_background(input_image_path, output_image_path)