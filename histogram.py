import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv ("air_quality_health_dataset.csv")

plt.title("Distribution of Air Quality Index Levels")
plt.xlabel("Air Quality Index")
plt.ylabel("Total Days")
plt.hist(data["aqi"].head(1827), bins=10, edgecolor="black")

# The plotted histogram takes all values of the air quality index from 2020 to 2024 and claasifies them in 10 intervals of 50 from 0 to 500.
# The resulting histogram shows us that the air quality index is evenly distributed with each interval having about 180 data points. This means that th air quality index varies a lot.