from dotenv import load_dotenv
from instabot import Bot
from os.path import join
import os
import time
from download_and_crop_image import IMAGES_DIR


def main():
    load_dotenv()
    instalogin = os.getenv('INSTALOGIN')
    instapassword = os.getenv('INSTAPASSWORD')
    upload_photos(instalogin, instapassword)


def upload_photos(instalogin, instapassword):
    bot = Bot()
    bot.login(username=instalogin, password=instapassword)

    files = filter(lambda x: x.endswith(('.square.jpg', '.square.png')), os.listdir(IMAGES_DIR))
    for file in files:
        try:
            bot.upload_photo(join(IMAGES_DIR, file), caption="Nice pic!")
        except Exception as ex:
            print(ex)
        time.sleep(60)


if __name__ == '__main__':
    main()
