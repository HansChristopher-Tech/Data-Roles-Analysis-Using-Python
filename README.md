# Python-Based Data Analysis 🖥️

## Analyzing Data Roles in the Philippines  

This project is inspired by **Luke Barousse's Data Analyst Portfolio Project** on YouTube.  
The difference is that I adapted it to focus specifically on the **Philippines**, where I am from.  

### Dataset  
The dataset used in this project is credited to **Luke Barousse** and is available on his official site. 

# Goals 🏁

1. 🔍 Perform **EDA** (Exploratory Data Analysis) on data roles worldwide —  
   providing insights such as 🌍 countries with the most job postings, 🏢 top hiring companies,  
   🏡 work-from-home possibilities, and more.
2. 💰 Analyze **Salaries** to compare pay across roles, regions, and companies.
3. 🛠️ Explore **Skills** — identifying which skills 💵 pay better and 📈 are in demand.
4. 📊 Provide an **overview of skill trends**, showing how demand evolves over time.
5. 🏆 Discover the **most optimal skill** to learn for maximizing opportunities.

# EDA 🔍  

## Overview  
This section performs **Exploratory Data Analysis (EDA)** to summarize and visualize the data.  
The plots are based on the sorting and counting of different columns in the dataset.  

### Code Example
```python
# Top 5 Data Roles, Countries, and Companies
df_da_roles = df["job_title_short"].value_counts().head(5).to_frame("count")
df_da_countries = df["job_country"].value_counts().head(5).to_frame("count")
df_da_companies = df["company_name"].value_counts().head(5).to_frame("count")

# Mapping columns for visualization
dict_column = {
    'job_work_from_home': 'Work from Home Offered',
    'job_no_degree_mention': 'Degree Requirement',
    'job_health_insurance': 'Health Insurance Offered'
}
```
## Result Plots: Bar Chart 📊
[![Top 5 Roles, Countries, and Companies](charts/Top%205%20data%20internatioanl.png)](charts/Top%205%20data%20internatioanl.png)

## Result Plots: Pie Chart 🥧
[![Opportunities for Top 5 Data Roles](charts/opportunities%20for%20the%20top%205%20data%20international.png)](charts/opportunities%20for%20the%20top%205%20data%20international.png)

## Key Insights 💡

1. 👨‍💻 **Data Roles:** Data Analysts hold the most positions, followed by Data Engineers and Data Scientists.  
2. 🌍 **Job Locations:** Most jobs are concentrated in English-speaking countries like the US, India, and the UK.  
3. 🏢 **Top Company:** Empreego has posted the most jobs by a wide margin.  
4. 🏠 **Work Setup:** Most jobs are performed at the office rather than remotely.  
5. 🎓 **Degree Requirement:** Only 30% of companies worldwide require a degree.  
6. 🩺 **Benefits:** Only 11% of companies offer health insurance.
# EDA 🔍  

## Overview  
This section performs **Exploratory Data Analysis (EDA)** to summarize and visualize the data.  
The plots are based on the sorting and counting of different columns in the dataset. 
The code bellow demonstrates the method of sorting the data relevant to this section's
goal.

### Code Example
```python
# Top 5 Data Roles, Countries, and Companies
df_da_roles = df["job_title_short"].value_counts().head(5).to_frame("count")
df_da_countries = df["job_country"].value_counts().head(5).to_frame("count")
df_da_companies = df["company_name"].value_counts().head(5).to_frame("count")

# Mapping columns for visualization
dict_column = {
    'job_work_from_home': 'Work from Home Offered',
    'job_no_degree_mention': 'Degree Requirement',
    'job_health_insurance': 'Health Insurance Offered'
}
```
## Result Plots: Bar Chart 📊
[![Top 5 Roles, Countries, and Companies](charts/Top%205%20data%20internatioanl.png)](charts/Top%205%20data%20internatioanl.png)

## Result Plots: Pie Chart 🥧
[![Opportunities for Top 5 Data Roles](charts/opportunities%20for%20the%20top%205%20data%20international.png)](charts/opportunities%20for%20the%20top%205%20data%20international.png)

## Key Insights 💡

1. 👨‍💻 **Data Roles:** Data Analysts hold the most positions, followed by Data Engineers and Data Scientists.  
2. 🌍 **Job Locations:** Most jobs are concentrated in English-speaking countries like the US, India, and the UK.  
3. 🏢 **Top Company:** Empreego has posted the most jobs by a wide margin.  
4. 🏠 **Work Setup:** Most jobs are performed at the office rather than remotely.  
5. 🎓 **Degree Requirement:** Only 30% of companies worldwide require a degree.  
6. 🩺 **Benefits:** Only 11% of companies offer health insurance.

# Salary Analysis 💰

## Overview  
This section performs **Salary Analysis** to summarize and visualize the salary data in the Philippines.  
The plots are based on the sorting and counting of different columns in the dataset.  
The code below demonstrates how the data is filtered and processed for this analysis.

### Code Example
```python
# Filter only Data Analyst jobs in PH + remove NaN salaries
df_ph_da = df[(df["job_title_short"] == "Data Analyst") & (df["job_country"] == "Philippines")].copy()
df_ph = df_ph_da.dropna(subset=["salary_year_avg"]).copy()

# Convert salary to PHP (assuming 1 USD = 56 PHP)
df_ph["salary_year_avg_php"] = df_ph["salary_year_avg"] * 56

# Explode skills for analysis
df_ph_skills = df_ph.explode("job_skills")
```
## Result Plots: Bar Chart 📊
[![Salary Distributions](charts/Salary%20Distributions.png)](charts/Salary%20Distributions.png)

## Result Plots: Pie Chart 🥧
[![Highest Paid and Most In-Demand Skills](charts/Highest%20Paid%20and%20Most%20Demand%20Skills.png)](charts/Highest%20Paid%20and%20Most%20Demand%20Skills.png)

## Key Insights 💡

1. 👨‍💻 **Data Analyst Salaries:** 50% of Data Analysts in the Philippines earn between **₱3M–₱6M per year**.  
2. 📉 **Limited Data:** Machine Learning and Cloud Engineer roles show only vertical lines in the box charts, indicating very few data points are available.  
3. 🔹 **Outliers:** Only Data Engineers and Business Analysts have outliers, suggesting a relatively uniform salary trend across most roles.  
4. 💵 **Highest-Paid Skills:** BigQuery, C, Flow, Sheets, and Zoom are among the highest-paid skills in the Philippine setting, all earning over **₱6M per year**.  
5. 📊 **Most In-Demand Skills:** SQL is the most in-demand skill among data roles in the Philippines, followed by Excel and Python.

   
