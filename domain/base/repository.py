import abc
from typing import Generic
from typing import TypeVar

from domain.base.value_objects import Entity as DomainEntity

Entity = TypeVar('Entity', bound=DomainEntity)


class GenericRepository(Generic[Entity], metaclass=abc.ABCMeta):
    """An interface for a generic repository"""

    @classmethod
    @abc.abstractmethod
    def create(cls, entity: Entity):
        pass

    @classmethod
    @abc.abstractmethod
    def remove(cls, entity: Entity):
        pass

    @classmethod
    @abc.abstractmethod
    def get_by_id(cls, id: int) -> Entity:
        pass

    @classmethod
    def persist(cls, entity: Entity):
        raise NotImplementedError()

    @classmethod
    def persist_all(cls):
        raise NotImplementedError()
