
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load the dataset
folder = Path(__file__).parent
df = pd.read_csv(folder / "data.csv")

# Display dataset
print("STUDENT PERFORMANCE ANALYSIS")
print(df.to_string(index=False))

# Basic statistics
print("\nAverage marks:", round(df["marks"].mean(), 2))
print("Highest marks:", df["marks"].max())
print("Lowest marks:", df["marks"].min())
print("Average attendance:", round(df["attendance"].mean(), 2), "%")

output = folder

# Chart 1: Study hours vs marks
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="study_hours", y="marks", s=90)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Marks")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(output / "study_hours_vs_marks.png")
plt.close()

# Chart 2: Attendance vs marks
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="attendance", y="marks")
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(output / "attendance_vs_marks.png")
plt.close()

# Chart 3: Correlation heatmap
columns = ["study_hours", "attendance", "marks"]
correlation = df[columns].corr()

print("\nCorrelation Matrix:")
print(correlation.round(2))

plt.figure(figsize=(7, 5))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)
plt.title("Student Performance Correlation")
plt.tight_layout()
plt.savefig(output / "correlation_heatmap.png")
plt.close()

print("\nAnalysis completed successfully!")
print("Charts saved inside the outputs folder.")
