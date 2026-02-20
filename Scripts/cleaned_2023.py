# ===============================
# FINAL DATA CLEANING (ONE RUN)
# ===============================

from google.colab import files
import pandas as pd

# 1) Upload your dataset
uploaded = files.upload()

# get filename automatically
filename = list(uploaded.keys())[0]

# 2) Read csv safely
df = pd.read_csv(filename, low_memory=False)

# 3) Remove unwanted Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]

# 4) Replace empty blanks with NA
df = df.replace(r'^\s*$', 'NA', regex=True)
df = df.fillna('NA')

# 5) Fill Higher Education / Company column missing with UNEMPLOYED
target_col = None
for col in df.columns:
    name = col.lower()
    if 'company' in name or 'higher' in name or 'study' in name:
        target_col = col
        break

if target_col:
    df[target_col] = df[target_col].replace('NA', 'UNEMPLOYED')

# 6) Save cleaned dataset
output_file = "CLEANED_POWERBI_DATASET.csv"
df.to_csv(output_file, index=False)

# 7) Download cleaned dataset
files.download(output_file)

print(" Dataset cleaned and downloaded successfully")

