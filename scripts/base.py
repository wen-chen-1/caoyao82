"""Public interface scaffold for few-shot baseline adapters.

Algorithm implementations are intentionally not included in this release.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Episode:
    """Paths shared by every baseline episode."""

    support_manifest: Path
    universe_manifest: Path
    data_root: Path
    output_dir: Path


class Baseline(ABC):
    """Minimal contract implemented by every baseline adapter."""

    name: str

    @abstractmethod
    def run(self, episode: Episode) -> None:
        """Run one episode and write predictions and metrics."""
        raise NotImplementedError
