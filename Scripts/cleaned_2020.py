# ===== DATASET CLEANING IN ONE RUN =====

from google.colab import files
import pandas as pd

# 1) Upload dataset
uploaded = files.upload()

# 2) Automatically detect uploaded filename
filename = list(uploaded.keys())[0]

# 3) Read dataset
df = pd.read_csv(filename)

# 4) Replace empty blanks with NA
df = df.replace(r'^\s*$', 'NA', regex=True)
df = df.fillna('NA')

# 5) Fill Higher Education / Company column with UNEMPLOYED
target_col = None
for col in df.columns:
    if "company" in col.lower() or "higher" in col.lower():
        target_col = col
        break

if target_col:
    df[target_col] = df[target_col].replace('NA', 'UNEMPLOYED')

# 6) Save cleaned dataset
clean_name = "CLEANED_" + filename
df.to_csv(clean_name, index=False)

# 7) Download cleaned dataset
files.download(clean_name)

print("Cleaning completed ✅ Download started")
