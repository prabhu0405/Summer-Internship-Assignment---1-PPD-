
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

#HISTOGRAM: Distribution of Burnout Risk

plt.figure(figsize=(8,5))

sns.histplot(df['burnout_risk'], bins=10, kde=True)

plt.title("Distribution of Burnout Risk")
plt.xlabel("Burnout Risk")
plt.ylabel("Frequency")

plt.savefig("1_histogram_burnout.png")

plt.close()

#SCATTER PLOT: Average stress level vs sleep hours

sleep_stress = df.groupby('sleep_hours')['stress_level'].mean()

plt.figure(figsize=(8,5))

plt.scatter(
    sleep_stress.index,
    sleep_stress.values,
    s=100
)

plt.plot(
    sleep_stress.index,
    sleep_stress.values
)

plt.title("Average Stress Level vs Sleep Hours")
plt.xlabel("Sleep Hours")
plt.ylabel("Average Stress Level")

plt.savefig("2_scatter_sleep_stress.png")

plt.close()

#HEATMAP

important_columns = [
    'stress_level',
    'burnout_risk',
    'sleep_hours',
    'daily_screen_time',
    'doomscrolling_duration',
    'focus_sessions',
    'task_completion_rate',
    'mental_fatigue',
    'emotional_exhaustion'
]

correlation = df[important_columns].corr()

plt.figure(figsize=(10,7))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.savefig("3_heatmap.png")

plt.close()


#BAR CHART: average burnout risk by Late Night Usage


late_night = df.groupby('late_night_device_usage')['burnout_risk'].mean()

plt.figure(figsize=(8,5))

late_night.plot(kind='bar')

plt.title("Average Burnout Risk by Late Night Device Usage")
plt.xlabel("Late Night Device Usage")
plt.ylabel("Average Burnout Risk")

plt.savefig("4_bar_chart.png")

plt.close()

#BOXPLOT: doomscrolling vs burnout risk

plt.figure(figsize=(8,5))

sns.boxplot(
    x='stress_level',
    y='doomscrolling_duration',
    data=df
)

plt.title("Doomscrolling Duration Across Stress Levels")
plt.xlabel("Stress Level")
plt.ylabel("Doomscrolling Duration")

plt.savefig("5_boxplot.png")

plt.close()

print("All meaningful visualizations created successfully!")