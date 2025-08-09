# kmer-sim

A lightweight Python toolkit for **k-mer–based similarity scoring** between DNA/RNA sequences.

K-mers (substrings of length 'k') are widely used in genomics for tasks like clustering, de-duplication, and sequence comparison.  
This project provides a small, well-tested library (and later a CLI) to:

- Build k-mer profiles from sequences
- Compute pairwise similarity using metrics such as **Jaccard**, **Containment**, and **Cosine**
- Work with common FASTA/FASTQ inputs and plain strings
- Keep the API simple, testable, and easy to extend

---

## Project Status

**Pre-alpha** – initial core functionality under active development.  
The goal is to first implement the core library + tests, then add CLI tools.

---

## Features (planned for v0.1)

- Generate canonical k-mers (optionally reverse-complement aware)
- Counted or set-based profiles
- Similarity metrics:
  - Jaccard index (set-based)
  - Containment (A in B)
  - Cosine similarity (count-based)
- Minimal FASTA reader
- CLI commands for direct comparisons (coming soon)
- Sketching/minhash support (future)

---

## Quick Example (planned API)

from kmer_sim import KmerProfile, jaccard_similarity

seq_a = "ACGTACGTAC"
seq_b = "ACGTTCGTAC"
k = 3

profile_a = KmerProfile.from_sequence(seq_a, k=k, canonical=True)
profile_b = KmerProfile.from_sequence(seq_b, k=k, canonical=True)

score = jaccard_similarity(profile_a.as_set(), profile_b.as_set())
print(f"Jaccard(k={k}) = {score:.3f}")

---

## FASTA example:

from kmer_sim.io import read_fasta
from kmer_sim import KmerProfile, cosine_similarity

for header, seq in read_fasta("example.fa"):
p = KmerProfile.from_sequence(seq, k=5, counted=True) # Compare, store, etc.

---

## Installation (dev)

# clone the repo

git clone https://github.com/robwalker-codes/kmer-sim.git
cd kmer-sim

# create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

# install dev dependencies

pip install --upgrade pip
pip install -r requirements-dev.txt

---

## Project Layout

```text
kmer-sim/
├── README.md
├── LICENSE
├── pyproject.toml
├── src/
│ └── kmer_sim/
│ ├── __init__.py
│ ├── core.py
│ ├── metrics.py
│ └── io.py
├── tests/
│ ├── test_core.py
│ ├── test_metrics.py
│ └── test_io.py
├── .gitignore
└── requirements-dev.txt
```

---

## Development Workflow

# run tests

pytest

# lint and format

ruff check .
black .

# type check

pyright # or mypy

---

## License

MIT – free to use, modify, and distribute.

---

## Acknowledgements

Inspired by common k-mer–based genomic approaches used in read-mapping, sketching, and sequence similarity tools.
