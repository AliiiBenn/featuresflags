from collections.abc import Callable
from typing import Optional, TypedDict

from featureflags.flags import FlagConfig
from featureflags.storage import Storage


class FeatureFlags:
    def __init__(self, storage: Storage, initial_flags: dict[str, FlagConfig]) -> None:
        self.storage = storage
        self._init_flags(initial_flags)

    def _init_flags(self, flags: dict[str, FlagConfig]) -> None:
        for name, config in flags.items():
            self.define(name, config)

    def define(
        self,
        name: str,
        config: FlagConfig,
    ) -> None:
        self.storage.set_flag(name, config)

    def enable(self, name: str) -> None:
        self.storage.enable_flag(name)

    def disable(self, name: str) -> None:
        self.storage.disable_flag(name)

    def is_enabled(self, name: str) -> bool:
        flag = self.storage.get_flag(name)

        return False if flag.is_none() else flag.unwrap()['enabled']
