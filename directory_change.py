# This is code for switching to a new directory.
import os


def change_directory(new_directory):
    os.chdir(new_directory)
    print(f"Changed directory to: {new_directory}")
