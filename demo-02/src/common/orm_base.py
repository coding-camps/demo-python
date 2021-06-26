# -*- coding: utf-8 -*-

import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from common.db_config import DbConfig
from abc import ABCMeta, abstractmethod, abstractproperty

# echo参数为False时,表示不打印sqlalchemy日志,True则打印 ( 建议设置为False关闭掉,不然会有非常多的日志信息 )
engine = create_engine(DbConfig().get_url(), echo=False, future=True)
base = declarative_base()


class BaseModel(base):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


def to_str(self: BaseModel.__class__) -> str:
    item = self.__dict__.copy()
    item.pop('_sa_instance_state')
    # return json.dumps(item, indent=4, ensure_ascii=False, separators=(',', ':'))
    strx = json.dumps(item, indent=4, ensure_ascii=False, separators=(',', ':'))
    print(type(strx))
    return strx
