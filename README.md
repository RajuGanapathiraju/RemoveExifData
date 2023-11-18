# Image Exif Data Remover

This Python script removes Exif data from images. Exif data often contains metadata such as camera settings, location, and other information that you may want to exclude from your images for privacy or other reasons.

## Dependencies

- [piexif](https://pypi.org/project/piexif/): A Python library to simplify working with Exif data.
- [Pillow](https://pypi.org/project/Pillow/): A powerful library for image processing.

## Usage

Install dependencies using the following command:

   ```bash
   pip install piexif Pillow

1. Modify the script to specify your input and output file paths:

input_file = '/path/to/your/input/image.jpg'
output_file = '/path/to/your/output/image_without_exif.jpg'

2. Run the script:

python image_exif_remover.py

This will read the input image, remove the Exif data, and save the new image without Exif information.





