import os
import shutil
import pytesseract
from PIL import Image

# Ask the user for the path to the Tesseract executable
tesseract_cmd = input("Please enter the path to the Tesseract executable, or press Enter to use the default path: ")

# If no value is supplied, default to the existing set one
if not tesseract_cmd:
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Tell pytesseract where to find the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

def ocr_from_images(input_folder, output_folder, archive_folder):
    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        return

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create the archive folder if it does not exist
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Get list of files in the input folder
    files = os.listdir(input_folder)

    # If the input folder is empty, return a message
    if not files:
        print("No input files found.")
        return

    # Loop over all files in the input folder
    for filename in files:
        # Construct the full file path
        input_file_path = os.path.join(input_folder, filename)
        
        # Open the image file
        try:
            with Image.open(input_file_path) as img:
                # Perform OCR on the image
                text = pytesseract.image_to_string(img)
        except Exception as e:
            print(f"Error processing file '{filename}': {e}")
            continue
            
        # Construct the output file path (replace the file extension with .txt)
        base, _ = os.path.splitext(filename)
        output_file_path = os.path.join(output_folder, f"{base}.txt")

        # Write the OCR output to the text file
        try:
            with open(output_file_path, 'w') as f:
                f.write(text)
        except Exception as e:
            print(f"Error writing to file '{output_file_path}': {e}")
            continue

        # Move the input file to the archive folder
        archive_file_path = os.path.join(archive_folder, filename)
        shutil.move(input_file_path, archive_file_path)

# Define the input, output, and archive directories
input_folder = "input"
output_folder = "output"
archive_folder = "archive"

# Run the function
ocr_from_images(input_folder, output_folder, archive_folder)
