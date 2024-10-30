import subprocess
import threading
import os
from tenacity import retry, stop_after_attempt, wait_fixed

# Get commands from commands.txt
with open("commands.txt", "r") as file:
    commands = file.readlines()

# Each command is on its own line
commands = [command.strip() for command in commands]

# Create `archive/` if it doesn't exist
os.makedirs("archive", exist_ok=True)

@retry(stop=stop_after_attempt(50), wait=wait_fixed(15))
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd="archive")
        print(f"Command '{command}' executed successfully:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}':\n{e.stderr}")
        raise

# Execute each command in a separate thread
threads = []
for command in commands:
    thread = threading.Thread(target=execute_command, args=(command,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()