# Analyze question 2: What is the correlation between the Air Quality (AQI) and the average daily temperature in urban region in 2025?
# Extracting the set of values of each variable of interest and observing the correlation coefficient 

# Introducing modules for data manipulation

import pandas as pd
import matplotlib.pyplot as plt

# Loading the data

data= pd.read_csv (r'C:\Users\anani\OneDrive\Documents\GitHub\deliverable-2\air_quality_health_dataset.csv')

# Creating a new copy of dataset only containing data of the year 2025 using To_Datetime function

data['date']= pd.to_datetime(data['date']) #Converting the date colunm into datetime using to_datetime function
data['Year']= data['date'].dt.year # Extracting only the year value using the .dt.year accessor, thus creating a new colunm for it
data_filtering_Q2 = data[(data['Year']==2025)].copy() # Selecting the year 2025 and making a copy of the dataset to not modify the original.

# Filtering data only for urban area in 2025

Urban_2025= data_filtering_Q2[data_filtering_Q2['population_density']== 'Urban'] # Creating a new dataset where the population density only contains the data corresoponding to urban region. This is obtained using the == operator to check for 'Urban' only and extracting it

# Extracting the set of data of AQI and daily average temperature of urban region in 2025

AQI_urban_2025=Urban_2025['aqi']
DAT_urban_2025= Urban_2025['temperature']

# Creating a Dataframe, Urban_df, for these two variables

Urban_df= pd.DataFrame({"AQI":[AQI_urban_2025], "Daily average temperature": [DAT_urban_2025]})

# Plotting a scatter plot 


# Computing the correlation coefficient


# Plot interpretation