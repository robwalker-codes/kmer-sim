import pytest
from kmer_sim import KmerComparer, JaccardMetric

@pytest.fixture
def make_comparer():
    def _make(*, kmer_length=3, canonical=True):
        return KmerComparer(kmer_length=kmer_length, canonical=canonical, metric=JaccardMetric())
    return _make