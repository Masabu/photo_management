import os
import re

def list_files_recursively(directory, pattern, dryrun=True, size_threshold=None):
    """
    Recursively list and optionally delete files in a directory matching a pattern.
    
    Parameters:
        directory (str): The directory to search.
        pattern (str): Regular expression pattern for file matching.
        dryrun (bool): If True, only list files without deleting. Default is True.
        size_threshold (int): File size threshold in bytes. Files larger than this will be deleted.
    """

    file_total_size = 0

    compiled_pattern = re.compile(pattern, re.IGNORECASE)  # Compile the regex pattern (case-insensitive)
    for root, dirs, files in os.walk(directory):
        #print(f"Folder: {root}")
        for file in files:
            if compiled_pattern.match(file):  # Match the file name against the pattern
                file_path = os.path.join(root, file)  # Get the full path of the file
                file_size = os.path.getsize(file_path)  # Get the file size in bytes

                file_total_size = file_total_size + file_size
                
                if size_threshold is None or file_size > size_threshold:
                    action = "Deleting" if not dryrun else "Found"
                    print(f"{action} File: {file_path} (Size: {file_size} bytes)")

                    if not dryrun:  # If dryrun is False, delete the file
                        try:
                            os.remove(file_path)
                            print(f"Deleted File: {file_path}")
                        except Exception as e:
                            print(f"Error deleting file {file_path}: {e}")
                else:
                    print(f"Skipping File: {file_path} (Size: {file_size} bytes)")

        #print()  # Blank line for readability
    file_total_size = file_total_size / 1024 / 1024 / 1024
    print(f"total file size of {directory} = {file_total_size} GB")

    return file_total_size


# Specify the directories to start from
search_directories = ["Art_Photos","Family_Photos", "GooglePhotos"]


# Regular expression pattern to match files

#pattern = r"\..*\.(jpeg|png|jpg|gif|json|xmp)$" 

pattern = r".*\.(json|xmp|dop)$"  

#pattern = r".*\((1|2|3|4)\).(jpeg|jpg)$"  # dupes

# File size threshold in bytes (e.g., 5 MB = 5 * 1024 * 1024 bytes)
size_threshold = 10 * 1024 * 1024

files_removed = 0

# List files recursively (set dryrun=False to actually delete files)
for folder in search_directories:
    print('**************************************')
    print(f"Cleaning up folder: {folder}")
    print('**************************************')
    size = list_files_recursively(folder, pattern, dryrun=True, size_threshold=None)
    files_removed = files_removed + size

print(f"total file size across folders {files_removed} GB")
