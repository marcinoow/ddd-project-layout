import abc


class BaseRepository(metaclass=abc.ABCMeta):
    """Base repository class."""

    @abc.abstractmethod
    def create(self, model):
        raise NotImplemented()

    @abc.abstractmethod
    def get_by_id(self, id_):
        raise NotImplemented()
