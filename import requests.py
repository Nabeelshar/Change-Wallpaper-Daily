import requests
from bs4 import BeautifulSoup
import os
import lxml
import random
def photo_downloader(url):
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image")
    count =0
    os.chdir('.\images')
    for i in all_image:
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href']
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(f'{count}.jpg','wb') as photo:
                photo.write(photo_bytes.content)
                count +=1

    print("Done")



words = ["4k-wallper","wallpaper","space-wallpaper","nature-wallpaper","building-wallpaper"]

words = random.choice(words)

if __name__ == "__main__":
    photo_downloader("https://unsplash.com/s/photos/" + words )