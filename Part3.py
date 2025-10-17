# Part 2 Loading the Dataset

import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv ("air_quality_health_dataset.csv")

print(data["city"])
print(data.describe())
print(data.head(10))
print(data.shape) 

# Part 3 Manipulating Data

is_unhealthy = []

for value in data["aqi"]:
    if value > 50:
        is_unhealthy.append(True)
    else:
        is_unhealthy.append(False)

print(data[is_unhealthy])

# We're making a new column/list titled is_unhealthy. When the aqi level is bigger than 50 the row is True, otherwise the row is False. 
# Then we only print the rows where is_unhealthy is True. Source: https://www.youtube.com/watch?v=2AFGPdNn4FM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=8&t=595s