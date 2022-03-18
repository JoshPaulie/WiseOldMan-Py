from itertools import count

from .static import LEVEL_EXPERIENCE_MILESTONES


def get_exp_miltstone(level: int) -> int | float:
    """Calculates level milestone from exp (s/o Darnell from the discord)"""
    return (1 / 8) * (
        (level ** 2) - level + 600 * (((2 ** (level / 7)) - (2 ** (1 / 7))) / ((2 ** (1 / 7)) - 1))
    )


def get_level(exp: int, virtual_level=False) -> int:
    """
    Calculates a skill's level. By default, it returns a max of 99.
    If you'd like to return a virtual level, set the argument to true
    """
    lvl = 1
    while get_exp_miltstone(lvl + 1) <= exp:
        lvl += 1

    if not virtual_level and lvl > 99:
        return 99
    else:
        return lvl
