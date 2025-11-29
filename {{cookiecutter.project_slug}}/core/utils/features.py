# core/utils/features.py
import os
from functools import lru_cache
import yaml
from decouple import config as config_env
from django.core.exceptions import ImproperlyConfigured


@lru_cache()
def get_enabled_apps() -> list[str]:
    """
        return enable module
    """
    config_path = config_env("FEATURES_CONFIG_PATH", "/app/config/features.yaml")
    
    if not os.path.exists(config_path):
        fallback_path = os.path.join(os.path.dirname(__file__), "../../config/features.yaml")
        if os.path.exists(fallback_path):
            config_path = fallback_path
        else:
            raise ImproperlyConfigured(f"Features config not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    enabled_modules = config.get("enabled_modules", [])
    
    apps = []
    for module in enabled_modules:
        if isinstance(module, str):
            apps.append(module)
        elif isinstance(module, dict) and "app" in module:
            apps.append(module["app"])
    
    return apps


def is_feature_enabled(feature_name: str) -> bool:
    """return enable feature

    Args:
        feature_name (str): feature name

    Returns:
        bool: if True enable else not enable
    """
    config_path = os.getenv("FEATURES_CONFIG_PATH", "/app/config/features.yaml")
    if not os.path.exists(config_path):
        return False
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    
    return feature_name in config.get("enabled_features", [])