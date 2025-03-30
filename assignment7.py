import pandas as pd
import matplotlib.pyplot as plt


# Task 1: Load and Explore the Dataset 
try:
    # Load the dataset 
    df = pd.read_csv('bank.txt', sep='\t')
    
    # Display first 5 rows
    print("First 5 rows:")
    print(df.head())
    
    # Check data structure
    print("\nData types:")
    print(df.dtypes)
    
    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    # Clean data: Replace 'unknown' with NaN and drop rows with missing critical data
    df.replace('unknown', pd.NA, inplace=True)
    df.dropna(subset=['job', 'education'], inplace=True)
    print("\nData after cleaning:")
    print(df.info())

except FileNotFoundError:
    print("Error: File not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
# Basic statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Group by 'job' and calculate mean 'duration' of calls
job_duration = df.groupby('job')['duration'].mean().sort_values(ascending=False)
print("\nAverage call duration by job:")
print(job_duration)

# Interesting finding: Check subscription rate ('y') by marital status
subscription_rate = df.groupby('marital')['y'].apply(lambda x: (x == 'yes').mean())
print("\nSubscription rate by marital status:")
print(subscription_rate)

# Task 3: Data Visualization
# --------------------------
plt.figure(figsize=(15, 10))

# 1. Line Chart: Call duration trends by age
plt.subplot(2, 2, 1)
df.groupby('age')['duration'].mean().plot(kind='line', color='blue')
plt.title('Average Call Duration by Age')
plt.xlabel('Age')
plt.ylabel('Duration (seconds)')

# 2. Bar Chart: Subscription rate by job
plt.subplot(2, 2, 2)
df[df['y'] == 'yes']['job'].value_counts().plot(kind='bar', color='green')
plt.title('Subscriptions by Job Type')
plt.xlabel('Job')
plt.ylabel('Count')
plt.xticks(rotation=45)

# 3. Histogram: Distribution of call durations
plt.subplot(2, 2, 3)
plt.hist(df['duration'], bins=30, color='orange', edgecolor='black')
plt.title('Distribution of Call Durations')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')

# 4. Scatter Plot: Age vs. Duration
plt.subplot(2, 2, 4)
plt.scatter(df['age'], df['duration'], alpha=0.5, color='red')
plt.title('Age vs. Call Duration')
plt.xlabel('Age')
plt.ylabel('Duration (seconds)')

plt.tight_layout()
plt.show()

