#!/usr/bin/env python3

import os
import sys
from PIL import Image, ExifTags, ImageFile

EXTENSIONS = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"]

def pexit_exif_print(image):
    exif_data = image._getexif()
    if exif_data is not None:
        print("~ EXIF present on " + image.filename)
        for tag, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            print(f"{tag_name}: {value}")
    else:
        print("! no EXIF data present on " + image.filename)

def pexit_exif_remove(image: ImageFile):
    if "exif" in image.info:
        print("Getting copy of image with no EXIF data")
        image_without_exif = image.copy()
        return image_without_exif
    else:
        print("! no EXIF data present on " + image)
        return image

def pexit_process_remove(image_path):
    image_without_exif = None
    try:
        with Image.open(image_path) as image:
            pexit_exif_print(image)
            image_without_exif = pexit_exif_remove(image)

        image_without_exif.save(image_path)
        print("+ new image saved at " + image_path + '\n')

        with Image.open(image_path) as modified_image:
            print(" — removed EXIF data from "+ image_path + '\n')
            pexit_exif_print(modified_image)

    except FileNotFoundError:
        print("! file was not found, verify this file exists: " + image_path)
    except PermissionError:
        print("! you do not have permission to access this file: " + image_path)
    except IOError:
        print("! an error occurred trying to open this file: " + image_path)
    except Exception as e:
        print("! unexpected error: ", exc_info=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("! no file paths provided. Please provide at least one image file path.")
        sys.exit(1)
    image_paths = sys.argv[1:]
    for image_path in image_paths:
        pexit_process_remove(image_path)