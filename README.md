# Command Line Application

A versatile and user-friendly Python command-line application that provides various utility commands for interacting with files, directories, text, and system information.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Command Examples](#command-examples)
- [Available Commands](#available-commands)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

Welcome to the Command Line Application! This application lets you perform various tasks through simple commands in your terminal.

### Prerequisites

- Python 3.x
- Required packages are listed in `requirements.txt`

### Installation

1. Clone this repository using `git clone https://github.com/your-username/command-line-app.git`
2. Navigate to the project directory: `cd command-line-app`
3. Install the required packages: `pip install -r requirements.txt`

## Usage

Run the application by executing `main.py` in your terminal. Provide the desired command and any necessary arguments.

### Command Examples

- List files in the current directory: `python main.py ls`
- Create a new directory: `python main.py mkdir new_directory`
- Delete a file: `python main.py rmfile path/to/file.txt`
- Delete a directory: `python main.py rmdir path/to/directory`
- View file information: `python main.py info path/to/file.txt`
- View system information: `python main.py sysinfo`
- List disks: `python main.py list_disks`
- Change directory: `python main.py cd new_path`
- Count words in text: `python main.py count_words --text "This is a sample text."`

## Available Commands

- `ls`: List files in a directory.
- `mkdir`: Create a new directory.
- `rmfile`: Delete a file.
- `rmdir`: Delete a directory.
- `info`: View file information.
- `sysinfo`: View system information.
- `list_disks`: List available disks.
- `cd`: Change the current directory.
- `count_words`: Count words in provided text.

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License


## Acknowledgments

- This project was inspired by the need for a versatile command-line utility.
- Thanks to the Python community for the wonderful packages used in this application.
