import pandas as pd
import numpy as np


file_name = "cleaned_dataset.csv"

df = pd.read_csv(file_name)


report_file = "insights_report.txt"

report = open(report_file, "w", encoding="utf-8")

#overview

report.write("-------------------------------------------------------\n")
report.write("DIGITAL BURNOUT & PRODUCTIVITY ANALYTICS REPORT\n")
report.write("-------------------------------------------------------\n\n")

report.write("1. DATASET OVERVIEW\n")
report.write("----------------------------------------------------\n")

report.write(f"Rows: {df.shape[0]}\n")
report.write(f"Columns: {df.shape[1]}\n\n")

report.write("Columns Present:\n")

for col in df.columns:
    report.write(f"- {col}\n")

report.write("\n")

#missing value(doesn't exist because we have handled in previous task)

report.write("2. DATA QUALITY CHECK\n")
report.write("----------------------------------------------------\n")

missing = df.isnull().sum()

total_missing = missing.sum()

if total_missing == 0:
    report.write("No missing values found.\n")
else:
    report.write("Missing Values:\n")

    for col, val in missing.items():
        if val > 0:
            report.write(f"- {col}: {val}\n")

duplicates = df.duplicated().sum()

report.write(f"\nDuplicate Rows: {duplicates}\n\n")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

#target columb

possible_targets = [
    "Productivity_Score",
    "Productivity",
    "Burnout_Level",
    "Burnout",
    "Stress_Level",
    "Performance_Score"
]

target_column = None

for col in possible_targets:
    if col in df.columns:
        target_column = col
        break

# fallback if not found
if target_column is None:
    target_column = numeric_cols[-1]

report.write("3. TARGET COLUMN SELECTED\n")
report.write("----------------------------------------------------\n")

report.write(f"Target Column Used: {target_column}\n\n")

#correlation features

correlation_matrix = df[numeric_cols].corr()

target_corr = correlation_matrix[target_column].sort_values(
    ascending=False
)

#important features

report.write("4. MOST INFLUENTIAL FEATURES\n")
report.write("----------------------------------------------------\n")

positive_features = []
negative_features = []

for feature, corr in target_corr.items():

    if feature == target_column:
        continue

    if corr > 0:
        positive_features.append((feature, corr))

    elif corr < 0:
        negative_features.append((feature, corr))

# Top Positive
report.write("Top Positive Influencers:\n")

for feature, corr in positive_features[:5]:
    report.write(
        f"- {feature} positively affects {target_column} "
        f"(Correlation: {round(corr,2)})\n"
    )

report.write("\n")

# Top Negative
report.write("Top Negative Influencers:\n")

for feature, corr in negative_features[:5]:
    report.write(
        f"- {feature} negatively affects {target_column} "
        f"(Correlation: {round(corr,2)})\n"
    )

report.write("\n")

#trend

report.write("5. TRENDS AND OBSERVATIONS\n")
report.write("----------------------------------------------------\n")

for feature, corr in target_corr.items():

    if feature == target_column:
        continue

    # Strong Positive
    if corr >= 0.5:
        report.write(
            f"- Higher values of '{feature}' are strongly associated "
            f"with increased '{target_column}'.\n"
        )

    # Moderate Positive
    elif corr >= 0.3:
        report.write(
            f"- '{feature}' shows moderate positive impact on "
            f"'{target_column}'.\n"
        )

    # Strong Negative
    elif corr <= -0.5:
        report.write(
            f"- Higher '{feature}' is associated with lower "
            f"'{target_column}'.\n"
        )

    # Moderate Negative
    elif corr <= -0.3:
        report.write(
            f"- '{feature}' has moderate negative relationship with "
            f"'{target_column}'.\n"
        )

report.write("\n")

#correlatoin features

report.write("6. HIGHLY CORRELATED FEATURES\n")
report.write("----------------------------------------------------\n")

found = False

for i in range(len(correlation_matrix.columns)):
    for j in range(i):

        col1 = correlation_matrix.columns[i]
        col2 = correlation_matrix.columns[j]

        corr = correlation_matrix.iloc[i, j]

        if abs(corr) > 0.8:

            found = True

            report.write(
                f"- {col1} and {col2} are highly correlated "
                f"(Correlation: {round(corr,2)})\n"
            )

if not found:
    report.write("No highly correlated features found.\n")

report.write("\n")

#dataset issue

report.write("7. POSSIBLE ISSUES IN DATASET\n")
report.write("----------------------------------------------------\n")

if total_missing > 0:
    report.write("- Dataset contains missing values.\n")

if duplicates > 0:
    report.write("- Dataset contains duplicate rows.\n")

report.write(
    "- Correlation does not always imply causation.\n"
)

report.write(
    "- Some patterns may be synthetic or artificially generated.\n"
)

report.write(
    "- Extreme outliers may affect analysis results.\n\n"
)

#conclusion

report.write("8. FINAL CONCLUSION\n")
report.write("----------------------------------------------------\n")

report.write(
    f"The dataset analysis shows that '{target_column}' is "
    f"influenced by multiple behavioral and work-related factors. "
)

report.write(
    "Correlation analysis identified the most impactful features "
    "affecting productivity or burnout. "
)

report.write(
    "The dataset is useful for data analysis, visualization, "
    "and machine learning tasks related to workplace wellness.\n"
)

report.write("REPORT GENERATED SUCCESSFULLY\n")

report.close()

print(f"\nReport generated successfully: {report_file}")