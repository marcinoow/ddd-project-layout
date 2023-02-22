from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(String, primary_key=True)
    content = Column(String)
    post_id = Column(Integer, ForeignKey('posts.id'))

    def __repr__(self):
        return f'Comment(id={self.id}, content={self.content}, post_id={self.post_id})'
