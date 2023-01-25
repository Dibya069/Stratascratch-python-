# Import your libraries
import pandas as pd

# Start writing code
sal = ms_employee_salary.sort_values(["salary"], ascending = False)


sal1 = sal.drop_duplicates(["id"])

result = sal1.sort_values(["id"])
result
