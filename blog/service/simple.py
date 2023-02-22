import time
import uuid
from blog.repository.crud.comment import CommentRepository
from blog.repository.crud.post import PostRepository
from blog.domain.post import Post
from blog.domain.comment import Comment


class SimpleService:
    """Creates simple service."""

    def __init__(self, session):
        self.session = session
        self.post_repository = PostRepository(session)
        self.comment_repository = CommentRepository(session)

    def run(self):
        """Performs fake operation (main app logic)."""
        print('Fake action in simple service...')

        print('Creating posts...')
        time.sleep(1)
        post_id = str(uuid.uuid4())
        post = Post(id=post_id,
                    title='Post 1',
                    content='Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
        self.post_repository.create(post)

        print('Creating comment...')
        time.sleep(1)
        comment_id = str(uuid.uuid4())
        comment_1 = Comment(id=comment_id,
                            content='Lorem Ipsum has been the industry\'s standard dummy text',
                            post=post)
        self.comment_repository.create(comment_1)

        print('Getting post from db...')
        time.sleep(1)
        print(self.post_repository.get_by_id(post_id))

        print('Getting comment from db...')
        time.sleep(1)
        print(self.comment_repository.get_by_id(comment_id))
