# root

*Community 0 | 6 files | cohesion 1.00*

## Definition

This community groups 6 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `calculate_and_draw_mandelbrot`, `draw_hypergeometric_shape`, `generate_valid_params`, `hypergeom`, `mandelbrot`, `map_value`. Core file: `hypercircle.py` (2 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `GLMandelbrot.py` | py | utility | 1 | no |
| `circle.py` | py | utility | 1 | no |
| `hypercircle.py` | py | utility | 2 | no |
| `hypermandala.py` | py | utility | 0 | no |
| `main.py` | py | utility | 1 | no |
| `mandelbrot.py` | py | utility | 2 | no |

## Key Symbols

- `calculate_and_draw_mandelbrot` (function, `GLMandelbrot.py:25`) `def calculate_and_draw_mandelbrot()`
- `generate_valid_params` (function, `circle.py:12`) `def generate_valid_params()`
- `generate_valid_params` (function, `hypercircle.py:12`) `def generate_valid_params()`
- `draw_hypergeometric_shape` (function, `hypercircle.py:20`) `def draw_hypergeometric_shape(a, b, z, angle, num_points)`
- `hypergeom` (function, `main.py:6`) `def hypergeom(a, b, c, z)`
- `map_value` (function, `mandelbrot.py:13`) `def map_value(value, from_low, from_high, to_low, to_high)`
- `mandelbrot` (function, `mandelbrot.py:17`) `def mandelbrot(c)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `GLMandelbrot.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `GLMandelbrot.py`
- `circle.py`
- `hypercircle.py`
- `hypermandala.py`
- `main.py`
- `mandelbrot.py`
