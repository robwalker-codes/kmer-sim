import math
from kmer_sim import KmerComparer, JaccardMetric

def test_identical_sequences_have_similarity_one():
    comparer = KmerComparer(kmer_length=3, canonical=True, metric=JaccardMetric())
    sequenceA = "ACGTACGT"
    sequenceB = "ACGTACGT"
    
    score = comparer.compare(sequenceA, sequenceB)
    
    assert math.isclose(score, 1.0, rel_tol=0, abs_tol=1e-12)