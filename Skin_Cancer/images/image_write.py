import os
import pandas as pd

# Folder containing the images
folder_path = 'melanoma'

# List all files in the folder
image_files = os.listdir(folder_path)

# Filter only for image files (if needed)
image_files = [file for file in image_files if file.endswith('.jpg') or file.endswith('.png')]

# Create a DataFrame with the file names
data = pd.DataFrame({'Image File': image_files})

# Save the DataFrame to a CSV file
data.to_csv('image_files.csv', index=False)
