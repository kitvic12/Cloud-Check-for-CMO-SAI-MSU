import requests
import time
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

from checker import analyze

def get_image_url(main_url="https://cmo-env.sai.msu.ru/allsky/"):
    response = requests.get(main_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tag = soup.find('img', {'alt': 'last frame'})
    relative_url = img_tag['src']
    base_url = main_url.rstrip('/')
    return f"{base_url}{relative_url}"


def get_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

def main():
    while True:
        image_url = get_image_url()
        image = get_image(image_url)
        if image:
            resp = analyze(image)
            print(f"{resp:.1f}%")
            time.sleep(240)
            continue
        print("GG")
        continue

if __name__ == "__main__":
    main()