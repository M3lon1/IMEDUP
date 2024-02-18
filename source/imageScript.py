from wand.image import Image
import os
import shutil

def change_format_and_save(input_folder, output_folder):
    # Change format to PNG and save
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, output_name + '.png')

        with Image(filename=input_path) as img:
            img.format = 'png'
            img.save(filename=output_path)

def resize_and_save(input_folder, output_folder, width, height):
    # Resize and save
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, output_name + '_resized.jpg')

        with Image(filename=input_path) as img:
            img.resize(width, height)
            img.format = 'jpeg'
            img.save(filename=output_path)

def resize_flip_and_save(input_folder, output_folder, width, height):
    # Resize, flip, and save
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, output_name + '_resized_flipped.jpg')

        with Image(filename=input_path) as img:
            img.resize(width, height)
            img.flop()  # Horizontal flip
            img.format = 'jpeg'
            img.save(filename=output_path)

def flop_and_save(input_folder, output_folder):
    # Flop and save
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, output_name + '_flopped.jpg')

        with Image(filename=input_path) as img:
            img.flop()  # Horizontal flip
            img.format = 'jpeg'
            img.save(filename=output_path)

def resize_crop_and_save(input_folder, output_folder, width, height, left, top, right, bottom):
    # Resize, crop, and save
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, output_name + '_resized_cropped.jpg')

        with Image(filename=input_path) as img:
            img.resize(width, height)
            img.crop(left=left, top=top, right=right, bottom=bottom)
            img.format = 'jpeg'
            img.save(filename=output_path)

def create_duplicates_and_save(input_folder, output_folder, num_duplicates):
    # Create duplicates and save all
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_path = os.path.join(input_folder, file)

        for i in range(1, num_duplicates + 1):
            output_name = os.path.splitext(file)[0] + f'_duplicate{i}'
            output_path = os.path.join(output_folder, output_name + '.jpg')

            shutil.copy(input_path, output_path)


input_folder = "/home/mirza/Documents/Images"
output_folder = "/home/mirza/Documents/Output"

# Change format to PNG and save
change_format_and_save(input_folder, output_folder)

# Resize and save
resize_and_save(input_folder, output_folder, 1024, 1024)

# Resize, flip, and save
resize_flip_and_save(input_folder, output_folder, 1024, 1024)

# Flop and save
flop_and_save(input_folder, output_folder)

# Resize, crop, and save
resize_crop_and_save(input_folder, output_folder, 800, 800, 100, 100, 700, 700)

# Create duplicates and save all
create_duplicates_and_save(input_folder, output_folder, 3)
