import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv ("air_quality_health_dataset.csv")


# Part 3 Manipulating Data

count_urban = 0
count_suburban = 0
count_rural = 0

for i in data["population_density"]:
    if i == "Urban":
        count_urban += 1
    elif i == "Suburban":
        count_suburban += 1
    else:
        count_rural += 1

print(count_urban)
print(count_suburban)
print(count_rural)