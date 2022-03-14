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
bexlii: Player = wom.get_player("bexlii") # Creates Player object, with player's most recent snapshot. Searchable by user id as well
bexlii_achivements = bexlii.get_achievements() # Returns list of any achievements awarded
bexlii_competitions = bexlii.get_competitions() # Returns list of any competitions particiapted in

print(bexlii_achivements)
print(bexlii_competitions)
print(bexlii.latest_snapshot.attack.exp)

```
👆 Would output 👇 (Formatted nicley for your viewing pleasure)
```python
[
    Achievement(threshold=13034431, player_id=369451, name='99 Cooking', metric='cooking', created_at=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), 
measure='experience'),
    Achievement(threshold=13034431, player_id=369451, name='99 Strength', metric='strength', created_at=datetime.datetime(2021, 12, 6, 22, 41, 6, 396000, tzinfo=datetime.timezone.utc),measure='experience')
]
[
    Competition(competition_id=8147, title='Skill of the Week', metric='mining', score=0, starts_at=datetime.datetime(2021, 12, 27, 5, 0, tzinfo=datetime.timezone.utc),
ends_at=datetime.datetime(2022, 1, 3, 5, 0, tzinfo=datetime.timezone.utc), competition_type='classic', group_id=None, created_at=datetime.datetime(2021, 12, 26, 14, 6, 3, 760000,      
tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2022, 1, 3, 6, 0, 1, 736000, tzinfo=datetime.timezone.utc), duration='1 week', participant_count=16),
    Competition(competition_id=5766, title='Who is the biggest No Life?', metric='overall', score=0, starts_at=datetime.datetime(2021, 9, 17, 5, 0, tzinfo=datetime.timezone.utc),      
ends_at=datetime.datetime(2021, 9, 24, 5, 0, tzinfo=datetime.timezone.utc), competition_type='classic', group_id=None, created_at=datetime.datetime(2021, 9, 14, 1, 44, 6, 323000,      
tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2021, 9, 24, 6, 0, 0, 589000, tzinfo=datetime.timezone.utc), duration='1 week', participant_count=71)
]
2601528
```
## Endpoints

### Player
- `/players` 👉 `WiseOldMan.get_player(username=, user_id=) -> Player`
- `/players/<id>/achievements` 👉 `Player.get_achievements() -> List[Achievement]`

### Groups
- `/groups/<id>` 👉 `WiseOldMan.get_group(group_id=) -> Group`
