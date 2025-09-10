import seaborn as sns
import pandas as pd
import os
import ast
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import calendar  # for month names
from matplotlib.ticker import PercentFormatter

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# Load Data
df = pd.read_csv(r"C:\Users\Hans Christopher\Documents\DATA ANALYST TOOLS\PYTHON\csvs\data_jobs.csv")

# Data Clean-Up
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

# Filter: Data Analyst + Philippines
df_ph_da = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "Philippines")].copy()
df_ph_da['job_posted_month_no'] = df_ph_da["job_posted_date"].dt.month
df_ph_da_skills_exploded = df_ph_da.explode('job_skills')
def plot_figure_1():
    # Generate Pivot Table
    df_pivot = df_ph_da_skills_exploded.pivot_table(
        index="job_posted_month_no", 
        columns="job_skills", 
        aggfunc="size", 
        fill_value=0
    )

    # Reorder columns by total counts
    df_pivot.loc["Total"] = df_pivot.sum()
    df_pivot = df_pivot[df_pivot.loc['Total'].sort_values(ascending=False).index]
    df_pivot = df_pivot.drop("Total")

    # Convert month numbers → full month names
    df_pivot.index = df_pivot.index.map(lambda x: calendar.month_name[x])
    df_pivot = df_pivot.astype(int)

    # Plot
    sns.set_theme(style="whitegrid", rc={"figure.figsize": (14, 7)})

    ax = sns.lineplot(
        data=df_pivot.iloc[:, :5],  # top 5 skills
        dashes=False,
        palette="tab10",
        linewidth=2.2
    )

    # Titles only (no axis labels)
    ax.set_title(
        "Top 5 Skills Trends for Data Analyst Roles in the Philippines",
        fontsize=16,
        weight="bold",
        pad=20
    )
    ax.set_ylabel("")  # remove y-axis label
    ax.set_xlabel("")  # remove x-axis label

    # Use month names as x-ticks
    ax.set_xticks(range(len(df_pivot.index)))
    ax.set_xticklabels(df_pivot.index, rotation=45, ha="right", fontsize=10)
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

    # Legend outside for clarity
    ax.legend(
        title="Skills",
        fontsize=10,
        title_fontsize=11,
        loc="upper left",
        bbox_to_anchor=(1.01, 1)
    )

    # Add grid styling
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
def plot_figure_2():
    # Generate Pivot Table
    df_pivot = df_ph_da_skills_exploded.pivot_table(
        index="job_posted_month_no", 
        columns="job_skills", 
        aggfunc="size", 
        fill_value=0
    )
    # Get monthly totals for normalization
    df_totals = df_ph_da.groupby("job_posted_month_no").size()

    # Convert counts to percentages
    df_percent = df_pivot.iloc[:12].div(df_totals / 100, axis=0)

    # Reset index to get month names
    df_percent = df_percent.reset_index()
    df_percent['job_posted_month'] = df_percent['job_posted_month_no'].apply(
        lambda x: pd.to_datetime(str(x), format='%m').strftime('%b')
    )
    df_percent = df_percent.set_index('job_posted_month')
    df_percent = df_percent.drop(columns='job_posted_month_no')

    # Take top 5 skills
    df_plot = df_percent.iloc[:, :5]

    # Plot
    sns.set_theme(style='ticks', rc={"figure.figsize": (14, 7)})
    sns.lineplot(data=df_plot, dashes=False, legend='full', palette='tab10')
    sns.despine()  # remove top and right spines

    plt.title('Trending Top Skills for Data Analysts in the Philippines (2023)')
    plt.ylabel('Likelihood in Job Posting')
    plt.xlabel('2023')
    plt.legend()
    plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
    plt.tight_layout()
    plt.show()

print("> What figure do you want to show (1 or 2)?: ")
print("> Figure 1: (Skill Trends in the Philippines)")
print("> Figure 2: (Likelihood in Job Postings)")

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
