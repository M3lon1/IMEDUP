import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.spatial.distance import hamming

# Connect to your SQL database
conn = sqlite3.connect('All_Visualhashes.db')
cursor = conn.cursor()

# Retrieve data from the database (assuming 'path' and 'visual_hash' are your column names)
cursor.execute("SELECT path, visual_hash FROM All_Images")
data = cursor.fetchall()

# Function to calculate hamming distance between two visual hashes
def hamming_distance(hash1, hash2):
    return hamming(np.array(list(hash1)), np.array(list(hash2)))

# print(data[0][1] - data[1][1])
# Create a matrix to store the hamming distances
num_images = len(data)
hamming_matrix = np.zeros((num_images, num_images))

# Calculate hamming distances and populate the matrix
for i in range(num_images):
    for j in range(i+1, num_images):
        hash1 = data[i][1]
        hash2 = data[j][1]
        distance = hamming_distance(hash1, hash2)
        hamming_matrix[i, j] = distance
        hamming_matrix[j, i] = distance

# Create a heatmap using matplotlib
plt.figure(figsize=(100, 100))  # Adjust the size as needed
plt.imshow(hamming_matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Hamming Distance Heatmap')
plt.xlabel('Image Index')
plt.ylabel('Image Index')

# Display the figure
plt.show()

# Close the database connection
conn.close()