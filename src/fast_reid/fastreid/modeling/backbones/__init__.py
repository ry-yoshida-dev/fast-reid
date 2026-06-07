# encoding: utf-8
"""Backbones used by MOT17 inference configs (ResNet + ResNeSt)."""

from .build import BACKBONE_REGISTRY, build_backbone
from .resnet import build_resnet_backbone
from .resnest import build_resnest_backbone
