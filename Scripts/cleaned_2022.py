
# COMPLETE DATA CLEANING (EXCEL FILE)
# =====================================

import pandas as pd
from google.colab import files

# 1) Read Excel dataset
file_name = "Student wise Data  - ver -2.xlsx"
df = pd.read_excel(file_name)

# 2) Replace all empty blanks with NA
df = df.replace(r'^\s*$', 'NA', regex=True)

# 3) Fill Higher Education missing values with UNEMPLOYED
for column in df.columns:
    if "higher" in column.lower():
        df[column] = df[column].replace('NA', 'UNEMPLOYED')

# 4) Save cleaned dataset
clean_file = "Cleaned_Student_Data.xlsx"
df.to_excel(clean_file, index=False)

print("DATA CLEANED SUCCESSFULLY ")

# 5) Download cleaned dataset
files.download(clean_file)


