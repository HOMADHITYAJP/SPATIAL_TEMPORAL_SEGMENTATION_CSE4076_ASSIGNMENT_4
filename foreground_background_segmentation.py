# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:14:45 2024

@author: homap
"""

import cv2
import os

def foreground_background_segmentation(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    backSub = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            frame = cv2.imread(os.path.join(input_folder, filename))
            fg_mask = backSub.apply(frame)

            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, fg_mask)

    print(f"Foreground-background segmented frames saved to {output_folder}")
