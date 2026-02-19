# =====================================
# ONE CLICK DATASET CLEANING PROGRAM
# =====================================

from google.colab import files
import pandas as pd

# Upload dataset
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# Read dataset safely
df = pd.read_csv(filename, low_memory=False)

# Remove unwanted Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]

# Replace empty blanks with NA
df = df.replace(r'^\s*$', 'NA', regex=True)
df = df.fillna('NA')

# Find placement / higher studies column automatically
target_col = None
for col in df.columns:
    name = col.lower()
    if 'company' in name or 'higher' in name or 'study' in name:
        target_col = col
        break

# Fill missing with UNEMPLOYED
if target_col is not None:
    df[target_col] = df[target_col].replace('NA', 'UNEMPLOYED')

# Save cleaned dataset
output_file = "FINAL_POWERBI_READY_DATASET.csv"
df.to_csv(output_file, index=False)

# Download automatically
files.download(output_file)

print("\n✅ CLEANING COMPLETED — FILE DOWNLOADED")
