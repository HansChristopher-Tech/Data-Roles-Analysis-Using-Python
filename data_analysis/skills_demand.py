import seaborn as sns
import pandas as pd
import os
import ast
import matplotlib.pyplot as plt

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# Load Data
df = pd.read_csv(r"C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\csvs\data_jobs.csv")

# Data Clean-Up
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

# Filter Data to Philippines
df_ph = df[df["job_country"] == "Philippines"]

# Explode the skills
df_ph = df_ph.explode("job_skills")

def plot_figure_1():
    # Grouping the Data
    df_skills_count = df_ph.groupby(["job_skills", "job_title_short"]).size()
    df_skills_count = df_skills_count.reset_index(name="Skill_Count")
    df_skills_count = df_skills_count.sort_values(by="Skill_Count", ascending=False)

    # Top 3 Job Titles
    df_job_titles = df_skills_count["job_title_short"].unique().tolist()
    df_job_titles = sorted(df_job_titles[:3])

    # Plotting Skills Count
    fig, ax = plt.subplots(len(df_job_titles), 1)  # FIX: subplots

    sns.set_theme(style="ticks")

    for i, job_title in enumerate(df_job_titles):
        df_plot = df_skills_count[df_skills_count['job_title_short'] == job_title].head(5)[::-1]
        sns.barplot(
            data=df_plot,
            x='Skill_Count',
            y='job_skills',
            ax=ax[i],
            palette='dark:b_r'
        )
        ax[i].set_title(job_title)
        ax[i].set_ylabel('')
        ax[i].set_xlabel('Skill Count')
        ax[i].invert_yaxis()
        ax[i].set_xlim(0, 3000)  # uniform scale

    fig.suptitle('Top Skills in Job Postings (Philippines)', fontsize=15)
    fig.tight_layout()
    plt.show()
def plot_figure_2():
    # Job title counts
    df_job_title_count = df_ph["job_title_short"].value_counts().reset_index()
    df_job_title_count.columns = ["job_title_short", "Total_Jobs"]

    # Skills count per job title
    df_skills_count = (
        df_ph.groupby(["job_skills", "job_title_short"])
        .size()
        .reset_index(name="Skill_Count")
    )

    # Merge to compute percentages
    df_skills_perc = pd.merge(df_skills_count, df_job_title_count, on="job_title_short", how="left")
    df_skills_perc["skill_percentage"] = (df_skills_perc["Skill_Count"] / df_skills_perc["Total_Jobs"]) * 100

    # Get unique job titles (limit to top 3 for clarity)
    df_job_titles = df_skills_perc["job_title_short"].unique().tolist()[:3]

    # Plot
    fig, ax = plt.subplots(len(df_job_titles), 1)
    sns.set_theme(style="ticks")

    for i, job_title in enumerate(df_job_titles):
        df_plot = df_skills_perc[df_skills_perc['job_title_short'] == job_title].nlargest(5, "skill_percentage")[::-1]
        sns.barplot(data=df_plot, x='skill_percentage', y='job_skills', ax=ax[i], palette='dark:b_r')
        ax[i].set_title(job_title)
        ax[i].set_ylabel('')
        ax[i].set_xlabel('Skill Percentage (%)')

    fig.suptitle('Likelihood of Skills Requested in Philippines Job Postings', fontsize=15)
    fig.tight_layout()
    plt.show()
print("> What figure do you want to show (1 or 2)?: ")
print("> Figure 1: (Top Skills in Job Postings)")
print("> Figure 2: (Likelihood of Skills Requested in Philippines Job Postings)")
while True:
    question = input("> ")

    try:
        if question == "1":
            plot_figure_1()
        elif question == "2":
            plot_figure_2()
        else:
            print("Error: Please choose either 1 or 2")
            continue
    except Exception as e:
        print(f"Error: {e}")
        continue

    again = input("Do you want to print the other chart? (Y/N): ")
    if again.lower() in ["y", "yes"]:
        if question == "1":
            plot_figure_2()
        elif question == "2":
            plot_figure_1()
    else:
        break