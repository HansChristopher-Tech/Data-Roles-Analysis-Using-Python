import seaborn as sns
import pandas as pd
import os
import ast
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# Load Data
df = pd.read_csv(r"C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\csvs\data_jobs.csv")

# Data Clean-Up
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

# === Figure 1: Salary Distribution ===
def plot_figure_1():
    # Filter only jobs in PH + remove NaN salaries
    df_ph_da = df[(df["job_country"] == "Philippines")].copy()
    df_ph = df_ph_da.dropna(subset=["salary_year_avg"]).copy()

    # Convert salary to PHP (assuming 1 USD = 56 PHP)
    df_ph["salary_year_avg_php"] = df_ph["salary_year_avg"] * 56
    sns.set_theme(style="ticks", rc={"figure.figsize": (10, 6)})
    ax = sns.boxplot(
        data=df_ph,
        x="salary_year_avg_php",
        y="job_title_short",
        palette="Set3"
    )

    sns.despine()

    # Titles and labels
    ax.set_title("Salary Distributions of Data Analyst Roles in the Philippines", fontsize=14, weight="bold", pad=15)
    ax.set_xlabel("Yearly Salary (PHP)", fontsize=12)
    ax.set_ylabel("")

    # Format x-axis in millions
    ticks_x = mtick.FuncFormatter(lambda x, pos: f'₱{int(x/1_000_000)}M')
    ax.xaxis.set_major_formatter(ticks_x)

    plt.tight_layout()
    plt.show()


# === Figure 2: Skills (Top Paid vs Most Demand) ===
def plot_figure_2():
    # Filter only Data Analyst jobs in PH + remove NaN salaries
    df_ph_da = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "Philippines")].copy()
    df_ph = df_ph_da.dropna(subset=["salary_year_avg"]).copy()

    # Convert salary to PHP (assuming 1 USD = 56 PHP)
    df_ph["salary_year_avg_php"] = df_ph["salary_year_avg"] * 56
    df_ph_skills = df_ph.explode("job_skills")

    # Top 10 highest-paying skills
    df_ph_top_pay = (
        df_ph_skills
        .groupby("job_skills")
        .agg(
            skill_count=("job_skills", "count"),
            median_salary=("salary_year_avg_php", "median")
        )
        .reset_index()
        .sort_values(by="median_salary", ascending=False)
        .head(10)
    )

    # Top 10 most in-demand skills
    df_ph_most_demand = (
        df_ph_skills
        .groupby("job_skills")
        .agg(
            skill_count=("job_skills", "count"),
            median_salary=("salary_year_avg_php", "median")
        )
        .reset_index()
        .sort_values(by="skill_count", ascending=False)
        .head(10)
    )

    # Plotting
    sns.set_theme(style="ticks", rc={"figure.figsize": (10, 10)})
    fig, ax = plt.subplots(2, 1, figsize=(12, 10))

    # Top 10 Highest Paid Skills
    sns.barplot(
        data=df_ph_top_pay,
        x="median_salary",
        y="job_skills",
        palette="dark:b_r",
        ax=ax[0]
    )
    ax[0].set_title("Top 10 Highest Paid Skills for Data Analysts in the Philippines", fontsize=13, weight="bold")
    ax[0].set_xlabel("Median Yearly Salary (PHP)")
    ax[0].set_ylabel("")
    ax[0].xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'₱{int(x/1_000_000)}M'))

    # Top 10 Most In-Demand Skills
    sns.barplot(
        data=df_ph_most_demand,
        x="skill_count",
        y="job_skills",
        palette="dark:g",
        ax=ax[1]
    )
    ax[1].set_title("Top 10 Most In-Demand Skills for Data Analysts in the Philippines", fontsize=13, weight="bold")
    ax[1].set_xlabel("Job Postings Count")
    ax[1].set_ylabel("")

    sns.despine()
    plt.tight_layout()
    plt.show()


# === User Choice Loop ===
print("> What figure do you want to show (1 or 2)?: ")
print("> Figure 1: Salary Distribution for Data Analysts in the Philippines")
print("> Figure 2: Highest Paid Skills and Most In-Demand Skills")

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
