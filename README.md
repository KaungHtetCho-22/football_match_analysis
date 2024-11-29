# Sports Analytics Video Processing System

This repository is designed for automated sports video analytics. It processes input videos, tracks players, referees, and ball positions, estimates player speeds and distances, and assigns players to teams and ball possession dynamically. Additionally, it visualizes data such as ball control percentages, transformed coordinates, and speed overlays directly onto the output video.

## Features

### 1. Object Tracking
- Detect and track players, referees, and ball positions using a YOLO-based detection model and ByteTrack tracking

### 2. Camera View Transformation
- Transforms coordinates from camera view to a normalized court view using perspective transformation

### 3. Speed and Distance Estimation
- Calculates the distance covered and speed of tracked players in meters per second (converted to km/h)

### 4. Team Assignment
- Dynamically assigns players to teams based on uniform colors

### 5. Ball Possession Detection
- Identifies which player and team currently possess the ball

### 6. Visualization
- Draws bounding boxes, ellipses, and triangles to represent players, referees, and ball positions
- Displays team ball possession statistics as a percentage on the output video
- Annotates player speeds and distances directly onto the video

## Installation
[Add installation instructions here]

## Usage
[Add usage instructions here]

## Dependencies
[List required libraries and dependencies]

## Contributing
[Add contribution guidelines]

## License
[Specify the license]