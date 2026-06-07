# encoding: utf-8
"""Meta-architectures for inference (Baseline, MGN)."""

from .baseline import Baseline
from .build import META_ARCH_REGISTRY, build_model
from .mgn import MGN
