from wiseoldman_py import wiseoldman

wom = wiseoldman.WiseOldMan()
bexlii = wom.get_player("bexlii")


def test_get_player():
    assert isinstance(bexlii.player_data, dict)


def test_player_skill():
    assert isinstance(bexlii.skill.attack_experience, int)
