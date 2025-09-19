from typing import Generic, Optional, Protocol, TypeVar

T = TypeVar("T", covariant=True)


class Maybe(Protocol[T]):
    def is_some(self) -> bool: ...
    def is_none(self) -> bool: ...
    def unwrap(self) -> T: ...
    def map(self, fn): ...
    def bind(self, fn): ...


class Some(Maybe[T]):
    def __init__(self, value: T):
        self.value = value

    def is_some(self) -> bool:
        return True

    def is_none(self) -> bool:
        return False

    def unwrap(self) -> T:
        return self.value

    def map(self, fn):
        return Some(fn(self.value))

    def bind(self, fn):
        return fn(self.value)


class Nothing(Maybe[T]):
    def is_some(self) -> bool:
        return False

    def is_none(self) -> bool:
        return True

    def unwrap(self) -> T:
        raise ValueError("Tried to unwrap a Nothing")

    def map(self, fn):
        return self

    def bind(self, fn):
        return self
