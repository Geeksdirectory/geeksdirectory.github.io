import os
import re

def replace_obsidian_links(folder_path):
    # Walk through all files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):  # Process only Markdown files
                file_path = os.path.join(root, file)

                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace Obsidian-style links with Markdown-style links
                updated_content = re.sub(r'!\[\[(.*?)\]\]', r'![alt text](\1)', content)

                # Write back the updated content if there are changes
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated: {file_path}")

if __name__ == "__main__":
    # Specify the path to your Obsidian vault or folder
    folder_path = input("Enter the folder path containing Markdown files: ").strip()

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        replace_obsidian_links(folder_path)
        print("Replacement completed!")
    else:
        print("Invalid folder path. Please provide a valid directory.")
