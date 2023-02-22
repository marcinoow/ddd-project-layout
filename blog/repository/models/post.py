from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    executions = relationship('Comment', backref='post')

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content})'
