# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:39:09 2024

@author: homap
"""

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def calculate_histogram(image, bins=256):
    hist = cv2.calcHist([image], [0], None, [bins], [0, 256])
    return cv2.normalize(hist, hist).flatten()

def histogram_intersection_score(hist1, hist2):
    intersection = np.minimum(hist1, hist2)
    return np.sum(intersection) / np.sum(hist1)

def plot_histogram(hist, title, color, save_path):
    plt.figure()
    plt.plot(hist, color=color)
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.savefig(save_path)
    plt.close()

def compare_histograms_and_detect_cuts(input_folder, hist_folder, cut_thresholds, cut_annotation_folder, detected_cuts):
    if not os.path.exists(hist_folder):
        os.makedirs(hist_folder)
    
    if not os.path.exists(cut_annotation_folder):
        os.makedirs(cut_annotation_folder)

    prev_frame = None
    prev_frame_path = None  # Initialize prev_frame_path here
    threshold_hardcut, threshold_softcut = cut_thresholds

    for idx, filename in enumerate(sorted(os.listdir(input_folder))):
        if filename.endswith(".png"):
            current_frame = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)

            current_hist = calculate_histogram(current_frame)

            hist_plot_path = os.path.join(hist_folder, f"hist_{filename}.png")
            plot_histogram(current_hist, f'Histogram of {filename}', 'blue', hist_plot_path)

            if prev_frame is not None:
                prev_hist = calculate_histogram(prev_frame)
                score = histogram_intersection_score(prev_hist, current_hist)
                print(f"Cut score between {os.path.basename(prev_frame_path)} and {filename}: {score:.4f}")

                if score < threshold_hardcut:
                    cut_type = "hard"
                    detected_cuts.append((filename, cut_type))
                elif score < threshold_softcut:
                    cut_type = "soft"
                    detected_cuts.append((filename, cut_type))

            prev_frame = current_frame
            prev_frame_path = os.path.join(input_folder, filename)  # Update prev_frame_path here

    print(f"Histogram analysis completed. Detected cuts: {detected_cuts}")
