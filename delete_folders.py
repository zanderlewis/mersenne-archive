# Delete all folders but .github/ and .git/
import os
import shutil

# Get all folders
folders = [folder for folder in os.listdir() if os.path.isdir(folder)]

# Delete all folders except .github/ and .git
for folder in folders:
    if folder != ".github" and folder != ".git":
        shutil.rmtree(folder)
        print(f"Deleted folder '{folder}'")

