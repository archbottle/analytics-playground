#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Constants
COMMON_FILE = "__common__.html"
START_MARKER = "<!-- ANALYTICS-START -->"
END_MARKER = "<!-- ANALYTICS-END -->"

def read_common_file():
    """Read the common analytics file."""
    with open(COMMON_FILE, 'r') as f:
        return f.read()

def update_html_file(file_path, common_content):
    """Update a single HTML file with the common analytics content."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Create the pattern to match the analytics section
    pattern = f"{START_MARKER}.*?{END_MARKER}"
    
    # Prepare the new analytics section
    new_section = f"{START_MARKER}\n{common_content}\n{END_MARKER}"
    
    # Check if the markers exist
    if START_MARKER in content and END_MARKER in content:
        # Replace existing section
        new_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    else:
        # Find the closing head tag and insert before it
        new_content = content.replace('</head>', f'{new_section}\n</head>')
    
    # Write back to file
    with open(file_path, 'w') as f:
        f.write(new_content)

def main():
    """Main function to update all HTML files."""
    # Read the common content
    common_content = read_common_file()
    
    # Get all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != COMMON_FILE]
    
    # Update each HTML file
    for html_file in html_files:
        print(f"Updating {html_file}...")
        update_html_file(html_file, common_content)
        print(f"Updated {html_file}")

if __name__ == "__main__":
    main() 