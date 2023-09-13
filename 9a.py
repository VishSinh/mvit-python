import os
import requests
from bs4 import BeautifulSoup

url = 'https://xkcd.com/1/'
os.makedirs('xkcd_comics', exist_ok=True)

while url:
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    comic_elem = soup.select_one('#comic img')

    if comic_elem:
        comic_url = f"https:{comic_elem['src']}"
        print(f"Downloading {comic_url}...")
        
        res = requests.get(comic_url)
        res.raise_for_status()
        
        with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as img_file:
            img_file.write(res.content)
    else:
        print('Could not find comic image.')
    
    prev_link = soup.select_one('a[rel="prev"]')
    url = f"https://xkcd.com{prev_link['href']}" if prev_link else None

print('All comics downloaded.')
