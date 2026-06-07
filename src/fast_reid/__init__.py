"""Inference-focused FastReID package."""

from __future__ import annotations

from pathlib import Path

__version__ = "2.0.0"

PACKAGE_ROOT = Path(__file__).resolve().parent
CONFIG_ROOT = PACKAGE_ROOT / "configs"

__all__ = ["__version__", "PACKAGE_ROOT", "CONFIG_ROOT"]
