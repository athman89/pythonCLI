# This is a simple command line interface program

import argparse

from create_directory import create_dir
from directory_change import change_directory
from exit_application import exit_application
from list_disk import list_disks
from list_file import list_files
from remove_directory import delete_dir
from remove_file import delete_file
from sys_info import view_system_info
from text_manipulation import count_words
from view_file import view_file_info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line Application")
    parser.add_argument("command",
                        choices=["mkdir", "info", "rmdir", "rmfile", "sys_info", "count_words",
                                 "list_disks", "ls", "cd", "exit"],
                        help="Choose a command to execute")
    parser.add_argument("--directory", help="Specify a directory for list_files or change_directory command")
    parser.add_argument("--text", help="Specify text for text manipulation")
    args = parser.parse_args()

    if args.command == "mkdir":
        create_dir(args.path)
    elif args.command == "info":
        view_file_info(args.path)
    elif args.command == "rmdir":
        delete_dir(args.path)
    elif args.command == "rmfile":
        delete_file(args.path)
    elif args.command == "sys_info":
        view_system_info()
    elif args.command == "count_words":
        num_words = count_words(args.text)
        print(f"Number of words: {num_words}")
    elif args.command == "list_disks":
        list_disks()
    elif args.command == "ls":
        list_files(args.directory)
    elif args.command == "cd":
        change_directory(args.directory)
    elif args.command == "exit":
        exit_application()
