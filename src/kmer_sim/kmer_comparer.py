from __future__ import annotations
from typing import Iterable, Set

class KmerComparer:
    def __init__(self, *, kmer_length: int, canonical: bool, metric) -> None:
        if kmer_length <= 0:
            raise ValueError("kmer_length must be > 0")
        self.kmer_length = kmer_length
        self.canonical = canonical
        self.metric = metric

    def compare(self, sequence_a: str, sequence_b: str) -> float:
        kmers_a = self._extract_kmers(sequence_a)
        kmers_b = self._extract_kmers(sequence_b)
        return self.metric.score(kmers_a, kmers_b)

    def _extract_kmers(self, sequence: str) -> Set[str]:
        sequence = sequence.upper()
        if len(sequence) < self.kmer_length:
            return set()

        kmers = (sequence[i:i + self.kmer_length] 
                 for i in range(len(sequence) - self.kmer_length + 1))

        if self.canonical:
            kmers = (self._canonical_form(kmer) for kmer in kmers)

        return set(kmers)

    def _canonical_form(self, kmer: str) -> str:
        reverse_complement = self._reverse_complement(kmer)
        return min(kmer, reverse_complement)

    @staticmethod
    def _reverse_complement(sequence: str) -> str:
        complement_map = str.maketrans("ACGT", "TGCA")
        return sequence.translate(complement_map)[::-1]
