# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `mandelbrot` | 2 | 4 | `GLMandelbrot.py`, `mandelbrot.py` |
| `draw` | 2 | 2 | `GLMandelbrot.py`, `hypercircle.py` |
| `generate` | 2 | 2 | `circle.py`, `hypercircle.py` |
| `params` | 2 | 2 | `circle.py`, `hypercircle.py` |
| `valid` | 2 | 2 | `circle.py`, `hypercircle.py` |

## Dialectic Prompts

- Thesis: `generate` centralizes 2 files; Antithesis: `params` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `generate` centralizes 2 files; Antithesis: `valid` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `params` centralizes 2 files; Antithesis: `valid` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
