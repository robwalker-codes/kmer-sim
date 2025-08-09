import pytest

def test_identical_sequences_have_similarity_one(make_comparer):
    comparer = make_comparer()
    sequence = "ACGTACGT"
    
    assert comparer.compare(sequence, sequence) == 1.0

def test_disjoint_sequences_have_zero(make_comparer):
    comparer = make_comparer()
    
    assert comparer.compare("AAAAAA", "CCCCCC") == 0.0