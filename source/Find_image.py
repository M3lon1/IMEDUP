import os
import imghdr

def find_image_files(directory):
    image_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Check image file 
            image_type = imghdr.what(file_path)
            if image_type:
                image_files.append(file_path)

    return image_files


try:
    directory_path = "D:\CS4DM Bauhaus Weimar\Octobr 2023\IMDEDU Project"
    image_files = find_image_files(directory_path)

    if not image_files:
        print("No image files found in the specified directory.")
    else:
        print("\nImage files found:")
        for image_file in image_files:
            print(image_file)

except Exception as e:
    print(f"An error occurred: {e}")
