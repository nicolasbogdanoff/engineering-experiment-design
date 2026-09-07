import numpy as np
import pytest

from engineering_experiment_design import add_two_factor_interactions, decode_coded_design, estimate_effects, full_factorial


def test_two_factor_design_has_four_coded_runs():
    names, design = full_factorial(["temperature", "speed"])
    assert names == ["temperature", "speed"]
    assert design.shape == (4, 2)
    assert set(np.unique(design)) == {-1.0, 1.0}


def test_effect_estimation_recovers_coded_linear_model():
    _, design = full_factorial(["a", "b"])
    response = 10 + 2 * design[:, 0] - 3 * design[:, 1]
    assert estimate_effects(design, response) == pytest.approx([10, 2, -3])


def test_two_factor_interactions_are_appended_as_coded_columns():
    _, design = full_factorial(["a", "b", "c"])
    expanded = add_two_factor_interactions(design)
    assert expanded.shape == (8, 6)
    assert expanded[0, 3:].tolist() == [1.0, 1.0, 1.0]


def test_factor_names_must_be_unique():
    with pytest.raises(ValueError):
        full_factorial(["a", "a"])


def test_coded_design_decodes_to_physical_levels():
    _, design = full_factorial(["temperature", "speed"])
    decoded = decode_coded_design(design, [20, 1000], [80, 3000])
    assert decoded[0].tolist() == [20, 1000]
    assert decoded[-1].tolist() == [80, 3000]


def test_decoding_rejects_non_coded_values():
    with pytest.raises(ValueError, match=r"only -1 and \+1"):
        decode_coded_design(np.array([[0.0, 1.0]]), [0, 0], [1, 1])
