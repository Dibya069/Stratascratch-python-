# Import your libraries
import pandas as pd
import re

# Start writing code
sl = google_file_store

sl["bear"] = sl["contents"].apply(lambda text: len(re.findall(r"\bbear\b", text)))
sl["bull"] = sl["contents"].apply(lambda text: len(re.findall(r"\bbull\b", text)))

sl[["bear", "bull"]].sum().reset_index()
