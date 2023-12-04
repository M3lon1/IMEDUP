import csv
import os
import imghdr
import hashlib


def add_values_to_csv(file_path, id, value1, value2):
    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the two values to the end of the CSV file
        csv_writer.writerow([id,value1, value2])

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

def get_hash(file):   
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)
    return (readable_hash)

try:
    directory_path = "D:\CS4DM Bauhaus Weimar\Octobr 2023\IMDEDU Project"
    CSV_file = "D:\CS4DM Bauhaus Weimar\Octobr 2023\IMDEDU Project\All_Images.csv"
    if not os.path.isfile(CSV_file):
        with open(CSV_file, 'a', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["id", "Hash", "File Location"])
    
    #Get all the i,age files in the repository
    image_files = find_image_files(directory_path)

    if not image_files:
        print("No image files found in the specified directory.")
    else:
        id = 1
        print("\nImage files found:")
        for image_file in image_files:
            hash = get_hash(image_file)
            add_values_to_csv(CSV_file, id, hash, image_file)
            id += 1

except Exception as e:
    print(f"An error occurred: {e}")
