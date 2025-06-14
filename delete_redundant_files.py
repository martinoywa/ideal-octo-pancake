import os

def delete_files_with_extension(root_dir, extension):
    deleted_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(extension):
                file_path = os.path.join(dirpath, file)
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    print(f"\nTotal files deleted: {len(deleted_files)}")

# Example usage
if __name__ == "__main__":
    directory = "."  # current parent directory
    ext = ".Identifier"  # delete all :Zone.Identifier files
    delete_files_with_extension(directory, ext)
