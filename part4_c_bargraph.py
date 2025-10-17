import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("air_quality_health_dataset.csv")

x = np.array(data["city"].head(5))
pm25 = np.array(data["pm2_5"].head(5))
aqi = np.array(data["aqi"].head(5))

plt.title("Comparison of PM2.5 and Air Quality Index by City")
plt.xlabel("City")
plt.ylabel("Value")

plt.bar(x, pm25, color="purple", width=0.4, label="PM2.5 (µg/m³)")
plt.bar(x, aqi, color="hotpink", width=0.2, label="AQI")

plt.legend()
plt.show()

# This bar chart compares PM2.5 levels and AQI for five cities.
# Each dataset uses a different color (purple and hot pink) to make them easy to tell apart.
# It shows that cities with higher PM2.5 levels usually have higher AQI values too.