import pytest
from featureflags import FeatureFlags
from featureflags.flags import FlagConfig


def test_ai_chat_feature_flag_is_enabled():
    flags = FeatureFlags({
        "AI_CHAT": FlagConfig(enabled=True)
    })
    assert flags.is_enabled("AI_CHAT") == True
