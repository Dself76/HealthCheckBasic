import psutil

def check_disk(disk, min_free_percent):
    """Checks if there is enough free disk space."""
    du = psutil.disk_usage(disk)
    free_percent = 100 * du.free / du.total
    return free_percent >= min_free_percent

def check_memory(min_free_percent):
    """Checks if there is enough free memory."""
    vm = psutil.virtual_memory()
    free_percent = 100 * vm.available / vm.total
    return free_percent >= min_free_percent

if __name__ == "__main__":
    disk = '/'
    if not check_disk(disk, 20):  # Check if at least 20% disk is free
        print(f"Disk space critical: less than 20% free on disk {disk}")
    else:
        print("Disk space is sufficient.")

    if not check_memory(10):  # Check if at least 10% memory is free
        print("Memory is low.")
    else:
        print("Memory level is sufficient.")
