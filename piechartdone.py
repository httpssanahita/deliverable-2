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

y=([count_urban, count_suburban, count_rural])
mylabels = ["Urban", "Suburban", "Rural"]

plt.title("Population Density")
plt.pie(y, labels = mylabels)

# We started by counting how many data points corresponded to each population density indicators using a for loop.
# Then using the list comprising of the counts, we plotted a pie chart that represent how many data point were taken in urban, suburban and rural locations.
# The resulting pie chart shows us that more than half of the data points were collected from urban locations.