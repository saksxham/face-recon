# Facial Expression Recognition Project

This is a Python project that detects faces from your webcam and performs a simple **smile/non-smile** expression classification using OpenCV Haar cascades.

## Requirements

- Python 3.7+
- Libraries: `opencv-python`, `numpy`, `pillow`

## Setup

1. Create/activate a virtual environment (recommended):
   - Windows (PowerShell): `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run the script:
   - `python main.py`

## How it works

- Captures live video from your webcam.
- Detects faces with OpenCV Haar cascades.
- Detects smiles within the face region.
- Displays a label: **Smiling** or **Not smiling**.

## Controls

- Press **`q`** to quit the application.

## Notes

- Make sure your webcam is accessible and not used by another application.
