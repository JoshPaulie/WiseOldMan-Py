from .static import LEVEL_EXPERIENCE_MILESTONES


def get_level(xp: int) -> int:
    """Calculates a skill's level up to 99"""
    if xp >= 13034431:
        return 99

    for indx, level_milestone in enumerate(LEVEL_EXPERIENCE_MILESTONES):
        if xp >= level_milestone and xp < LEVEL_EXPERIENCE_MILESTONES[indx + 1]:
            return indx + 1

    return 1


def get_exp(level: int) -> int | float:
    """Calculates level from exp (s/o Darnell from the discord)"""
    return (1 / 8) * (
        (level ** 2) - level + 600 * (((2 ** (level / 7)) - (2 ** (1 / 7))) / ((2 ** (1 / 7)) - 1))
    )


def get_virtual_level(exp: int) -> int:
    """Calculates a skill's level up to and beyond 99 (again ty Darnell)"""
    lvl = 1
    while get_exp(lvl + 1) <= exp:
        lvl += 1
    return lvl
