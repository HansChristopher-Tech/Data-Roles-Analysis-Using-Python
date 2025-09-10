import seaborn as sns
import pandas as pd
import os
import ast
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from adjustText import adjust_text

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# Load Data
df = pd.read_csv(r"C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\csvs\data_jobs.csv")

# Data Clean-Up
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

# Filter only Data Analyst jobs in PH + remove NaN salaries
df_ph_da = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "Philippines")].copy()
df_ph = df_ph_da.dropna(subset=["salary_year_avg"]).copy()

# Convert salary to PHP (assuming 1 USD = 56 PHP)
df_ph["salary_year_avg_php"] = df_ph["salary_year_avg"] * 56
df_ph_skills = df_ph.explode("job_skills")

# Calculate Percentage on Job Postings that have skills
df_ph_da_skills = (
    df_ph_skills
    .groupby("job_skills")
    .agg(
        skill_count=("job_skills", "count"),    
        median_salary=("salary_year_avg_php", "median") 
    )
    .sort_values(by="skill_count", ascending=False)
)

df_DA_job_count = len(df_ph_da)  # total job postings
df_ph_da_skills['Skills Percentage'] = (df_ph_da_skills["skill_count"] / df_DA_job_count) * 100

# Keep only skills that appear in > 5 of postings
df_ph_da_skills_high_demand = df_ph_da_skills.head(10)
# Plot scatter
plt.figure(figsize=(10,6))
plt.scatter(
    df_ph_da_skills_high_demand['Skills Percentage'], 
    df_ph_da_skills_high_demand['median_salary'],
    s=80, alpha=0.7
)
plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Salary (₱PHP)')
plt.title('Most Optimal Skills for Data Analysts in the Philippines')

# Format y-axis as ₱xxxK
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'₱{int(y/1000000)}M'))

# Add labels to points
texts = []
for i, txt in enumerate(df_ph_da_skills_high_demand.index):
    texts.append(
        plt.text(
            df_ph_da_skills_high_demand['Skills Percentage'].iloc[i], 
            df_ph_da_skills_high_demand['median_salary'].iloc[i], 
            " " + txt
        )
    )
# Adjust text to avoid overlap and add arrows
adjust_text(texts, 
            arrowprops=dict(arrowstyle="->", color="black", lw=1),
            force_points=0.5, force_text=0.5, expand_points=(1.2,1.2))

plt.show()
