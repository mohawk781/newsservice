from sqlalchemy import Column, Integer, String
from flaskr.db import Base


class News(Base):
    __tablename__ = 'News'
    id = Column('news_id', Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(50))
    time = Column(String(100))
    text = Column(String(1000))
    tag = Column(String(50))
    facilityid = Column(String(500))

    def __init__(self, title, author, time, text, tag, facilityid):
        self.title = title
        self.author = author
        self.time = time
        self.text = text
        self.tag = tag
        self.facilityid = facilityid
