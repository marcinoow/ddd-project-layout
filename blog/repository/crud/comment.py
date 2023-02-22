from blog.repository.crud.base import BaseRepository
from blog.repository.models.comment import Comment as CommentModel
from blog.domain.comment import Comment as CommentEntity
from blog.domain.post import Post as PostEntity


class CommentRepository(BaseRepository):
    """Creates object to manage comment in data in database."""
    def __init__(self, session):
        self.session = session

    def create(self, comment):
        """Creates comment."""
        comment_model = CommentModel(id=comment.id, content=comment.content, post_id=comment.post.id)
        self.session.add(comment_model)
        self.session.commit()

    def get_by_id(self, id_):
        """Gets comment by id."""
        comment_model = self.session.query(CommentModel).get(id_)
        if comment_model is not None:
            return CommentEntity(id=comment_model.id,
                                 content=comment_model.content,
                                 post=PostEntity(id=comment_model.post.id,
                                                 title=comment_model.post.title,
                                                 content=comment_model.post.content)
                                 )
