# Import your libraries
import pandas as pd

# Start writing code
sl = amazon_transactions

s1 = sl.sort_values(by=['user_id','created_at'])

s1["diff"] = s1.groupby("user_id")["created_at"].diff()

s1[s1["diff"] <= pd.Timedelta(days = 7)]["user_id"].unique()
