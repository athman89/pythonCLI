# This is the command for listing disks available in the system
import psutil


def list_disks():
    disks = psutil.disk_partitions()
    for disk in disks:
        print(f"Device: {disk.device}\nMountpoint: {disk.mountpoint}\nFilesystem Type: {disk.fstype}\n")
