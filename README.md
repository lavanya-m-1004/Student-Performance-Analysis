# 🎓 Student Performance Analysis

## 📌 Project Overview

Student Performance Analysis is a Python-based data analytics project designed to evaluate and visualize student academic performance using real-world educational data. This project demonstrates the complete data analysis workflow, including data collection, preprocessing, statistical analysis, performance evaluation, and data visualization. The objective is to transform raw student records into meaningful insights that support academic performance assessment and decision-making.

---

## 🎯 Project Objectives

- Analyze student performance across multiple subjects.
- Calculate and evaluate overall academic scores.
- Identify top-performing and low-performing students.
- Compare performance trends based on gender.
- Generate visual insights through charts and graphs.
- Apply data analytics techniques to educational datasets.

---

## 📂 Dataset Information

### Dataset Name
Students Performance Dataset

### Total Records
1000 Student Records

### Features Included

| Feature | Description |
|----------|-------------|
| Gender | Student Gender |
| Race/Ethnicity | Student Group Classification |
| Parental Level of Education | Parent Educational Background |
| Lunch | Lunch Type |
| Test Preparation Course | Course Completion Status |
| Math Score | Mathematics Marks |
| Reading Score | Reading Marks |
| Writing Score | Writing Marks |

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- Matplotlib

### Development Tools
- Visual Studio Code
- Git
- GitHub

### Version Control
- Git
- GitHub Repository Management

---

## 📁 Project Structure

```text
Student_Performance_Analysis/
│
├── data/
│   └── StudentsPerformance.csv
│
├── charts/
│   ├── average_scores.png
│   ├── gender_performance.png
│   └── total_score_distribution.png
│
├── reports/
│   ├── Project_Summary.txt
│   ├── output_1.jpeg
│   ├── output_2.jpeg
│   ├── output_3.jpeg
│   └── output_4.jpeg
│
├── analysis.py
│
├── gitignore
│
├── License
│
└── README.md
```

---

# ⚙️ Project Workflow

## Step 1: Import Required Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```

Purpose:
- Data manipulation using Pandas
- Data visualization using Matplotlib

---

## Step 2: Load Dataset

```python
df = pd.read_csv("data/StudentsPerformance.csv")
```

Purpose:
- Read dataset into a DataFrame
- Prepare data for analysis

---

## Step 3: Data Exploration

Performed the following operations:

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
```

Analysis Included:
- Dataset preview
- Number of rows and columns
- Column names
- Data types

---

## Step 4: Missing Value Analysis

```python
print(df.isnull().sum())
```

Purpose:
- Detect incomplete records
- Verify dataset quality

### Result

✅ No Missing Values Found

---

## Step 5: Statistical Analysis

```python
print(df.describe())
```

Generated:

- Mean
- Median
- Standard Deviation
- Minimum Values
- Maximum Values
- Quartiles

---

## Step 6: Total Score Calculation

```python
df["total_score"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
)
```

Purpose:
- Evaluate overall student performance

---

## Step 7: Top Performers Analysis

```python
df.sort_values(
    by="total_score",
    ascending=False
).head(5)
```

Purpose:
- Identify highest-performing students

### Output

Top 5 Students based on Total Score

---

## Step 8: Low Performers Analysis

```python
df.sort_values(
    by="total_score"
).head(5)
```

Purpose:
- Identify students requiring academic improvement

### Output

Bottom 5 Students based on Total Score

---

## Step 9: Gender-wise Analysis

```python
df.groupby("gender")[
    ["math score",
     "reading score",
     "writing score"]
].mean()
```

Purpose:
- Compare academic performance between genders

### Findings

- Female students achieved higher average scores in Reading and Writing.
- Male students showed competitive performance in Mathematics.

---

# 📊 Data Visualizations

---

## 1️⃣ Average Scores by Subject

### Code

```python
avg_scores = [
    df["math score"].mean(),
    df["reading score"].mean(),
    df["writing score"].mean()
]

subjects = [
    "Math",
    "Reading",
    "Writing"
]

plt.bar(subjects, avg_scores)
```

### Output

📈 average_scores.png

Purpose:
- Compare average subject performance.

---

## 2️⃣ Gender-wise Performance Analysis

### Code

```python
gender_avg = df.groupby("gender")[
    ["math score",
     "reading score",
     "writing score"]
].mean()

gender_avg.plot(kind="bar")
```

### Output

📈 gender_performance.png

Purpose:
- Compare academic performance by gender.

---

## 3️⃣ Total Score Distribution

### Code

```python
df["total_score"].hist(
    bins=20
)
```

### Output

📈 total_score_distribution.png

Purpose:
- Understand score distribution patterns.

---

# 📋 Results and Findings

### Average Scores

| Subject | Average Score |
|----------|---------------|
| Mathematics | 66.09 |
| Reading | 69.17 |
| Writing | 68.05 |

### Key Insights

✅ Dataset contains no missing values.

✅ Reading achieved the highest average score.

✅ Mathematics recorded the lowest average score.

✅ Female students performed better in Reading and Writing.

✅ Student scores were concentrated around the average range.

---

# 🚀 Git Commands Used

### Initialize Repository

```bash
git init
```

### Add Files

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Student Performance Analysis"
```

### Create Main Branch

```bash
git branch -M main
```

### Connect GitHub Repository

```bash
git remote add origin https://github.com/USERNAME/Student-Performance-Analysis.git
```

### Push to GitHub

```bash
git push -u origin main
```

---

# 📚 Skills Demonstrated

### Technical Skills

- Python Programming
- Data Analysis
- Data Visualization
- Statistical Analysis
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Git Version Control
- GitHub Repository Management

### Soft Skills

- Problem Solving
- Analytical Thinking
- Documentation
- Reporting
- Data Interpretation

---

# 🎯 Project Outcome

Successfully developed a complete educational data analytics solution capable of transforming raw student performance data into meaningful insights through statistical analysis and visualization techniques.

This project demonstrates practical experience in:

- Data Analytics
- Python Programming
- Data Visualization
- Report Generation
- Git & GitHub Workflow

and serves as a foundational project for Data Analytics, Data Science, and Python Development roles.

---

## 👩‍💻 Author

### Lavanya M

B.Sc Computer Science

---

## ⭐ Repository Support

If you found this project useful, consider giving it a ⭐ on GitHub.
