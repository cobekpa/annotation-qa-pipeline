import pandas as pd

df = pd.read_csv("./data/cleaned_reviews.csv")

report = {
    "total_records": len(df),
    "missing_sentiment": df['sentiment'].isnull().sum(),
    "duplicate_reviews": df.duplicated(subset=['cleaned_review']).sum()
}

report_df = pd.DataFrame([report])

report_df.to_csv("./reports/qc_summary.csv", index=False)

print("QC report generated!")