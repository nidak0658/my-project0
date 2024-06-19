import os
import shutil

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Define the base path for organized files
organized_folder = os.path.expanduser("~/Downloads/Organized")

# Ensure the organized folder exists
if not os.path.exists(organized_folder):
    os.makedirs(organized_folder)

# Define file categories and their corresponding extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def organize_files():
    for filename in os.listdir(downloads_folder):
        # Get the full path of the file
        file_path = os.path.join(downloads_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Find the corresponding category
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_folder = os.path.join(organized_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                shutil.move(file_path, category_folder)
                print(f"Moved: {filename} -> {category_folder}")
                break
        else:
            # If no category is found, move to 'Others'
            others_folder = os.path.join(organized_folder, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, others_folder)
            print(f"Moved: {filename} -> {others_folder}")

if __name__ == '__main__':
    organize_files()
