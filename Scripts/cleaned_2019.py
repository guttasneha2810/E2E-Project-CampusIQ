# --------- IMPORT LIBRARIES ----------
import pandas as pd
from google.colab import files

# --------- LOAD DATASET ----------
# Change file name if yours is different
file_name = "Student wise Data  - ver -2(2019).csv"
df = pd.read_csv(file_name)

# --------- CLEANING PART ----------

# 1) Replace empty blanks with NA
df = df.replace(r'^\s*$', 'NA', regex=True)

# 2) Fill Higher Education missing values with UNEMPLOYED
# (column name must be same as your dataset)
for col in df.columns:
    if "Higher" in col or "higher" in col:
        df[col] = df[col].replace('NA', 'UNEMPLOYED')

# --------- SAVE CLEANED DATA ----------
clean_file = "Cleaned_Student_Data.csv"
df.to_csv(clean_file, index=False)

print("Dataset cleaned successfully!")

# --------- DOWNLOAD ----------
files.download(clean_file)