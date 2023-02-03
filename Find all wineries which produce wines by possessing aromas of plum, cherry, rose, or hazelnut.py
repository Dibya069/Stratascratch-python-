# Import your libraries
import pandas as pd
import re
# Start writing code
s = winemag_p1

s = s.loc[s["description"].str.contains(r"\b(plum|cherry|rose|hazelnut)\b", flags = re.I, regex = True)]
s["winery"].drop_duplicates()
