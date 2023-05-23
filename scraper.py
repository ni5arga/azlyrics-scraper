import requests
from bs4 import BeautifulSoup

url = "https://www.azlyrics.com/lyrics/michaeljackson/billiejean.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

lyrics_div = soup.find('div', class_='ringtone')
lyrics = lyrics_div.find_next_sibling('div').text.strip()

print(lyrics)
