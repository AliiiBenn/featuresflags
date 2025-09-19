from typing import ClassVar, Optional, Protocol

from featureflags.flags import FlagConfig
from featureflags.maybe import Maybe, Some, Nothing


class Storage(Protocol):
    def get_flag(self, name: str) -> Maybe[FlagConfig]: ...
    def set_flag(self, name: str, config: FlagConfig) -> None: ...
    def list_flags(self) -> dict[str, FlagConfig]: ...

    def enable_flag(self, name: str) -> Maybe[FlagConfig]: ...
    def disable_flag(self, name: str) -> Maybe[FlagConfig]: ...


class InMemoryStorage(Storage):
    _flags: ClassVar[dict[str, FlagConfig]] = {}

    def get_flag(self, name: str) -> Maybe[FlagConfig]:
        flag = self._flags.get(name)

        return Some(flag) if flag is not None else Nothing()

    def set_flag(self, name: str, config: FlagConfig) -> None:
        self._flags[name] = config

    def list_flags(self) -> dict[str, FlagConfig]:
        return self._flags

    def enable_flag(self, name: str) -> Maybe[FlagConfig]:
        if name not in self._flags:
            return Nothing()

        self._flags[name]["enabled"] = True
        return Some(self._flags[name])

    def disable_flag(self, name: str) -> Maybe[FlagConfig]:
        if name not in self._flags:
            return Nothing()

        self._flags[name]["enabled"] = False
        return Some(self._flags[name])
