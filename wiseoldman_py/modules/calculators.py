from static import LEVEL_EXPERIENCE_MILESTONES


def get_level(xp):
    for indx, level_milestone in enumerate(LEVEL_EXPERIENCE_MILESTONES):
        if xp >= level_milestone and xp < LEVEL_EXPERIENCE_MILESTONES[indx + 1]:
            return indx + 1


print(get_level(82))
