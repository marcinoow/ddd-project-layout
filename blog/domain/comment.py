from dataclasses import dataclass

from .post import Post


@dataclass
class Comment:
    id: str
    content: str
    post: Post
