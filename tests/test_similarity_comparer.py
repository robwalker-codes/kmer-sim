import pytest

_RC_TABLE = str.maketrans("ACGT", "TGCA")
def reverse_complement(seq: str) -> str:
    return seq.translate(_RC_TABLE)[::-1]

def test_identical_sequences_have_similarity_one(comparer):
    s = "ACGTACGT"
    assert comparer.compare(s, s) == pytest.approx(1.0, abs=1e-12)

def test_disjoint_sequences_have_zero(comparer):
    assert comparer.compare("AAAAAA", "CCCCCC") == 0.0

@pytest.mark.parametrize(
    "a,b,k,canonical,expected",
    [
        ("ACGTAC", "ACGTTC", 3, False, pytest.approx(1/3, abs=1e-12)),
        ("", "", 3, True, pytest.approx(1.0, abs=1e-12)),
    ],
)
def test_basic_cases(comparer_factory, a, b, k, canonical, expected):
    cmp = comparer_factory(kmer_length=k, canonical=canonical)
    assert cmp.compare(a, b) == expected

def test_both_shorter_than_k_yield_one_as_both_empty_sets(comparer_factory):
    cmp = comparer_factory(kmer_length=5, canonical=True)
    assert cmp.compare("AC", "A") == pytest.approx(1.0, abs=1e-12)

def test_reverse_complements_equal_under_canonicalisation(comparer_factory):
    s = "AAACCC"
    rc = reverse_complement(s)

    cmp_canonical = comparer_factory(kmer_length=3, canonical=True)
    cmp_raw = comparer_factory(kmer_length=3, canonical=False)

    canonical_result = cmp_canonical.compare(s, rc)
    raw_result = cmp_raw.compare(s, rc)

    assert canonical_result == pytest.approx(1.0, abs=1e-12)
    assert raw_result == 0.0 

def test_symmetry(comparer_factory):
    cmp = comparer_factory(kmer_length=3, canonical=True)
    a, b = "ACGTAC", "ACGTTC"
    assert cmp.compare(a, b) == cmp.compare(b, a)
