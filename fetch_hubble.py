import requests
from pathlib import Path
from download_and_crop_image import IMAGES_DIR, download_and_crop_image


def main():
    Path(IMAGES_DIR).mkdir(parents=True, exist_ok=True)
    fetch_hubble_images_from_collection('stsci_gallery')


def fetch_hubble_images_from_collection(collection):
    api_url = f'http://hubblesite.org/api/v3/images?page=all&collection_name={collection}'
    response = requests.get(api_url)
    response.raise_for_status()
    for image in response.json():
        fetch_hubble_image_by_id(image['id'])


def fetch_hubble_image_by_id(image_id):
    api_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(api_url)
    response.raise_for_status()
    image_details = response.json()
    file_url = image_details['image_files'][-1]['file_url']
    download_and_crop_image(f'http:{file_url}', f'image_{image_id}')


if __name__ == '__main__':
    main()