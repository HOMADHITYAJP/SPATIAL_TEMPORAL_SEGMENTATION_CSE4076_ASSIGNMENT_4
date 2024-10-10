# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:55:42 2024

@author: homap
"""

import cv2
import os

def display_summary(detected_cuts, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    summary_image = []

    for filename, cut_type in detected_cuts:
        summary_image.append((filename, cut_type))

    print("Summary of detected cuts:")
    for filename, cut_type in summary_image:
        print(f"{filename}: {cut_type}")
