# Import your libraries
import pandas as pd

# Start writing code
sl1 = airbnb_hosts
sl2 = airbnb_guests

sl = pd.merge(sl1, sl2, on = ("gender", "nationality"))
sl[["host_id", "guest_id"]].drop_duplicates()
