# -*- coding: utf-8 -*-

import json


class DbConfig(object):
    _url_tmp = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}'

    def __init__(self):
        self.config = {
            'dialect': 'mysql',
            'driver': 'mysqlconnector',
            'user': 'root',
            'password': 'root',
            'host': '127.0.0.1',
            'port': 3306,
            'database': 'store',
            'charset': 'utf8mb4'
        }
        self._init_url()

    def _init_url(self):
        self.url = self._url_tmp.format(**self.config)

    def set_config(self, config):
        self.config = config
        self._init_url()

    def get_url(self):
        return self.url

    def __str__(self):
        return json.dumps({'config': self.config, 'url': self.url}, indent=4, ensure_ascii=False, separators=(',', ':'))
