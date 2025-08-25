from __future__ import annotations
from collections.abc import Callable
import pytest
from kmer_sim import KmerComparer, JaccardMetric

DEFAULT_K = 3  # avoids magic number in tests

@pytest.fixture
def comparer_factory() -> Callable[..., KmerComparer]:
    def create(*, kmer_length: int = DEFAULT_K, canonical: bool = True, metric=None) -> KmerComparer:
        metric = JaccardMetric() if metric is None else metric
        return KmerComparer(kmer_length=kmer_length, canonical=canonical, metric=metric)
    return create

@pytest.fixture
def comparer(comparer_factory: Callable[..., KmerComparer]) -> KmerComparer:
    return comparer_factory()