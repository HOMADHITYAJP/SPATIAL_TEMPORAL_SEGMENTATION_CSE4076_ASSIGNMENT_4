# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:50:30 2024

@author: homap
"""

import cv2
import numpy as np
import os

def sobel_edge_detection(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
            img = img.astype(np.float32)

            grad_x = cv2.filter2D(img, -1, sobel_x)
            grad_y = cv2.filter2D(img, -1, sobel_y)
            
            sobel_combined = np.sqrt(grad_x**2 + grad_y**2)
            sobel_normalized = cv2.convertScaleAbs(sobel_combined)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, sobel_normalized)

    print(f"Sobel edge detection frames saved to {output_folder}")

