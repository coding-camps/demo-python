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

    def __str__(self):
        return super(self.__class__).to_str()
        # return str(super(Link, self))