import requests
from bs4 import BeautifulSoup
import os
from threading import Thread
from pathlib import Path


host_refer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'https://hotgirl.biz'
}
pic_refer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'https://hotgirl.biz'
}

dir_pic_download = '/Users/edgar/Downloads/'


def crawl_pic_from():
    for i in range(100, 150):
        url = 'https://hotgirl.biz/mix-vol-%d/' % i
        name = 'mfstar-vol-%d' % i
        crawl_remote_pic(url, name)


def crawl_remote_pic(url, name):
    start_html = requests.get(url, headers=host_refer)
    soup = BeautifulSoup(start_html.text, "html.parser")
    all_a = soup.find('div', class_='thecontent').find_all('a')
    if not all_a:
        print("not content link pic ")
        return
    list_pic = []
    for link in all_a:
        list_pic.append(link.get('href'))
    fold = Path(dir_pic_download + name)
    if not fold.exists():
        os.makedirs(dir_pic_download + name)
    download_list_pic(dir_pic_download + name, list_pic)


def download_list_pic(fold, list_pic):
    index = 0
    threads = []
    for img_url in list_pic:
        if index > 0:
            path = "%s/%d.jpg" % (fold, index)
            # download_pic(img_url, path)
            t = Thread(target=download_pic, args=(img_url, path))
            threads.append(t)
        index = index + 1
    for t in threads:
        t.start()
    for th in threads:
        th.join()


def download_pic(img_url, path):
    image = requests.get(img_url)
    with open(path, "wb") as f:
        f.write(image.content)


if __name__ == '__main__':
    crawl_pic_from()
