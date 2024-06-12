# Augmented-Reality

# Augmented Reality Poster Placement

This project demonstrates the use of OpenCV and ArUco markers to place a poster image accurately within a classroom image by detecting markers and performing perspective transformations.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Details](#algorithm-details)
  - [ArUco Marker Detection](#aruco-marker-detection)
  - [Poster Perspective Transformation](#poster-perspective-transformation)
  - [Image Merging](#image-merging)
- [Results](#results)
- [Contributing](#contributing)


## Introduction

This project aims to blend virtual objects with the physical environment by overlaying a poster onto a classroom wall. The poster is accurately positioned using ArUco markers for reference, ensuring correct perspective and placement.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sushantchoraghe/Augmented-Reality.git
    cd Augmented-Reality
    ```

2. Install the required libraries:
    ```sh
    pip install opencv-python-headless numpy
    ```

## Usage

1. Place your classroom image and poster image in the project directory.
2. Update the image file paths in the script if necessary.
3. Run the script:
    ```sh
    python main.py
    ```

## Algorithm Details

### ArUco Marker Detection

The script detects ArUco markers in the classroom image using OpenCV's `cv2.aruco.detectMarkers()` function. The markers are used as reference points for placing the poster.

### Poster Perspective Transformation

A smaller portion of the poster is calculated, and a perspective transformation matrix is created to map the poster onto the classroom image accurately.

### Image Merging

The transformed poster is merged with the classroom image. The area of the poster is blacked out in the classroom image, and the transformed poster is overlaid in its place.

## Results

The final image with the correctly placed poster is saved and displayed.

![Sample Result](sample_result.jpg)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

