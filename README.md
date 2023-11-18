# Image Exif Data Remover

This Python script removes Exif data from images. Exif data often contains metadata such as camera settings, location, and other information that you may want to exclude from your images for privacy or other reasons.

## Getting Started

Usage

1. Modify the script (remove_exif.py) to specify your input and output file paths:

input_file = '/path/to/your/input/image.jpg'
output_file = '/path/to/your/output/image_without_exif.jpg'

2. Run the script:

python remove_exif.py

### Prerequisites

Make sure you have the required dependencies installed:

- [piexif](https://pypi.org/project/piexif/): A Python library to simplify working with Exif data.
- [Pillow](https://pypi.org/project/Pillow/): A powerful library for image processing.

Install the dependencies using the following command:

```bash
pip install piexif Pillow

