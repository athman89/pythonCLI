# This is the code for showing system information
import os
import psutil


def view_system_info():
    print(f"System: {os.name}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"Memory: {psutil.virtual_memory().total} bytes")
