# Import your libraries
import pandas as pd

# Start writing code
sl = lyft_drivers

sl = sl.loc[(sl["yearly_salary"] <= 30000) | (sl["yearly_salary"] > 70000)]
sl
