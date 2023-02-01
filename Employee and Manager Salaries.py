# Import your libraries
import pandas as pd

# Start writing code
e = employee

s = pd.merge(e, e, left_on = "manager_id", right_on = "id")
s[["first_name_x", "salary_x"]].loc[s["salary_x"] > s["salary_y"]]
