# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:42:54 2024

@author: homap
"""

import cv2
import os

def extract_frames(video_path, output_folder, fps=2):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vidcap = cv2.VideoCapture(video_path)
    total_fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(total_fps // fps)

    success, image = vidcap.read()
    count = 0
    frame_count = 0

    while success:
        if count % frame_interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
            cv2.imwrite(frame_path, image)
            frame_count += 1

        success, image = vidcap.read()
        count += 1

    vidcap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")


