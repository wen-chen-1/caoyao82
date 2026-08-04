"""Command-line scaffold for a single few-shot baseline episode."""

import argparse
from pathlib import Path

from base import Episode
from registry import BASELINE_NAMES


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method", choices=BASELINE_NAMES, required=True)
    parser.add_argument("--support-manifest", type=Path, required=True)
    parser.add_argument("--universe-manifest", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    episode = Episode(
        support_manifest=args.support_manifest,
        universe_manifest=args.universe_manifest,
        data_root=args.data_root,
        output_dir=args.output_dir,
    )
    raise NotImplementedError(
        f"The executable {args.method} adapter is not included in this release. "
        f"Episode configuration: {episode}"
    )


if __name__ == "__main__":
    main()
