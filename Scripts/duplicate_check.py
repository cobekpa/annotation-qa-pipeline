import pandas as pd

#This checks if annotators labeled the same review multiple times.

df = pd.read_csv("./data/cleaned_reviews.csv")

duplicates = df[df.duplicated(subset=['cleaned_review'])]

print("Duplicate reviews:", len(duplicates))