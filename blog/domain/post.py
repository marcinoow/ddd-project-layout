from dataclasses import dataclass

# from .comment import Comment


@dataclass
class Post:
    id: str
    title: str
    content: str
    # Should I implement it? If yes how to implement it here and in crud?
    # comments: list[Comment]
    #
    # def __post_init__(self):
    #     if self.comments is None:
    #         self.comments = []
