
import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("data.csv")

# Display dataset
print("Student Dataset:")
print(df)

# Calculate average marks
average = df["marks"].mean()
print("\nAverage Marks:", round(average, 2))

# Find highest and lowest marks
print("Highest Marks:", df["marks"].max())
print("Lowest Marks:", df["marks"].min())

# Create a chart
plt.scatter(df["study_hours"], df["marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid()
plt.savefig("study_hours_vs_marks.png")
plt.show()
