from typing import Callable, Optional, TypedDict

from featureflags.flags import FlagConfig


class FeatureFlags:
    def __init__(self, *flags: dict[str, FlagConfig]) -> None:
        self._flags: dict[str, FlagConfig] = {}
        for d in flags:
            self._flags.update(d)

    def define(self, name: str, config: FlagConfig) -> None:
        self._flags[name] = config

    def enable(self, name: str) -> None:
        if name in self._flags:
            self._flags[name]["enabled"] = True

    def disable(self, name: str) -> None:
        if name in self._flags:
            self._flags[name]["enabled"] = False

    def is_enabled(self, name: str, context: Optional[dict] = None) -> bool:
        flag = self._flags.get(name)
        if not flag:
            return False

        if not flag.get("enabled", False):
            return False

        condition = flag.get("condition")
        if condition and not condition(context or {}):
            return False

        rollout = flag.get("rollout", 100)
        if rollout < 100 and context and "user_id" in context:
            uid = str(context["user_id"])
            return hash(uid) % 100 < rollout

        return True
