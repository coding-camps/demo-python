# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from mysql_orm import Book

if __name__ == '__main__':
    config = {
        'dialect': 'mysql',
        'driver': 'mysqlconnector',
        'user': 'qdm673522401',
        'password': 'Zhao123123',
        'host': 'qdm673522401.my3w.com',
        'port': 3306,
        'database': 'qdm673522401_db'
    }
    url = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}'.format(**config)
    print(url)
    engine = create_engine(url, echo=True, future=True)
    # DBsession = sessionmaker(bind=engine)
    # session = DBsession()
    # books = session.query(Book).limit(3)
    # for book in books:
    #     print(book)

    stmt = (
        select(Book)
    )
    books = None
    with Session(engine) as session:
        books = session.execute(stmt);
        # books = session.execute(stmt).all()
        books2 = session.query(Book).where(Book.press == '崇文书局')
    for i, book in enumerate(books):
        print(i + 1, book)
    for i, book in enumerate(books2):
        print(i + 1, book)
