# -*- coding: utf-8 -*-

import json
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    version = Column(String(100))
    authors = Column(String(100))
    press = Column(String(100))
    my_comment: str = Column('comments', String(300))
    type1 = Column('type1', String(30))
    type2 = Column('type2', String(30))
    status = Column(String(20))

    def __repr__(self):
        item = self.__dict__.copy()
        item.pop('_sa_instance_state')
        return json.dumps(item, indent=4, ensure_ascii=False, separators=(',', ':'))


class ImageItem(Base):
    __tablename__ = 'host_images'

    id = Column(Integer, primary_key=True)
    width = Column(Integer)
    # "width": 5400,
    # "height": 3600,3.
    # "filename": "ycc.jpg",
    # "storename": "zBobXF6wgdPKhcp.jpg",
    # "size": 3383033,
    # "path": "/2021/04/07/zBobXF6wgdPKhcp.jpg",
    # "hash": "MDmsp29hcofOXLxeYiykj7nQHS",
    # "created_at": 1617727812,
    # "url": "https://i.loli.net/2021/04/07/zBobXF6wgdPKhcp.jpg",
    # "delete": "https://sm.ms/delete/MDmsp29hcofOXLxeYiykj7nQHS",
    # "page": "https://sm.ms/image/zBobXF6wgdPKhcp"
