# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from common.orm_base import BaseModel
from common.db_config import DbConfig


class DbUtils(object):
    def __init__(self, model):
        self.model = model
        self.model.metadata.create_all(BaseModel.engine)
        # self.session = sessionmaker(bind=BaseModel.engine)()

    def write(self, items):
        self.session = sessionmaker(bind=BaseModel.engine)()
        try:
            data = self.model(**items)
            self.session.add(data)
            self.session.commit()
        except():
            self.session.rollback()
        finally:
            self.session.close()

    def read_all(self):
        url = DbConfig().get_url()
        self.engine = create_engine(url, echo=True, future=True)
        with Session(self.engine) as session:
            return session.query(self.model).all()
