import os

def walk_and_forensic(path):
    for root_path, folders, files in os.walk(path):
        for folder in folders:
            print(os.path.join(root_path, folder))

        for filename in files:
            if filename.endswith('.cpp'):
                os.replace(os.path.join(root_path, filename), os.path.join(".", "folder_cpp", filename))
            elif filename.endswith('.html'):
                os.replace(os.path.join(root_path, filename), os.path.join(".", "folder_html", filename))
            elif filename.endswith('.txt'):
                os.replace(os.path.join(root_path, filename), os.path.join(".", "folder_txt", filename))

walk_and_forensic("..")