from __future__ import annotations
from typing import Set

class JaccardMetric:
    """Calculates the Jaccard index between two sets of k-mers."""

    @staticmethod
    def score(kmers_a: Set[str], kmers_b: Set[str]) -> float:
        """Return the Jaccard similarity between two sets."""
        if not kmers_a and not kmers_b:
            return 1.0  # identical empty sets = max similarity

        intersection_size = len(kmers_a & kmers_b)
        union_size = len(kmers_a | kmers_b)

        return intersection_size / union_size if union_size > 0 else 0.0
