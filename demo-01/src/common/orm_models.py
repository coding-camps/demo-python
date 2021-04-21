# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from common.orm_base import BaseModel


class Link(BaseModel.base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    title = Column(String(100))
    tag = Column(String(100))
    status = Column(String(100))

    # def __str__(self) -> str:
    #     item = self.__dict__.copy()
    #     item.pop('_sa_instance_state')
    #     return json.dumps(item, indent=4, ensure_ascii=False, separators=(',', ':'))

    # def __init__(self, **items):
    #     for key in items:
    #         if hasattr(self, key):
    #             setattr(self, key, items[key])
