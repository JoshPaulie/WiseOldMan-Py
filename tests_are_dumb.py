"""Docstrings are dumber"""
from wiseoldman_py import wiseoldman
from pprint import pprint

wom = wiseoldman.WiseOldMan()
bexlii = wom.get_player("bexlii")

# Tests
def test_get_player():
    assert isinstance(bexlii.player_data, dict)


# Debugging
print(bexlii.skill.attack_ehp)
