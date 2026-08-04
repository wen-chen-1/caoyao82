# LUCID: A Training-Free Few-Shot Framework for Leaf Disease Diagnosis via Visual–Knowledge Evidence Fusion

This repository provides the project overview, evaluation protocol, and baseline interface scaffolding for LUCID. Experiments include the main evaluation on Neem and cross-dataset evaluations on Tulsi and Jujube. 
## Overview

LUCID is a training-free few-shot framework that combines visual prototypes with structured symptom knowledge. It first constructs class prototypes using a frozen visual encoder and obtains five-dimensional, diagnosis-free observations from a vision-language model. The observations are then matched against expert knowledge, followed by visual-dominant confidence-gated fusion. For ambiguous predictions, LUCID performs an additional class-name-free observation using visible differences between the Top-2 candidates.

## Datasets

| Dataset | Role | Source |
|---|---|---|
| Neem | Main experiment | [AI-MedLeafX v1](https://data.mendeley.com/datasets/zz7r5y4dc6/1) |
| Tulsi | Generalization experiment | [Medicinal Plant Leaf Disease Dataset v1](https://data.mendeley.com/datasets/ncg7kk3gwx/1) |
| Jujube | Generalization experiment | [Jujube Leaf Disease and Health Image Dataset v4](https://data.mendeley.com/datasets/yxmf3cd865/4) |

Experiments are conducted under 1-, 3-, 5-, and 10-shot settings. 

Dataset download links, directory structures, and additional protocol details are provided in [data/README.md](data/README.md).

## Main results

Accuracy is reported as the mean ± sample standard deviation over five runs.

| Dataset | 1-shot | 3-shot | 5-shot | 10-shot |
|---|---:|---:|---:|---:|
| Neem | **68.55 ± 3.88** | **75.65 ± 0.83** | **80.54 ± 1.79** | **83.65 ± 0.83** |
| Tulsi | **79.27 ± 6.12** | **88.94 ± 3.40** | **93.50 ± 1.15** | **94.88 ± 0.93** |
| Jujube | **57.26 ± 5.15** | **71.91 ± 2.11** | **74.27 ± 1.63** | **78.74 ± 0.95** |

## Installation

Python 3.10 or later is recommended. The current interface scaffold uses only the Python standard library:

```bash
python scripts/run_baseline.py --help
```


## Data preparation

Download the datasets from their original sources and arrange them under `data/` according to [data/README.md](data/README.md). Paths stored in the manifests are relative to the corresponding dataset root.

## Baselines

The repository contains interface scaffolding for the following few-shot baselines:

- SigLIP visual prototype
- ViT-B/16
- ResNet-50
- CLIP visual prototype
- CoOp
- Tip-Adapter
- MVPDR

All methods use the same support and evaluation-universe protocol. The files under `scripts/` define the expected inputs and outputs.

```bash
python scripts/run_baseline.py --help
```



## Reproducibility

No query labels are used for support selection or external-dataset parameter tuning. Evaluation metrics include accuracy, macro-precision, macro-recall, and macro-F1, reported over five runs.


