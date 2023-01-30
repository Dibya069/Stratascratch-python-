# Import your libraries
import pandas as pd

# Start writing code
sol = spotify_worldwide_daily_song_ranking

sol["cou"] = 1

sl = sol.groupby(['artist'])["cou"].count().reset_index()
sl.sort_values("cou", ascending = False)
