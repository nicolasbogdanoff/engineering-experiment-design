"""Small, transparent tools for engineering experiment design."""

from .factorial import add_two_factor_interactions, estimate_effects, full_factorial

__all__ = ["add_two_factor_interactions", "full_factorial", "estimate_effects"]
