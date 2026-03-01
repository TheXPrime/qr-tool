# QR Tool

A simple desktop QR utility built with **Python + Tkinter** for creating and scanning QR codes.

## Features

- Generate QR codes from text or links.
- Scan QR codes from image files (`.png`, `.jpg`, `.jpeg`).
- Scan QR codes live from your camera.
- Automatically saves generated codes to `data/output/`.

## Project Structure

- `main.py` — GUI application (generator + image scanner + camera scanner).
- `requirements.txt` — pinned Python dependencies.
- `build.bat` — Windows build script for generating `dist/qr-tool.exe`.

## Requirements

- Python **3.10+**
- A working webcam (for camera scanning)
- The app uses OpenCV's built-in QR detector, avoiding external `pyzbar` DLL dependencies in frozen builds.

## Quick Start (Run from Source)

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

## Build Windows Executable

```bat
build.bat
```

After a successful build, the executable is available at:

```text
dist/qr-tool.exe
```

## Usage

### 1) Generate QR

1. Enter text or URL in **Text / Link**.
2. Optionally enter an output filename.
3. Click **Generate**.
4. Output is saved in `data/output/`.

### 2) Scan from Image

1. Click **Browse** and select a QR image.
2. Click **Scan**.
3. Decoded content appears in the result box.

### 3) Scan from Camera

1. Click **Camera Scan**.
2. Present a QR code to the camera.
3. Press **ESC** to close camera window manually.

## Notes

- Default output filename is `qr.png` when no filename is provided.
- For longer content, the app adjusts QR generation parameters automatically.
