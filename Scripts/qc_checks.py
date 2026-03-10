import pandas as pd

#Checks the distributions of sentiment labels

df = pd.read_csv("./data/cleaned_reviews.csv")

print("Total records:", len(df))

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Label distribution
print("\nLabel Distribution:")
print(df['sentiment'].value_counts())