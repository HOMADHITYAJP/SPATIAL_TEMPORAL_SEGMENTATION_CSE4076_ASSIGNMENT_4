# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:07:25 2024

@author: homap
"""
import cv2
import os

# draw_bounding_boxes.py
def draw_bounding_boxes(input_folder, seg_bound_folder, output_folder, original_output_folder, min_box_size=40):
    if not os.path.exists(seg_bound_folder):
        os.makedirs(seg_bound_folder)
        
    if not os.path.exists(original_output_folder):
        os.makedirs(original_output_folder)

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            original_frame = cv2.imread(os.path.join(input_folder, filename))
            seg_bound_frame = cv2.imread(os.path.join(seg_bound_folder, filename))

            gray_seg = cv2.cvtColor(seg_bound_frame, cv2.COLOR_BGR2GRAY)
            _, thresh_seg = cv2.threshold(gray_seg, 50, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh_seg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw bounding boxes on original frames
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w > min_box_size and h > min_box_size:
                    cv2.rectangle(original_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Save original frame with bounding boxes
            original_output_path = os.path.join(original_output_folder, filename)
            cv2.imwrite(original_output_path, original_frame)

            # Save the Sobel edge-detected frame with bounding boxes
            seg_bound_color = cv2.cvtColor(gray_seg, cv2.COLOR_GRAY2BGR)  # Convert to BGR for color bounding boxes
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w > min_box_size and h > min_box_size:
                    cv2.rectangle(seg_bound_color, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Save segmented frame with bounding boxes
            seg_bound_output_path = os.path.join(seg_bound_folder, filename)
            cv2.imwrite(seg_bound_output_path, seg_bound_color)

    print(f"Bounding boxes on Sobel and original frames saved to {seg_bound_folder} and {original_output_folder}")
