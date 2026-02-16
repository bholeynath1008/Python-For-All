import pandas as pd
import numpy as np

students_python = [
    {"Name": "Alice", "Age": 20, "Grade": 85},
    {"Name": "Bob", "Age": 22, "Grade": 90},
    {"Name": "Charlie", "Age": 21, "Grade": 78},
]

# create df from dictionary

students = pd.DataFrame(students_python)
# print(students)

grades_panda = students[students["Grade"] > 80]
# print(grades_panda)

# Create Series with custom index labels

s = pd.Series([10, 20, 30], index=["a","b","c"])
print(s)
