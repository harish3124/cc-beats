from bs4 import BeautifulSoup
import requests

def init():
    # library will be a dict of index:(url, attribution_text)
    library = {}
    index = 0

    base_url = "https://ncs.io/music-search?q=&genre=&mood=&version=regular-instrumental&page={}"
    base_attr_text = "Song: {} - {} Music provided by NoCopyrightSounds \n Free Download/Stream: http://ncs.io{}"

    page_no = 1
    while True:
        page = requests.get(base_url.format(page_no))
        soup = BeautifulSoup(page.text, 'html.parser')

        try:
            table = soup.find_all('tbody')[1]
            for song in table.find_all('tr'):
                song_details = song.find_all('td')[3]
                name = song_details.find('p').text
                artist = song_details.find('span').text
                href = song_details.find('a').get('href')

                url = song.find('td').a.get('data-url')

                attribution_text = base_attr_text.format(name, artist, href, href)
                library[index] = (url, attribution_text)
                index += 1

        except:
            break

        print("page no:", page_no)
        page_no += 1

    print(len(library))

    return library
