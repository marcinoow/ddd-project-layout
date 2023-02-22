from blog.repository.crud.base import BaseRepository
from blog.repository.models.post import Post as PostModel
from blog.domain.post import Post as PostEntity


class PostRepository(BaseRepository):
    """Creates object to manage post in data in database."""
    def __init__(self, session):
        self.session = session

    def create(self, post):
        """Creates post."""
        post_model = PostModel(id=post.id, title=post.title, content=post.content)
        self.session.add(post_model)
        self.session.commit()

    def get_by_id(self, id_):
        """Gets post by id."""
        post_model = self.session.query(PostModel).get(id_)
        if post_model is not None:
            return PostEntity(id=post_model.id, title=post_model.title, content=post_model.content)
