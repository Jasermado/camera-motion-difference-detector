# Camera Motion Difference Detector

A simple Python and OpenCV project that detects motion by comparing consecutive camera frames.

## Description

This program uses your camera as input and displays a black-and-white window that shows only the parts of the frame that changed.

If nothing is moving, the window stays mostly black. If something moves, the changed area appears white.

## Features

- Opens your camera or webcam
- Reads frames from the camera
- Converts frames to grayscale
- Blurs frames to reduce noise
- Compares each frame with the previous frame
- Displays the difference as a black-and-white motion mask
- Closes when you press `q`

## Requirements

- Python 3
- OpenCV
- A working camera or webcam

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install OpenCV directly:

```bash
pip install opencv-python
```

## Usage

Run the program:

```bash
python main.py
```

If that does not work, try:

```bash
python3 main.py
```

## Camera Not Working?

If the camera does not open, change the camera index in the code.

For example, change:

```python
cap = cv2.VideoCapture(1)
```

to:

```python
cap = cv2.VideoCapture(0)
```

You can also try `2` if you have more than one camera.

## How to Close

Press `q` to close the program.
