import requests
import subprocess

# URL of the commands file
url = "https://download.mersenne.ca/download.mersenne.ca_2024-10-01.txt"

# Fetch the commands from the URL
response = requests.get(url)
commands = response.text.splitlines()

# Create `archive/` if it doesn't exist
subprocess.run("mkdir -p archive", shell=True)

# cd into `archive/`
subprocess.run("cd archive", shell=True)

# Execute each command
for command in commands:
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Command '{command}' executed successfully:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}':\n{e.stderr}")