# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
df = df.groupby("games").name.nunique().reset_index().sort_values("name", ascending = False).head(1)
