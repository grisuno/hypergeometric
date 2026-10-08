# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `mandelbrot` | files=2 | mentions=4 | `GLMandelbrot.py`, `mandelbrot.py`
- `draw` | files=2 | mentions=2 | `GLMandelbrot.py`, `hypercircle.py`
- `generate` | files=2 | mentions=2 | `circle.py`, `hypercircle.py`
- `params` | files=2 | mentions=2 | `circle.py`, `hypercircle.py`
- `valid` | files=2 | mentions=2 | `circle.py`, `hypercircle.py`

## Dialectic

- Thesis: `generate` centralizes 2 files; Antithesis: `params` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `generate` centralizes 2 files; Antithesis: `valid` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `params` centralizes 2 files; Antithesis: `valid` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
