# This is a simple code for creating a directory
import os


def create_dir(directory):
    try:
        os.mkdir(directory)
        print(f"Created directory: {directory}")
    except FileExistsError:
        print(f"Directory '{directory}' already exists.")
