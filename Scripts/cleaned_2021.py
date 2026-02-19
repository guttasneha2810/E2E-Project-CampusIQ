# ==============================
# COMPLETE DATA CLEANING PROGRAM
# ==============================

from google.colab import files
import pandas as pd

# 1) Upload file
uploaded = files.upload()

# get uploaded file name automatically
filename = list(uploaded.keys())[0]

# 2) Read dataset (fix mixed type warning)
df = pd.read_csv(filename, low_memory=False)

# 3) Remove Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]

# 4) Replace empty blanks with NA
df = df.replace(r'^\s*$', 'NA', regex=True)
df = df.fillna('NA')

# 5) Fill Higher Education / Company column with UNEMPLOYED
target_col = None
for col in df.columns:
    if ('company' in col.lower()) or ('higher' in col.lower()) or ('study' in col.lower()):
        target_col = col
        break

if target_col is not None:
    df[target_col] = df[target_col].replace('NA', 'UNEMPLOYED')

# 6) Save cleaned dataset
output_file = "FINAL_POWERBI_DATASET.csv"
df.to_csv(output_file, index=False)

# 7) Force download
files.download(output_file)

print("\n✅ Cleaning Finished Successfully")
print("Downloaded File Name:", output_file)
