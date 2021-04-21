# -*- coding: utf-8 -*-

import re
import time
import requests


class Getfile(object):  #下载文件

    def __init__(self,url):
        self.url=url

    def getheaders(self):
        try:
            r = requests.head(self.url)
            headers =  r.headers
            return headers
        except:
            print('无法获取下载文件大小')
            exit()

    def getfilename(self):  #获取默认下载文件名
        if 'Content-Disposition' in self.getheaders():
            print(self.getheaders())
            file = self.getheaders().get('Content-Disposition')
            filename = re.findall('filename="(.*)"',file)
            if filename:
                print(filename)
                return filename[0]

    def downfile(self,filename):  #下载文件
        self.r = requests.get(self.url,stream=True)
        with open(filename, "wb") as code:
            for chunk in self.r.iter_content(chunk_size=1024): #边下载边存硬盘
                if chunk:
                    code.write(chunk)
        time.sleep(1)


if __name__ == '__main__':
    # <a href="https://sm.ms/image/Lkvitbn8NpFwms5" target="_blank"><img src="https://i.loli.net/2021/04/07/Lkvitbn8NpFwms5.jpg" alt="01d01.jpg"></a>
    url = 'https://i.loli.net/2021/04/07/Lkvitbn8NpFwms5.jpg'

    # filename = Getfile(url).getfilename()
    # filename = "abc.jpg"
    # Getfile(url).downfile(filename)
    resp = requests.get(url)
    img = resp.content
    with open('a.jpg', 'wb') as f:
        f.write(img)