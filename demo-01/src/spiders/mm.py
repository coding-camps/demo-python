# -*- coding: utf-8 -*-
# encoding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import os

images_dir = "E:\\mmimages\\"

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


def download_images(url_sub, image_counts, start, default_counts):
    # url_sub  为图片下载其实地址
    # image_counts为共下载多少幅
    # default_counts 默认最多下载20页
    # start 从那页开始下载
    if (default_counts + start) > image_counts:
        end = image_counts
    else:
        end = default_counts + start
    # 一句话获取url 的basename
    end_path = os.path.basename(url_sub).split('.')[0]
    base_path = os.path.dirname(url_sub)
    for i in range(start - 1, end - 1):
        file_name = end_path + '_' + str(i + 1)
        url = base_path + '/' + file_name + '.htm'
        # 打开url 后，用bs 提取图片地址
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        datas = soup.select('.ImageBody > p > img')[0]
        image_url = datas.get('src')
        response = requests.get(image_url, headers=headers, stream=True)
        with open(images_dir + file_name + '.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)
        fd.close()
        print(file_name + '  finished....., please wait')


def get_image_count(soup_sub):
    # 获取图片总数
    image_nums_str = soup_sub.select('.NewPages > ul > li > a')[0]
    image_nums_str = image_nums_str.get_text()
    image_nums = int(re.findall(r"\d+\.?\d*", image_nums_str)[0])
    return image_nums


def download_sub_images(url_sub, start, default_counts):
    # 从一个子目录开始下载一套图
    page_sub = requests.get(url_sub, headers=headers)
    soup_sub = BeautifulSoup(page_sub.text, 'html.parser')
    # 1. 获取一共有多少页图片
    image_counts = get_image_count(soup_sub)
    # print image_count
    # 2. 下载图片
    download_images(url_sub, image_counts, start, default_counts)


if __name__ == '__main__':
    # 后来发现流量都是钱啊，不递归了，直接下载某个子类目吧
    # url_main = 'https://www.umei.cc/tags/BeautyLeg.htm'
    # page = requests.get(url_main, headers=headers)
    # soup = BeautifulSoup(page.text, 'html.parser')
    # links = [link.get('href') for link in soup.find_all('a', 'TypeBigPics')]
    # print links
    # url_sub = links[0]
    url_sub = raw_input(
        'please input where the first path is\n (such as https://www.umei.cc/p/gaoqing/gangtai/26056.htm)：\n >:  ')
    start = raw_input('please input start number(default is 1):  \n >:  ')
    start = 1 if not start else int(start)
    default_counts = raw_input('please input how many you want to download(default is 20):  \n >:  ')
    default_counts = 20 if not default_counts else int(default_counts)
    download_sub_images(url_sub, start, default_counts)
