import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request
import os
import ssl
import time
from PIL import Image
import bs4
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.foxsports.com/mlb/players?teamId=0&season=2019&position=0&page={}&country=0&grouping=0&weightclass=0'

# urlを読み込んで、そのページのhtml要素を返す。
def get_hp(url):
    res = requests.get(url)
    res.raise_for_status() # エラーならここで例外を発生させる
    return res.text


# urlのページから写真のurlと選手の名前を取り出す。
def get_image_url(url):
    soup = BeautifulSoup(get_hp(url), 'lxml')
    photo = soup.select('#wisfoxbox > section.wisbb_top > section > div.wisbb_bioContent > div.wisbb_bioLargeHeadshot > img')
    photo = photo[0]
    photo_url = photo.get('src')
    photo_name = photo.get('alt')
    return photo_url, photo_name


# 選手一覧のページから各選手へ繋がるurlを取得する。
def get_player_url_list(url):
    player_url_list = []
    soup = BeautifulSoup(get_hp(url), 'lxml')
    players = soup.select('#wisfoxbox > section.wisbb_body > div > div.wisbb_playersTable > div > table > tbody > tr')
    for player in players:
        draft = player.findAll('td')[3].string
        if draft != 'Undrafted':
            player_url = player_url_list.append(player.find('a').get('href'))
    return player_url_list


# Half_or_Pure_appフォルダ内に選手画像を保存する。
def save_player_photo(url):
    url_list = get_player_url_list(url)
    os.chdir("/Users/k.masuda/Desktop/Half_or_Pure_app/Not_Japanese_men")
    for i in url_list:
        time.sleep(0.5)
        url0 = 'https://www.foxsports.com/' + i
        img_url, image_name = get_image_url(url0)
        if img_url == "#":
            break
        print(image_name)
        img = urllib.request.urlopen(img_url).read()
        with open('{}.jpg'.format(image_name), 'wb') as file:
            file.write(img)


for i in range(76, 100):
    url = 'https://www.foxsports.com/mlb/players?teamId=0&season=2019&position=0&page={}&country=0&grouping=0&weightclass=0'.format(i)
    print(url)
    save_player_photo(url)
    time.sleep(10)



