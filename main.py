import os
import re

def find_unused_images(base_directory, image_directories, extensions):
    # Get all image files from specified directories
    all_images = set()
    for image_dir in image_directories:
        full_path = os.path.join(base_directory, image_dir)
        for root, _, files in os.walk(full_path):
            for file in files:
                if file.lower().endswith(extensions):
                    all_images.add(file)

    # Get all files that might reference images
    used_images = set()
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith(('.html', '.css', '.js')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    found_images = re.findall(r'[\'"]([^\'"]*\.(?:' + '|'.join(extensions) + '))[\'"]', content, re.I)
                    used_images.update(map(os.path.basename, found_images))

    # Find unused images
    unused_images = all_images - used_images
    return unused_images

# Usage
base_dir = '.'  # Current directory, change this if your script is not in the root of your project
image_dirs = ['img', 'assets/images']
extensions = ('.jpg', '.png', '.gif', '.jpeg', '.svg', '.webp', '.mp4', '.webm')

unused = find_unused_images(base_dir, image_dirs, extensions)
print("Potentially unused images and videos:")
for image in unused:
    print(image)

print(f"\nTotal number of potentially unused files: {len(unused)}")