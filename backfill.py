import os
import glob
import re

# Path to your posts directory
posts_dir = "_posts"

# The front matter you want to add to each post
additional_front_matter = """
layout: single
author: "Matt Demers"
author_profile: true
read_time: true
comments: true
share: true
related: true
"""

# Process all markdown files
for file_path in glob.glob(f"{posts_dir}/*.md"):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file has frontmatter
    if content.startswith('---'):
        # Skip files that already have layout and author
        if 'layout: single' in content and 'author: matt' in content:
            print(f"Skipping {os.path.basename(file_path)} - already has required frontmatter")
            continue
        
        # Find where the frontmatter ends
        second_marker = content.find('---', 3)
        if second_marker > 0:
            # Insert additional front matter before the end marker
            updated_content = content[:second_marker] + additional_front_matter + content[second_marker:]
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"Updated {os.path.basename(file_path)}")
        else:
            print(f"Invalid frontmatter format in {os.path.basename(file_path)}")
    else:
        print(f"No frontmatter found in {os.path.basename(file_path)}")

print("\nDone! Front matter added to all posts.")