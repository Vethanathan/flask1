import shutil
import os
folder_path = "static\\files\\extracted"

if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print(f"{folder_path} has been deleted.")
else:
    print(f"{folder_path} does not exist.")
