# Import your libraries
import pandas as pd

# Start writing code
sol = dc_bikeshare_q1_2012.sort_values(["end_time"], ascending = False)

sl1 = sol.drop_duplicates(["bike_number"])
sl1[["bike_number", "end_time"]]
