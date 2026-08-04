# Local outputs

This directory is the default location for locally generated experiment
artifacts. Result files are not distributed with the repository.

Running the LUCID pipeline creates stage-specific subdirectories containing
manifests, embeddings, predictions, diagnostic records, metadata, and
`metrics.json` files. VLM observations are cached separately and can be reused
across shot settings and support seeds.

Generated files under `results/` are ignored by Git. This prevents prediction
files, VLM caches, embeddings, model checkpoints, and local benchmark summaries
from being committed accidentally.
