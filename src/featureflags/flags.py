from typing import TypedDict, Callable, Optional


class FlagConfig(TypedDict):
    enabled: bool
    rollout: int
    condition: Optional[Callable[[dict], bool]]
    # variant: Optional[str]
    # expires_at: Optional[str]  # ISO 8601 date
