# Import your libraries
import pandas as pd

# Start writing code
s1 = airbnb_contacts.groupby('id_guest')['n_messages'].sum().reset_index()

s = s1.sort_values("n_messages", ascending = False)

s["rank"] = s["n_messages"].rank(method = "dense", ascending = False)

s[["rank", "id_guest", "n_messages"]]
