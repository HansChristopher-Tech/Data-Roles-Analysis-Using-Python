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
