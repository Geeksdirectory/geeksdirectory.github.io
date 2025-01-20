import os
import markdown
import pdfkit

# Function to convert Markdown to PDF
def md_to_pdf(md_content, output_path):
    # Convert markdown content to HTML
    html_content = markdown.markdown(md_content)
    
    # Convert HTML to PDF and save it
    pdfkit.from_string(html_content, output_path)

# Ask user for the input folder (containing .md files)
input_folder = input("Enter the path to the folder containing .md files: ").strip()

# Ask user for the output folder (where .pdf files will be saved)
output_folder = input("Enter the path to the folder where PDFs should be saved: ").strip()

# Ensure the output folder exists, create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".md"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename.replace(".md", ".pdf"))
        
        # Read the Markdown content
        with open(input_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        # Convert and save as PDF
        md_to_pdf(md_content, output_file_path)
        print(f'Converted {filename} to PDF')

print("Conversion complete.")

