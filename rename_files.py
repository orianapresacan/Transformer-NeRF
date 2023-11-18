import os

directory = 'logs'

files = os.listdir(directory)
counter = 0

image_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')

for filename in files:
    if filename.lower().endswith(image_formats):
        new_filename = f'{counter:03d}.png' 
        original_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        
        os.rename(original_file_path, new_file_path)

        counter += 1

print(f"Renamed {counter} files.")
