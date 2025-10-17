import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("air_quality_health_dataset.csv")

x = data["date"].head(30)
y = data["aqi"].head(30)

plt.title("Air Quality Index Over Time")
plt.xlabel("Date")
plt.ylabel("AQI Level")

plt.plot(x, y, color="green", linestyle="-", marker="o")
plt.grid(True)
plt.show()

# This line graph shows how the air quality index changes over time.
# The grid makes it easier to see patterns and changes in air quality from day to day.