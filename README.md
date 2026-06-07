# fast-reid

## Overview

Inference-only fork of [JDAI-CV/fast-reid](https://github.com/JDAI-CV/fast-reid). Import as `fast_reid.fastreid` (configs ship under `fast_reid.configs`). Training stacks, datasets, evaluation, and unused backbones were removed; MOT17 YAML configs are bundled for ReID-Inference.

PyTorch is not pinned; install it separately for your CUDA/CPU setup.

```bash
pip install .
```

## Components

| Component | Description |
| --------- | ----------- |
| [src/fast_reid/fastreid/](src/fast_reid/fastreid/) | Config, modeling (Baseline/MGN), layers, checkpoint utilities. |
| [src/fast_reid/configs/MOT17/](src/fast_reid/configs/MOT17/) | MOT17 model YAML stems (`sbs_S50`, `bagtricks_R50`, …). |

## Examples

```python
import torch
from fast_reid import CONFIG_ROOT
from fast_reid.fastreid.config import get_cfg
from fast_reid.fastreid.modeling.meta_arch import build_model
from fast_reid.fastreid.utils.checkpoint import Checkpointer

cfg = get_cfg()
cfg.merge_from_file(str(CONFIG_ROOT / "MOT17" / "sbs_S50.yml"))
cfg.merge_from_list(["MODEL.WEIGHTS", "path/to/model.pth", "MODEL.BACKBONE.PRETRAIN", False])
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
cfg.freeze()

model = build_model(cfg)
Checkpointer(model).load("path/to/model.pth")
```
