# -*- coding: utf-8 -*-

import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from common.db_config import DbConfig

dbConfig = DbConfig()

class BaseModel:
    """
    DB_USER:数据库用户名
    DB_PASSWORD:数据库用户密码
    DB_HOST:数据库连接地址
    """
    # echo参数为False时,表示不打印sqlalchemy日志,True则打印 ( 建议设置为False关闭掉,不然会有非常多的日志信息 )
    # engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4', echo=False)
    engine = create_engine(dbConfig.get_url(), echo=False, future=True)
    base = declarative_base()


def __repr__(orm_obj: BaseModel.base) -> str:
    item = orm_obj.__dict__.copy()
    item.pop('_sa_instance_state')
    return json.dumps(item, indent=4, ensure_ascii=False, separators=(',', ':'))
