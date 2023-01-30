# Import your libraries
import pandas as pd

# Start writing code
s = employee

s1 = s.groupby("department").apply(lambda x: x[x["salary"] == x["salary"].max()])
s1[["department", "first_name", "salary"]]
