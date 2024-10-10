# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:27:54 2024

@author: homap
"""

import cv2
import os

def shade_consistent_regions(original_folder, seg_mask_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_list = sorted(os.listdir(original_folder))
    prev_frame = None

    for idx in range(len(frame_list)):
        if frame_list[idx].endswith(".png"):
            original_frame = cv2.imread(os.path.join(original_folder, frame_list[idx]))
            current_frame = cv2.imread(os.path.join(seg_mask_folder, frame_list[idx]), cv2.IMREAD_GRAYSCALE)

            if prev_frame is None:
                prev_frame = current_frame
                continue

            consistent_regions = (current_frame == prev_frame)

            shaded_frame = original_frame.copy()
            shaded_frame[consistent_regions] = [0, 255, 0]

            output_path = os.path.join(output_folder, frame_list[idx])
            cv2.imwrite(output_path, shaded_frame)

            prev_frame = current_frame

    print(f"Shaded consistent regions saved to {output_folder}")
