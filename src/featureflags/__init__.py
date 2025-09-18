from collections.abc import Callable
from typing import Optional, TypedDict


class FeatureFlags:
    def __init__(self) -> None:
        pass

    def define(
        self,
        name: str,
        enabled: bool = False,
        condition: Optional[Callable] = None,
        rollout: int = 100,
    ) -> None:
        pass

    def enable(self, name: str) -> None:
        pass

    def disable(self, name: str) -> None:
        pass

    def is_enabled(self, name: str) -> None:
        pass
