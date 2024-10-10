# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:48:29 2024

@author: homap
"""
# annotate_cuts.py

import cv2
import os
def annotate_frames_with_cuts(input_folder, detected_cuts, output_folder):
    for frame_name, cut_type in detected_cuts:
        frame_path = os.path.join(input_folder, frame_name)
        frame = cv2.imread(frame_path)

        # Add text annotation for cut type (hardcut or softcut)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 255) if cut_type == "hard" else (0, 255, 255)  # Red for Hardcut, Yellow for Softcut
        cv2.putText(frame, cut_type.capitalize(), (50, 50), font, 1, color, 2, cv2.LINE_AA)

        # Save the annotated frame
        output_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(output_path, frame)

        print(f"Annotated {frame_name} with {cut_type} and saved to {output_folder}")
