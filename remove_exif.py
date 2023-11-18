import piexif
from PIL import Image

def strip_exif(file_path):
    pil_image = Image.open(file_path)
    exif_data = pil_image.info.get('exif')
    

    if exif_data is not None:
        # Remove the Exif data
        exif_dict = piexif.load(exif_data)
        exif_dict.pop('exif', None)
        exif_bytes = piexif.dump(exif_dict)
        pil_image.info['exif'] = exif_bytes

    return pil_image


if __name__ == '__main__':
    input_file = '/Users/rgy/Downloads/exif_example.jpeg'
    output_file = '/Users/rgy/Downloads/exif_example_without_exif.jpeg'

    new_image = strip_exif(input_file)
    new_image.save(output_file, quality=95)
