import requests
from pathlib import Path
from download_and_crop_image import IMAGES_DIR, download_and_crop_image


def main():
    Path(IMAGES_DIR).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(api_url)
    response.raise_for_status()
    launches = response.json()
    flickr_images = []
    for launch in reversed(launches):
        flickr_images = launch['links']['flickr_images']
        if flickr_images:
            break

    for index, image_url in enumerate(flickr_images):
        download_and_crop_image(image_url, f'spacex{index}')


if __name__ == '__main__':
    main()
