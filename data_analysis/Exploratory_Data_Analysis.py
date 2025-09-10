
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

#Data Clean-Up
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

#Data Metrics
df_da_roles = df["job_title_short"].value_counts().head(5).to_frame("count")
df_da_countries = df["job_country"].value_counts().head(5).to_frame("count")
df_da_companies = df["company_name"].value_counts().head(5).to_frame("count")
dict_column = {
    'job_work_from_home': 'Work from Home Offered',
    'job_no_degree_mention': 'Degree Requirement',
    'job_health_insurance': 'Health Insurance Offered'
}
def plot_figure_1():
    # Make sure seaborn uses a nice style
    sns.set(style="whitegrid")

    # Create subplots (3 rows, 1 column for barplots)
    fig, axes = plt.subplots(3, 1)

    # --- Top Roles ---
    sns.barplot(
        x=df_da_roles['count'], 
        y=df_da_roles.index, 
        hue=df_da_roles.index,   # required for palette
        legend=False,            # disable redundant legend
        ax=axes[0], 
        palette="viridis"
    )
    axes[0].set_title("Top Data Roles")


    # --- Top Countries ---
    sns.barplot(
        x=df_da_countries['count'], 
        y=df_da_countries.index, 
        hue=df_da_countries.index,
        legend=False,
        ax=axes[1], 
        palette="plasma"
        
    )
    axes[1].set_title("Top Countries")


    # --- Top Companies ---
    sns.barplot(
        x=df_da_companies['count'], 
        y=df_da_companies.index, 
        hue=df_da_companies.index,
        legend=False,
        ax=axes[2], 
        palette="magma"
    )
    axes[2].set_title("Top Companies")
    for ax in axes:
        ax.xaxis.set_major_formatter(
            mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k')
        )
        ax.set_xlabel("")   # removes "count"
        ax.set_ylabel("")   # removes "job_title_short"
    plt.tight_layout()
    plt.show()
def plot_figure_2():
    fig, ax = plt.subplots(1, 3, figsize=(11, 3.5))

    for i, (column, title) in enumerate(dict_column.items()):
        ax[i].pie(df[column].value_counts(), labels=['False', 'True'], autopct='%1.1f%%', startangle=90)
        ax[i].set_title(title)

    plt.show()
print("> What figure do you want to show (1 or 2)?: ")
print("> Figure 1: (Roles, Countries, and Companies)")
print("> Figure 2: (Job Opportunities)")

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
