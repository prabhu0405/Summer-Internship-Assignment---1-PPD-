
import pandas as pd

df = pd.read_csv("digital_burnout_productivity_dataset.csv")

# Display first 5 rows
print("First 5 Rows:\n")
print(df.head())


# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

#filling numeric missing values with column mean
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

#filling categorical missing values with mode
categorical_columns = df.select_dtypes(include=['object']).columns

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

#removing duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)

print(f"\nDuplicates Removed: {before - after}")

#statistics
print("\nDataset Statistics:\n")
print(df.describe())

#converting categorical columns into numbers
df_encoded = pd.get_dummies(df, drop_first=True)

print("\nEncoded Dataset Preview:\n")
print(df_encoded.head())

#cleaned dataset
df_encoded.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")