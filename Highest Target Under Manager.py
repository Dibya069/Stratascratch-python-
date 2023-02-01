# Import your libraries
import pandas as pd

# Start writing code
e = salesforce_employees

f = e[e.manager_id == 13].nlargest(1, "target", keep = "all")
f[["first_name", "target"]]
