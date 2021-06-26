# -*- coding: utf-8 -*-
import os
from common.db_utils import DbUtils
from common.orm_models import Link


def read_line_content(file):
    with open(file, 'rt') as f:
        lines = f.readlines()
        for line in lines:
            yield line.strip()


def walk_dir(dir):
    data_files = ['links.txt']
    for root, dirs, files in os.walk(dir):
        files = filter(lambda fn: fn in data_files, files)
        for file in files:
            yield os.path.join(root, file)


def is_url(url: str):
    return url.startswith("https://") or url.startswith("http://")


def is_empty(line: str):
    return len(line.strip()) == 0


def save_links():
    db = DbUtils(Link)
    p = r'./'
    for f in walk_dir(p):
        lines = read_line_content(f)
        tag = None
        url = None
        for line in lines:
            if len(line) > 1000:
                print(f, line)
            elif is_empty(line):
                tag = None
            elif not is_url(line):
                tag = line
            else:
                url = line
                item = {"url": url}
                if tag is not None:
                    item['tag'] = tag
                try:
                    print(item)
                    db.write(item)
                except BaseException:
                    print(f, item)


def read_links():
    db = DbUtils(Link)
    return db.read_all()


if __name__ == '__main__':
    links = read_links()
    for i, link in enumerate(links):
        print(i, str(link))
    # save_links()
