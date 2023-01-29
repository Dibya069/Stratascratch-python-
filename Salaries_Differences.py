# Import your libraries
import pandas as pd

# Start writing code
s1 = db_employee
s2 = db_dept

s = pd.merge(s1, s2, left_on = "department_id", right_on = "id")
ss1 = s.loc[s["department"] == "marketing", "salary"].max()
ss2 = s.loc[s["department"] == "engineering", "salary"].max()
ss1 - ss2
