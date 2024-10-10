# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:59:29 2024

@author: homap
"""

import cv2
import os

def track_objects(input_folder, output_folder, min_box_size=40):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            frame = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
            _, thresh = cv2.threshold(frame, 50, 255, cv2.THRESH_BINARY)

            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            frame_color = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w > min_box_size and h > min_box_size:
                    cv2.rectangle(frame_color, (x, y), (x + w, y + h), (255, 0, 0), 2) 

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, frame_color)

    print(f"Bounding boxes saved to {output_folder}")



