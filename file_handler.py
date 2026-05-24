import os

def save_to_file(file_path, object_list):
    """
    Saves a list of objects to a .txt file using a delimiter.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for obj in object_list:
                file.write(obj.to_file_string())
    except IOError:
        print(f"Error: Could not write to file '{file_path}'. Check permissions.")

def load_from_file(file_path):
    """
    Reads data from a .txt file and returns a list of raw string data arrays.
    """
    raw_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    row = cleaned_line.split('|')
                    raw_data.append(row)
    except FileNotFoundError:
        print(f"System: No database found for '{file_path}'. Starting fresh.")
    
    return raw_data