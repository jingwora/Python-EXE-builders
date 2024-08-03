# functions.py

import os

def is_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file.read()
        return True
    except:
        return False

def combine_files(file1, file2):
    if not os.path.exists(file1) or not os.path.exists(file2):
        return None, "One or both files do not exist."
    
    if not is_text_file(file1) or not is_text_file(file2):
        return None, "One or both files are not text files."

    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
        
        combined_content = content1 + "\n" + content2
        return combined_content, None
    except Exception as e:
        return None, f"Error reading files: {e}"
