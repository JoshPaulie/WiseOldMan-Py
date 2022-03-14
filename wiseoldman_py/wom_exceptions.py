class PlayerNotFoundError(ValueError):
    pass


# ? I wasn't sure what to inherit, docs lead me to believe this is fine
class PlayerHasNoAchievementsError(Exception):
    pass
