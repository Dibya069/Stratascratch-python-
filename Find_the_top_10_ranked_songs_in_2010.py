# Import your libraries
import pandas as pd

# Start writing code
sol = billboard_top_100_year_end.loc[billboard_top_100_year_end["year"] == 2010]
sol1 = sol[["year_rank", "group_name", "song_name"]].drop_duplicates(["year_rank"])
sol1.head(10)
