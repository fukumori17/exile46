#!/usr/bin/env python
#
# data_preparation.py
#
# Created by Kosuke FUKUMORI on 2021/03/31
#

import requests
import re
import os
from bs4 import BeautifulSoup


def get_all_imgs():
    image_save_dir = 'imgs'
    get_nogi_imgs(image_save_dir)
    get_exile_imgs(image_save_dir)

def get_nogi_imgs(image_save_dir='imgs'):
    nogi_jpg_dir = os.path.join(image_save_dir, 'nogi')
    os.makedirs(nogi_jpg_dir, exist_ok=True)

    nogi_top_url = 'http://www.nogizaka46.com/member'
    nogi_thumb_base_url = 'https://img.nogizaka46.com/www/member/img/{}_prof.jpg'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3864.0 Safari/537.36'}

    html = requests.get(nogi_top_url, headers=headers)
    bs = BeautifulSoup(html.content, 'html.parser')
    elements = bs.find_all(href=re.compile('./detail/'))
    len(elements)

    for i, e in enumerate(elements):
        name = e.img['class'][0]
        thumb_url = nogi_thumb_base_url.format(name)
        jpg_res = requests.get(thumb_url)
        file_name = os.path.join(nogi_jpg_dir, f'{i:02d}.jpg')
        with open(file_name, 'wb') as f:
            f.write(jpg_res.content)
            print(f'Saved {file_name}')
        
def get_exile_imgs(image_save_dir='imgs'):
    exile_jpg_dir = os.path.join(image_save_dir, 'exile')
    os.makedirs(exile_jpg_dir, exist_ok=True)
    exile_top_url = 'https://exile.jp/profile'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3864.0 Safari/537.36'}
    html = requests.get(exile_top_url, headers=headers)
    bs = BeautifulSoup(html.content, 'html.parser')
    elements = bs.find_all(href=re.compile('./member.php'))
    for i, e in enumerate(elements):
        thumb_url = e.img['src']
        jpg_res = requests.get(thumb_url)
        file_name = os.path.join(exile_jpg_dir, f'{i:02d}.jpg')
        with open(file_name, 'wb') as f:
            f.write(jpg_res.content)
            print(f'Saved {file_name}')
