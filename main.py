# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:05:23 2024

@author: homap
"""


import os
from extract_frames import extract_frames
from sobel_edge_detection import sobel_edge_detection
from draw_bounding_boxes import draw_bounding_boxes  
from foreground_background_segmentation import foreground_background_segmentation
from shade_consistent_regions import shade_consistent_regions
from histogram_analysis import compare_histograms_and_detect_cuts
from annotate_cuts import annotate_frames_with_cuts
from display_summary import display_summary

# Define paths
video_path = "sample.mp4"
frames_folder = "vid2frame"  
sobel_output_folder = "segframe"
bounding_boxes_folder = "segboundframe"
original_bounding_boxes_folder = "ogboundframe"  
segmentation_folder = "forebacksegframe"
shaded_regions_folder = "consistent_regions"
histogram_folder = "histograms"
cut_annotations_folder = "cut_annotation_frames"  
cut_summary_folder = "summary"

# Step 1: Extract frames
extract_frames(video_path, frames_folder)

# Step 2: Sobel edge detection
sobel_edge_detection(frames_folder, sobel_output_folder)

# Step 3: Track and draw bounding boxes on segmented and original frames
draw_bounding_boxes(frames_folder, sobel_output_folder, bounding_boxes_folder, original_bounding_boxes_folder)

# Step 4: Foreground-background segmentation
foreground_background_segmentation(frames_folder, segmentation_folder)

# Step 5: Shade consistent regions
shade_consistent_regions(frames_folder, segmentation_folder, shaded_regions_folder)

# Step 6: Compare histograms and detect cuts
detected_cuts = []
compare_histograms_and_detect_cuts(frames_folder, histogram_folder, (0.5, 0.8), cut_annotations_folder, detected_cuts)  

# Step 7: Annotate frames with detected cuts
annotate_frames_with_cuts(frames_folder, detected_cuts, cut_annotations_folder)

# Step 8: Display summary
display_summary(detected_cuts, cut_summary_folder)
