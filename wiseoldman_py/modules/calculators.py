from .static import LEVEL_EXPERIENCE_MILESTONES


def get_level(xp: int) -> int:
    """Calculates a skill's level up to 99"""
    if xp >= 13034431:
        return 99

    for indx, level_milestone in enumerate(LEVEL_EXPERIENCE_MILESTONES):
        if xp >= level_milestone and xp < LEVEL_EXPERIENCE_MILESTONES[indx + 1]:
            return indx + 1

    return 0
