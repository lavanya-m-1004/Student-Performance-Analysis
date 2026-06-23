import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("data/StudentsPerformance.csv")
print("Dataset Loaded Successfully!")
print(df.head())
print("\nShape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())

# Create total score column
df["total_score"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
)

print("\nTop 5 Students:")
print(
    df.sort_values(
        by="total_score",
        ascending=False
    ).head(5)
)

print("\nBottom 5 Students:")
print(
    df.sort_values(
        by="total_score"
    ).head(5)
)

print("\nAverage Score by Gender:")
print(
    df.groupby("gender")[
        ["math score", "reading score", "writing score"]
    ].mean()
)

avg_scores = [
    df["math score"].mean(),
    df["reading score"].mean(),
    df["writing score"].mean()
]

subjects = ["Math", "Reading", "Writing"]

plt.figure(figsize=(6,4))
plt.bar(subjects, avg_scores, color=["blue", "green", "orange"])

plt.title("Average Scores by Subject")
plt.ylabel("Average Score")

plt.savefig("charts/average_scores.png")
plt.show()

gender_avg = df.groupby("gender")[
    ["math score", "reading score", "writing score"]
].mean()

gender_avg.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Gender-wise Average Scores")
plt.ylabel("Average Score")
plt.xlabel("Gender")

plt.savefig("charts/gender_performance.png")
plt.show()

plt.figure(figsize=(6,4))

df["total_score"].hist(
    bins=20,
    color="skyblue",
    edgecolor="black"
)

plt.title("Distribution of Total Scores")
plt.xlabel("Total Score")
plt.ylabel("Number of Students")

plt.savefig("charts/total_score_distribution.png")
plt.show()
