# Import your libraries
import pandas as pd

# Start writing code
orders["yr"] = orders["order_date"].dt.year 
orders["mn"] = orders["order_date"].dt.month 

orders = orders[(orders["yr"] == 2019) & (orders["mn"] == 3)]

sl = orders.groupby(["cust_id"]).sum().reset_index()
sl[["cust_id", "total_order_cost"]].sort_values("total_order_cost", ascending = False)
