import os
import datetime

def generate_frontmatter(file_path, folder_name):
    """
    Generate the frontmatter for a given file based on its creation date and folder structure.
    """
    # Extract the file name without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Format the title based on folder and file name
    title = f"{folder_name} {file_name.replace('.', ' ')}".strip()

    # Get the file creation date
    creation_time = os.path.getctime(file_path)
    date = datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")

    # Create the frontmatter
    frontmatter = f"""---
title: {title}
date: {date}
---
"""

    return frontmatter

def update_markdown_files(directory):
    """
    Add frontmatter to Markdown files that are missing it.
    """
    for root, _, files in os.walk(directory):
        folder_name = os.path.basename(root)

        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    content = f.read()

                # Check if the file already has frontmatter
                if content.strip().startswith("---"):
                    continue

                # Generate the frontmatter
                frontmatter = generate_frontmatter(file_path, folder_name)

                # Add the frontmatter to the file
                with open(file_path, "w") as f:
                    f.write(frontmatter + "\n" + content)

                print(f"Updated: {file_path}")

def main():
    directory = input("Enter the path to the Hugo content directory: ")

    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid path.")
        return

    print("Updating Markdown files...")
    update_markdown_files(directory)
    print("All files updated successfully.")

if __name__ == "__main__":
    main()

