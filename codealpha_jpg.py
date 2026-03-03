import os
import shutil

# ------------------------------
# Task Automation Script
# Move all .jpg files to a new folder
# ------------------------------

# Source folder path (change this to your folder path)
source_folder = "source_folder"

# Destination folder path
destination_folder = "jpg_files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all files in source folder
for filename in os.listdir(source_folder):
    
    # Check if file ends with .jpg
    if filename.endswith(".jpg"):
        
        # Full file path
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        # Move file
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("✅ All .jpg files moved successfully!")