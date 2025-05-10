import pandas as pd           # For data handling
import matplotlib.pyplot as plt  # For static plots
import seaborn as sns         # For statistical visualizations
import plotly.express as px   # For interactive plots
import geopandas as gpd
#Task 1
try:
    df = pd.read_csv("cloud_workload_dataset.csv")
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)
    
#Task 2
#Calling the df to display a preview of the table
df.head()
#Check for missing values
df.isnull().sum()
#Showcase median, mean, standard deviation etc.
df.describe()
#isolate the date from datetime
df['Task_Start_Time'] = pd.to_datetime(df['Task_Start_Time'])
df['date_only'] = df['Task_Start_Time'].dt.date
#print(df['date_only'])
#Group the data
Memory_Consumption_per_time = df.groupby(df['date_only']).size().reset_index(name='Memory_Consumption')
print(Memory_Consumption_per_time)

#Task3
# Creating the line chart

# Set the style for better visualization
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(Memory_Consumption_per_time['date_only'], Memory_Consumption_per_time['Memory_Consumption'], marker='o', linestyle='-', linewidth=2, color='#0a0a0a', markersize=8)

# Customize the plot
plt.title('Memory Consumption per year', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Memory Consumption', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Add data labels for each point
for x, y in zip(Memory_Consumption_per_time['date_only'],  Memory_Consumption_per_time['Memory_Consumption']):
    plt.text(x, y + (y * 0.02), f'{y:,}', ha='center', fontsize=9)

# Format y-axis with comma separators for thousands
plt.gca().get_yaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Create a simple bar chart
# Sort by number of active users in descending order and select top 15
top15 = df.sort_values(by='Task_Waiting_Time (ms)', ascending=True).head(15)

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(top15['Data_Source'], top15['Task_Waiting_Time (ms)'], color='orange')
plt.xlabel('Data_Source')
plt.ylabel('Task_Waiting_Times')
plt.title('Top 20 used data source based on active users')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Scatter graph
# Sort by HIV cases in descending order and select top 10
top50 = df.sort_values(by='Network_Bandwidth_Utilization (Mbps)').head(50)

# Randomize the order of the top 10
top50_random = top50.sample(frac=1, random_state=10).reset_index(drop=True)

# Create the bar plot for the randomized order
plt.figure(figsize=(10, 6))
plt.scatter(top50_random['Task_Waiting_Time (ms)'], top50_random['Network_Bandwidth_Utilization (Mbps)'], color='crimson')
plt.xlabel('Task Waiting Time (ms)')
plt.ylabel('Network Bandwidth Utilization')
plt.title('Bandwidth utilisation based on task waiting time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Create a pie chart
# Sort by Adult prevalence of HIV/AIDS in descending order and select top 20
top5 = df.sort_values(by='Error_Rate (%)', ascending=False).head(5)

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(top5['Error_Rate (%)'], labels=top5['Data_Source'], autopct='%1.1f%%', startangle=140)
plt.title('Error rate per data source %')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.tight_layout()
plt.show()