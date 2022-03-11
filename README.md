# Pythonic Wise Old Man wrapper.

WiseOldMan-Py is a simple Python wrapper for wiseoldman.net, an Old School RuneScape stat tracking site.

> 🛈 This project is in a working state, but lacks many features.

You can add me on discord [here](https://discordapp.com/users/177131156028784640) if you are interested in helping me package this up for others to use.

## Example Usage

```python
import wiseoldman

wom = wiseoldman.WiseOldMan()
bexlii = wom.get_player("bexlii")

print(bexlii.latest_stats.attack.exp) # 2601528
```
## Endpoints
- `/player` 👉 `WiseOldMan.get_player(username, user_id)`
- `/player/id/achievements` 👉 `WiseOldMan.get_player(username, user_id)`
