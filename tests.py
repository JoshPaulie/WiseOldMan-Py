from wiseoldman_py import wiseoldman
from wiseoldman_py.player import Player

wom = wiseoldman.WiseOldMan()
bexlii = wom.get_player("bexlii")


def test_get_player():
    assert isinstance(bexlii, Player)


def test_player_skill():
    assert isinstance(bexlii.latest_snapshot.attack.experience, int)
