import numpy as np
import pytest

from engineering_experiment_design import estimate_effects, full_factorial


def test_two_factor_design_has_four_coded_runs():
    names, design = full_factorial(["temperature", "speed"])
    assert names == ["temperature", "speed"]
    assert design.shape == (4, 2)
    assert set(np.unique(design)) == {-1.0, 1.0}


def test_effect_estimation_recovers_coded_linear_model():
    _, design = full_factorial(["a", "b"])
    response = 10 + 2 * design[:, 0] - 3 * design[:, 1]
    assert estimate_effects(design, response) == pytest.approx([10, 2, -3])


def test_factor_names_must_be_unique():
    with pytest.raises(ValueError):
        full_factorial(["a", "a"])
