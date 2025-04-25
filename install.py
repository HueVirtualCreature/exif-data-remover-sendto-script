import os
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))
batch_file = os.path.join(current_dir, "remove_exif_data.bat")
if not os.path.exists(batch_file):
    raise FileNotFoundError(f"Batch file not found: {batch_file}")

# Replace <PATH> in the batch file with the current directory path
with open(batch_file, "r") as file:
    content = file.read()
content = content.replace("<PATH>", current_dir)
with open(batch_file, "w") as file:
    file.write(content)

# Windows "SendTo" folder path
sendto_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "SendTo")
if not os.path.exists(sendto_folder):
    raise FileNotFoundError(f"SendTo folder not found: {sendto_folder}")

shutil.copy(batch_file, sendto_folder)
print(f"Copied to {sendto_folder} and updated.")