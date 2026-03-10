import pandas as pd

#This ensures annotation guidelines were followed.

df = pd.read_csv("./data/cleaned_reviews.csv")

valid_labels = ["positive", "negative", "neutral"]

invalid = df[~df['sentiment'].isin(valid_labels)]

print("Valid labels:", len(invalid))