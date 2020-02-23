from os.path import join
from PIL import Image
import requests

IMAGES_DIR = "images"


def download_and_crop_image(image_url, file_name):
    file_extension = get_extension(image_url)
    download_image(image_url, join(IMAGES_DIR, f'{file_name}.{file_extension}'))
    crop_to_square(join(IMAGES_DIR, f'{file_name}.{file_extension}'),
                   join(IMAGES_DIR, f'{file_name}.square.jpg'))


def get_extension(path: str):
    return path.split('.')[-1]


def download_image(url, path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def crop_to_square(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert('RGB')
    if image.width < image.height:
        margin = int((image.height - image.width) / 2)
        coordinates = (0, margin, image.width, margin + image.width)
    else:
        margin = int((image.width - image.height) / 2)
        coordinates = (margin, 0, margin + image.height, image.height)

    cropped = image.crop(coordinates)
    cropped.save(output_path)
