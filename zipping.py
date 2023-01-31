
import zipfile
import os

def unzip(filename):

    # Specify the directory to extract the contents to
    filename_alias,extension = filename.split('.')
    extract_to = 'static\\files\\extracted\\'+filename_alias

    # Open the zip file
    with zipfile.ZipFile('static\\files\\'+filename, 'r') as zip_ref:
        # Create the specified directory if it doesn't exist
        os.makedirs(extract_to, exist_ok=True)
        # Extract the contents to the specified directory
        zip_ref.extractall(extract_to)

def stringyfy(file_path):
    string = ""
    with open(file_path, "r") as file:
        string+=file.read()
    return string.replace("\n"," ")



def list_files(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

print(list_files("static\\files\\extracted\\test_dir"))
# s=stringyfy("static\\files\\extracted\\twitter.py")
# print(s)