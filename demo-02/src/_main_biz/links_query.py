# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from common.db_config import DbConfig
from common.orm_models import Link

if __name__ == '__main__':
    print("hello world")
    url = DbConfig().get_url()

    engine = create_engine(url, echo=True, future=True)

    links = None
    with Session(engine) as session:
        links = session.query(Link).all()

    for i, link in enumerate(links):
        print(i, link)
        # print(i, link.to_json())
