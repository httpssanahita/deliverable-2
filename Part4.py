# Part 4 Plotting Data

import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv ("air_quality_health_dataset.csv")

plt.scatter(data["temperature"], data["aqi"])