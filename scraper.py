import requests
from bs4 import BeautifulSoup

# URL for the song lyrics on azlyrics.com
# Bille Jean for the example xD, can be anyone song you want to fetch

url = "https://www.azlyrics.com/lyrics/michaeljackson/billiejean.html"

# Send a GET request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the lyrics from the HTML tags
lyrics_div = soup.find('div', class_='col-xs-12 col-lg-8 text-center')
lyrics = lyrics_div.find_all('div')[6].get_text()

# Print the lyrics
print(lyrics)
