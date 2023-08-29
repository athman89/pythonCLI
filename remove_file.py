# This is a simple code for removing a file from a directory.
import os


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
