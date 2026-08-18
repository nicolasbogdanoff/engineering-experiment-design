# Engineering Experiment Design

Transparent Python utilities for planning two-level full-factorial engineering experiments and estimating coded intercept/main effects.

## Scope

The package generates a complete \(2^k\) design with coded levels `-1` and `+1`. Given observed responses, it estimates the intercept and main effects with least squares:

\[
 y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + \epsilon
\]

This first version deliberately excludes automatic claims about significance, causality, or optimality. Replication, randomization, blocking, interaction terms, residual analysis, and engineering constraints must be considered in the study plan.

## Quick start

```bash
python -m venv .venv
python -m pip install -e '.[test]'
pytest -q
python examples/two_factor_study.py
```

## Repository structure

- `engineering_experiment_design/factorial.py`: design generation and effect estimation.
- `examples/`: a four-run two-factor study with a small deterministic noise vector.
- `tests/`: equation-level regression tests.

## Academic direction

Planned extensions include interaction columns, replicated-run summaries, residual diagnostics, and a design report that records factor units, physical levels, randomization, and measurement uncertainty.

## Author

Nicolás Mauricio Bogdanoff · Universidad Paraguayo Alemana (UPA) · [ORCID](https://orcid.org/0009-0004-6275-3013)

## License and citation

MIT License. See `CITATION.cff` for citation metadata.
