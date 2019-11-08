from bs4 import BeautifulSoup
import requests
import urllib3

song = str(input("Enter the name of the song:  ")).lower()
artist = str(input("Enter the name of the artist:  ")).lower()

if artist[:4] == 'the ':
        artist = artist[4:]


processed_artist = ''
processed_song = ''

for i in range(len(artist)):
    if artist[i] != ' ' and artist[i] != '.' and artist[i] != r"'":
        processed_artist = processed_artist + artist[i]

for i in range(len(song)):
    if song[i] != ' ' and song[i] != '.' and song[i] != r"'":
        processed_song = processed_song + song[i]

url = 'https://www.azlyrics.com/lyrics/' + processed_artist + '/' + processed_song + '.html'
print(url)
print("Click the link above to visit website.")
print('\n' + song.upper() + ' BY ' + artist.upper() + ':')
response = requests.get(url)
content = BeautifulSoup(response.content, 'html.parser')

lyrics = content.find('div',class_='col-xs-12 col-lg-8 text-center').find_all('div')
processed_lyrics = []

for i in range(len(lyrics)):
        text = lyrics[i].get_text()
        text = text.strip()
        processed_lyrics.append(text)

for i in range(len(processed_lyrics)):
        if len(processed_lyrics[i]) > 150:
                print('\n\n')
                print(processed_lyrics[i])
                break