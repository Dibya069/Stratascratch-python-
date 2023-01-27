# Import your libraries
import pandas as pd

# Start writing code
sl1 = customers
sl2 = orders

sl1 = sl1.loc[(sl1["first_name"] == "Jill") | (sl1["first_name"] == "Eva")]

sl = pd.merge(sl1, sl2, left_on = "id", right_on = "cust_id", how = "left")
sl[["order_date", "order_details", "total_order_cost", "first_name"]]
