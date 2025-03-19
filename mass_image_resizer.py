import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder, size=(256, 256)):
    if not os.path.exists(folder_path):
        print(f"Error: Input folder '{folder_path}' does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.gif')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    img = img.resize(size, Image.ANTIALIAS)
                    img.save(output_path)
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing images: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()

    # Convert to absolute paths
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)

    resize_images_in_folder(input_folder, output_folder)
