# Public split manifests

The released Neem manifests contain the fixed evaluation universe, the
independent validation split, and the support set for each few-shot run.

The query set is not stored repeatedly. It is generated locally for every run
as:

```text
query = evaluation universe - current support set
```

Paths are relative to the dataset root supplied through `--data-root`, and
image content is identified by SHA-256. `scripts/run_lucid_pipeline.py`
performs this operation automatically. `scripts/build_query_manifest.py`
provides the same operation for standalone baseline scripts.
