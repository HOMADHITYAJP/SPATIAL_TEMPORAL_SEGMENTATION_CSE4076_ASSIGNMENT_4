# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 19:30:14 2024

@author: homap
"""

import cv2
import os
import matplotlib.pyplot as plt

# Define the paths to the annotation and segmentation folders
cut_annotation_folder = 'cut_annotation_frames'
segmentation_folder = 'segframe'
output_folder = 'result_visualization'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to display images
def display_images(images, titles=None):
    n = len(images)
    plt.figure(figsize=(15, 5))
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        if titles:
            plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Load and display annotated frames
cut_frames = [f for f in os.listdir(cut_annotation_folder) if f.endswith('.png')]
segmented_frames = [f for f in os.listdir(segmentation_folder) if f.endswith('.png')]

# Retrieve and save annotated and segmented frames together
for cut_frame in cut_frames:
    # Load the cut annotated frame
    cut_frame_path = os.path.join(cut_annotation_folder, cut_frame)
    cut_image = cv2.imread(cut_frame_path)

    # Load the corresponding segmented frame (assuming naming convention matches)
    seg_frame_path = os.path.join(segmentation_folder, cut_frame)
    seg_image = cv2.imread(seg_frame_path)

    # Check if both images were loaded successfully
    if cut_image is not None and seg_image is not None:
        # Save the images together
        combined_image = cv2.hconcat([cut_image, seg_image])
        output_path = os.path.join(output_folder, f'visualization_{cut_frame}')
        cv2.imwrite(output_path + '_combined.png', combined_image)

        # Optionally display the combined image
        display_images([combined_image], titles=[f'Combined Visualization: {cut_frame}'])

# Function to visualize soft cuts and hair cuts
def visualize_cuts(cut_type='soft'):
    # Define paths for soft cuts and hair cuts
    cut_frames = [f for f in os.listdir(cut_annotation_folder) if cut_type in f and f.endswith('.png')]
    


    # Visualize each cut frame
    for cut_frame in cut_frames:
        cut_frame_path = os.path.join(cut_annotation_folder, cut_frame)
        cut_image = cv2.imread(cut_frame_path)

        if cut_image is not None:
            plt.figure(figsize=(8, 4))
            plt.imshow(cv2.cvtColor(cut_image, cv2.COLOR_BGR2RGB))
            plt.title(f'{cut_type.capitalize()} Cut: {cut_frame}')
            plt.axis('off')
            plt.show()


# Show visualizations for soft cuts and hair cuts
visualize_cuts(cut_type='soft')
visualize_cuts(cut_type='hair')

print("Result visualization completed and saved to:", output_folder)
