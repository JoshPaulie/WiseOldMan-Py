# Pythonic Wise Old Man wrapper.

WiseOldMan-Py is a simple Python wrapper for [wiseoldman.net](https://wiseoldman.net/), an Old School RuneScape stat tracking site.

> 🛈 This project is in a working state, but lacks many endpoints. Contributors welcome

> 🛈 This project is not made by the WOM team. Hoping this will become the official Py wrapper. 🤞 

You can add me on discord [here](https://discordapp.com/users/177131156028784640) if you are interested in helping me package this up for others to use.

## Example Usage

```python
import wiseoldman
from wiseoldman_py.player import Player


wom = wiseoldman.WiseOldMan()
bexlii: Player = wom.get_player("bexlii")

print(bexlii.latest_snapshot.attack.exp) # 2601528
```
## Endpoints

### Player
- `/player` 👉 `WiseOldMan.get_player(username=, user_id=) -> Player`
- `/player/<id>/achievements` 👉 `Player.get_achievements() -> List[Achievement]`

### Groups
- `/groups` 👉 `WiseOldMan.get_group(group_id=) -> Group`
