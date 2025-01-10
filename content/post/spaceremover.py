import os
import re

def remove_spaces_from_filenames_in_directory(directory):
    """
    Remove spaces from image filenames in the specified directory and its subdirectories.
    """
    renamed_files = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(r'\.(png|jpg|jpeg|gif|bmp|svg)$', file, re.IGNORECASE):
                old_path = os.path.join(root, file)
                new_file = file.replace(" ", "")
                new_path = os.path.join(root, new_file)

                if old_path != new_path:
                    os.rename(old_path, new_path)
                    renamed_files[file] = new_file

    return renamed_files

def update_md_files(directory, renamed_files):
    """
    Update .md files to reflect the renamed image files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)

                with open(md_path, "r") as md_file:
                    content = md_file.read()

                updated_content = content
                for old_name, new_name in renamed_files.items():
                    updated_content = re.sub(
                        rf"\b{re.escape(old_name)}\b", new_name, updated_content
                    )

                if content != updated_content:
                    with open(md_path, "w") as md_file:
                        md_file.write(updated_content)

def main():
    directory = input("Enter the path to the directory: ")

    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid path.")
        return

    print("Removing spaces from image filenames...")
    renamed_files = remove_spaces_from_filenames_in_directory(directory)

    if renamed_files:
        print("Updating .md files to reflect changes...")
        update_md_files(directory, renamed_files)
        print("All .md files updated successfully.")
    else:
        print("No image files with spaces found.")

if __name__ == "__main__":
    main()
