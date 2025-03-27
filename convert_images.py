import os
import glob
import re

# Path to your posts directory
posts_dir = "_posts"

# Process all markdown files
for file_path in glob.glob(f"{posts_dir}/*.md"):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file has frontmatter and coverImage
    if content.startswith('---') and 'coverImage:' in content:
        # Extract the cover image filename
        cover_image_match = re.search(r'coverImage:\s*"([^"]+)"', content)
        
        if cover_image_match:
            image_filename = cover_image_match.group(1)
            
            # Create the replacement header block
            header_block = f'header:\n  image: "/assets/images/{image_filename}"'
            
            # Replace the coverImage line with the header block
            # This regex looks for the coverImage line with potential whitespace
            updated_content = re.sub(
                r'coverImage:\s*"[^"]+"', 
                header_block, 
                content
            )
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"Updated {os.path.basename(file_path)}")
        else:
            print(f"coverImage format not recognized in {os.path.basename(file_path)}")
    else:
        print(f"No coverImage found in {os.path.basename(file_path)}")

print("\nDone! coverImage replaced with header.image in all posts.")