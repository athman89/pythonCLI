# This is code for listing files in a directory
import os


def list_files(directory="."):
    files = os.listdir(directory)
    for file in files:
        print(file)
