import sqlite3
import math
import cv2
from PIL import Image
import numpy as np
import imagehash
import sqlite3
import os

def rotate_image(image, angle):
    """
    Rotates an OpenCV 2 / NumPy image about it's centre by the given angle
    (in degrees). The returned image will be large enough to hold the entire
    new image, with a black background
    """

    # Get the image size
    # No that's not an error - NumPy stores image matricies backwards
    image_size = (image.shape[1], image.shape[0])
    image_center = tuple(np.array(image_size) / 2)

    # Convert the OpenCV 3x2 rotation matrix to 3x3
    rot_mat = np.vstack(
        [cv2.getRotationMatrix2D(image_center, angle, 1.0), [0, 0, 1]]
    )

    rot_mat_notranslate = np.matrix(rot_mat[0:2, 0:2])

    # Shorthand for below calcs
    image_w2 = image_size[0] * 0.5
    image_h2 = image_size[1] * 0.5

    # Obtain the rotated coordinates of the image corners
    rotated_coords = [
        (np.array([-image_w2,  image_h2]) * rot_mat_notranslate).A[0],
        (np.array([ image_w2,  image_h2]) * rot_mat_notranslate).A[0],
        (np.array([-image_w2, -image_h2]) * rot_mat_notranslate).A[0],
        (np.array([ image_w2, -image_h2]) * rot_mat_notranslate).A[0]
    ]

    # Find the size of the new image
    x_coords = [pt[0] for pt in rotated_coords]
    x_pos = [x for x in x_coords if x > 0]
    x_neg = [x for x in x_coords if x < 0]

    y_coords = [pt[1] for pt in rotated_coords]
    y_pos = [y for y in y_coords if y > 0]
    y_neg = [y for y in y_coords if y < 0]

    right_bound = max(x_pos)
    left_bound = min(x_neg)
    top_bound = max(y_pos)
    bot_bound = min(y_neg)

    new_w = int(abs(right_bound - left_bound))
    new_h = int(abs(top_bound - bot_bound))

    # We require a translation matrix to keep the image centred
    trans_mat = np.matrix([
        [1, 0, int(new_w * 0.5 - image_w2)],
        [0, 1, int(new_h * 0.5 - image_h2)],
        [0, 0, 1]
    ])

    # Compute the tranform for the combined rotation and translation
    affine_mat = (np.matrix(trans_mat) * np.matrix(rot_mat))[0:2, :]

    # Apply the transform
    result = cv2.warpAffine(
        image,
        affine_mat,
        (new_w, new_h),
        flags=cv2.INTER_LINEAR
    )

    return result


def largest_rotated_rect(w, h, angle):
    """
    Given a rectangle of size wxh that has been rotated by 'angle' (in
    radians), computes the width and height of the largest possible
    axis-aligned rectangle within the rotated rectangle.

    Original JS code by 'Andri' and Magnus Hoff from Stack Overflow

    Converted to Python by Aaron Snoswell
    """

    quadrant = int(math.floor(angle / (math.pi / 2))) & 3
    sign_alpha = angle if ((quadrant & 1) == 0) else math.pi - angle
    alpha = (sign_alpha % math.pi + math.pi) % math.pi

    bb_w = w * math.cos(alpha) + h * math.sin(alpha)
    bb_h = w * math.sin(alpha) + h * math.cos(alpha)

    gamma = math.atan2(bb_w, bb_w) if (w < h) else math.atan2(bb_w, bb_w)

    delta = math.pi - alpha - gamma

    length = h if (w < h) else w

    d = length * math.cos(alpha)
    a = d * math.sin(alpha) / math.sin(delta)

    y = a * math.cos(gamma)
    x = y * math.tan(gamma)

    return (
        bb_w - 2 * x,
        bb_h - 2 * y
    )


def crop_around_center(image, width, height):
    """
    Given a NumPy / OpenCV 2 image, crops it to the given width and height,
    around it's centre point
    """

    image_size = (image.shape[1], image.shape[0])
    image_center = (int(image_size[0] * 0.5), int(image_size[1] * 0.5))

    if(width > image_size[0]):
        width = image_size[0]

    if(height > image_size[1]):
        height = image_size[1]

    x1 = int(image_center[0] - width * 0.5)
    x2 = int(image_center[0] + width * 0.5)
    y1 = int(image_center[1] - height * 0.5)
    y2 = int(image_center[1] + height * 0.5)

    return image[y1:y2, x1:x2]


def Get_Posible_Rotation_Hash(image, teta, n,source_path):
    image_height, image_width = image.shape[0:2]
    i = 1
    alpha = teta
    while i <= n:
        image_orig = np.copy(image)
        image_rotated = rotate_image(image_orig, alpha)
        image_rotated_cropped = crop_around_center(image_rotated,*largest_rotated_rect(image_width,image_height,math.radians(i)))
        # Convert to PIL image so we can work on it with imageHash library
        a = get_hash(image_rotated_cropped)
        add_values_to_database(a,source_path,alpha)
        alpha += teta
        i += 1


def get_unique_paths(database_path,query):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    # Execute the SQL query to select unique paths
    cursor.execute(query)
    # Fetch all the unique paths as a list
    unique_paths = [row[0] for row in cursor.fetchall()]
    # Close the database connection
    connection.close()
    return unique_paths

def add_values_to_database(Hash, File_path, Rotation):
    c.execute("INSERT INTO All_Images VALUES (:Hash, :File_path, :Rotation)", {'Hash': str(Hash), 'File_path': File_path, 'Rotation':Rotation})
    conn.commit()

def get_hash(image):
    im_pil = Image.fromarray(image)
    Hash = imagehash.dhash(im_pil)
    print(Hash)
    return Hash







if __name__ == "__main__":
    # Replace 'All_Images.db' with the actual path to your database file
    rotation_degree = 2
    number_of_rotations = 5
    database_path = 'All_Images.db'
    query = "SELECT DISTINCT Path FROM All_Images"
    unique_paths_list = get_unique_paths(database_path,query)
    try:
        directory_path = "D:\CS4DM Bauhaus Weimar\Octobr 2023\IMDEDU Project"
        SQL_file = "D:\CS4DM Bauhaus Weimar\Octobr 2023\IMDEDU Project\All_Visualhashes.db"
        if not os.path.isfile(SQL_file):
            conn = sqlite3.connect(SQL_file)
            c = conn.cursor()
            c.execute("""CREATE TABLE All_Images (
                Visual_hash text,
                Path text,
                Rotation text
            )""")
            print("Data base with name All_Images.db has been created.")
        else:
            conn = sqlite3.connect(SQL_file)
            c = conn.cursor()
        #Get all the image files in the repository
        
        for image_file in unique_paths_list:
            image = cv2.imread(image_file)
            original_hash = get_hash(image)
            
            add_values_to_database(original_hash,image_file,0)
            print("done")
            Get_Posible_Rotation_Hash(image,rotation_degree,number_of_rotations,image_file)
            
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Print or use the unique paths list as needed
        print(unique_paths_list[0])