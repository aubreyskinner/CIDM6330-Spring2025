from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> T:
        pass

    @abstractmethod
    def create(self, item: T) -> T:
        pass

    @abstractmethod
    def update(self, item_id: int, item: T) -> T:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> None:
        pass
