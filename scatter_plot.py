
# Extracting a sample of values of Air quality index and daily average temperature variable corresponding to the year 2025 and observing the correlation coefficient by creating a scatter plot
# Observing how the air quality index varies with daily average temperature
# Introducing modules for data manipulation

import pandas as pd
import matplotlib.pyplot as plt

# Loading the data

data= pd.read_csv (r'C:\Users\anani\OneDrive\Documents\GitHub\deliverable-2\air_quality_health_dataset.csv')

# Creating a new copy of dataset only containing data of the year 2025 using To_Datetime function

data['date']= pd.to_datetime(data['date']) #Converting the date colunm into datetime using to_datetime function
data['Year']= data['date'].dt.year # Extracting only the year value using the .dt.year accessor, thus creating a new colunm for it
Urban_2025 = data[( data['population_density']== 'Urban') & (data['Year']==2025) ]# Selecting the rows only with urban values in the population density column in the year 2025 

#creating a Dataframe to selection columns for scatter plot
Urban_df= Urban_2025[['aqi','temperature']]

# Plotting a scatter plot 

plt.scatter(Urban_df['temperature'], Urban_df['aqi'], color= 'teal')


# Labeling the scatter plot
plt.title("Relationship between Temperature and Air Quality vs in urban areas (2025)")
plt.xlabel("Temperature (℃)")
plt.ylabel("Air Quality Index (AQI)")
plt.grid(True)
plt.show()












# Plot interpretation
