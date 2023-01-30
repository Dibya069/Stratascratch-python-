# Import your libraries
import pandas as pd

# Start writing code
s1 = sf_employee
s2 = sf_bonus


s2 = s2.groupby("worker_ref_id")["bonus"].sum().reset_index() #this was the most important thing in this problem

s = pd.merge(s1, s2, left_on = "id", right_on = "worker_ref_id")
s["com"] = s[["salary", "bonus"]].sum(axis = 1)

ss = s[["employee_title", "sex", "com"]]
ss.groupby(["employee_title", "sex"])["com"].mean().reset_index()
