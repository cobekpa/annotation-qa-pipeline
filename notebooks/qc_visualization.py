import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("./data/cleaned_reviews.csv")

sentiment_counts = df['sentiment'].value_counts()
sentiment_percent = df['sentiment'].value_counts(normalize=True) * 100

plt.figure(figsize=(6,4))
ax = sns.countplot(x='sentiment', data=df)

for i, count in enumerate(sentiment_counts):
    percentage = sentiment_percent.iloc[i]
    ax.text(i, count + 1, f'{percentage:.1f}%', ha='center')

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.show()