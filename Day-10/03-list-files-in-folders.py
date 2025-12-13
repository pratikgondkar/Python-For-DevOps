import os

def list_files_in_folders(folder_paths):
    try:
        files = os.listdir(folder_paths)
        return files, None
    except FileNotFoundError:
        return None, f"Error: The folder '{folder_paths}' does not exist."
    except PermissionError:
        return None, "Permission denied."
    
def main():
    folder_paths = input("Enter the folder paths separated by space: ").split()
    
    for folder_path in folder_paths:
        files, error = list_files_in_folders(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()