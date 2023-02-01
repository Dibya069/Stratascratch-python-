# Import your libraries
import pandas as pd

# Start writing code
c = customers
o = orders

ss = pd.merge(c, o, left_on = "id", right_on = "cust_id", how = "left")

ss[["first_name", "last_name", "city", "order_details"]].sort_values(["first_name", "order_details"], na_position ='first')
