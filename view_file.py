# This is code for viewing information about a file.
import os


def view_file_info(file_path):
    try:
        file_info = os.stat(file_path)
        print(f"File Size: {file_info.st_size} bytes")
        print(f"Last Modified: {file_info.st_mtime}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
