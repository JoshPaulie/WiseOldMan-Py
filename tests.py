from wiseoldman_py import wiseoldman
from wiseoldman_py.player import Achievement, Player

wom = wiseoldman.WiseOldMan()


def test_get_player_by_username():
    """Test for player by username"""
    bexlii = wom.get_player(username="bexlii")
    assert isinstance(bexlii, Player)


def test_get_player_by_user_id():
    """Test for player by user id"""
    bexlii = wom.get_player(user_id=369451)
    assert isinstance(bexlii, Player)


def test_player_skill_level():
    """Test for player's skill, which is a custom property that should be checked."""
    bexlii = wom.get_player(username="bexlii")
    assert isinstance(bexlii.latest_snapshot.attack.level, int)


def test_player_get_achievements():
    """Test for getting a player's achievements"""
    bexlii_achievements = wom.get_player_achievements(username="bexlii")
    assert isinstance(bexlii_achievements, list)
