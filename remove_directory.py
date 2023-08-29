# This is the code for deleting a directory
# It takes the directory name as its argument
import os


def delete_dir(directory):
    try:
        os.rmdir(directory)
        print(f"Deleted directory: {directory}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except OSError:
        print(f"Directory '{directory}' is not empty.")
