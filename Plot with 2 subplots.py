# Comparing the temperature and ozone levels of London and New Mexico for the year 2024

# Introducing modules for data manipulation

import pandas as pd
import matplotlib.pyplot as plt

# Loading the data using Pandad module

data= pd.read_csv (r'C:\Users\anani\OneDrive\Documents\GitHub\deliverable-2\air_quality_health_dataset.csv')

data['date']= pd.to_datetime(data['date']) #Converting the date colunm into datetime using to_datetime function
data['Year']= data['date'].dt.year # Extracting only the year value using the .dt.year accessor, thus creating a new colunm for it
data_filtering_year= data[(data['Year']>=2023) & (data['Year']<=2024)] #Selecting the years 2023 and 2023 from the Year column
          

               
#Filtering the "city" and "Year" Columns for London and Mexico city in 2023 and 2024

# Selecting only "London" in "city" column and only data corresponding to the year 2023 and 2024
London_2023= data [ (data['city']== 'London') & (data_filtering_year['Year']==2023) ]
London_2024= data [ (data['city']== 'London') & (data_filtering_year['Year']==2024) ]

# Selecting only "Mexico city" in "city" column and only data corresponding to the year 2023 and 2023
Mexico_city_2023= data [ (data['city']== 'Mexico City') & (data['Year']==2023) ]
Mexico_city_2024= data [ (data['city']== 'Mexico City') & (data['Year']==2024) ]


# The mean values of temperature and ozone concentrations in London and Mexcio city in 2023 and 2024

Mean_london_temp_2023= London_2023['temperature'].mean()
Mean_london_temp_2024= London_2024['temperature'].mean()

Mean_Mexico_city_temp_2023= Mexico_city_2023['temperature'].mean()
Mean_Mexico_city_temp_2024= Mexico_city_2024['temperature'].mean()


# The mean value of ozone concentrations in London and Mexcio city in 2023 and 2024
Mean_london_o3_2023 = London_2023['o3'].mean()
Mean_london_o3_2024 = London_2024['o3'].mean()

Mean_Mexico_city_o3_2023 = Mexico_city_2023['o3'].mean()
Mean_Mexico_city_o3_2024 = Mexico_city_2024['o3'].mean()

# Create DataFrames of means for plotting
London_means = pd.DataFrame({
    'Year': [2023, 2024],
    'Temperature': [Mean_london_temp_2023, Mean_london_temp_2024],
    'Ozone': [Mean_london_o3_2023, Mean_london_o3_2024]
})

Mexico_means = pd.DataFrame({
    'Year': [2023, 2024],
    'Temperature': [Mean_Mexico_city_temp_2023, Mean_Mexico_city_temp_2024],
    'Ozone': [Mean_Mexico_city_o3_2023, Mean_Mexico_city_o3_2024 ]
})


# Create side-by-side bar subplots with  matplotlib.pyplot
# the function creates one figure with one or more subplots (axes) in a single grid layout
fig, axes = plt.subplots(1, 2, figsize=(14,6)) # 1 row and 2 columns give 2 side-by-side subplots
# figzi

# London subplot 
# axes[0] corresponds to the London sublpot and axes[1] corresponds to Mexico City one
# Bars are off set by 0.15 so that they don't overlap with a width of 0.3 for each bar
axes[0].bar(London_means['Year'] - 0.15, London_means['Temperature'], width=0.3, label='Temperature (℃)', color='blue')
axes[0].bar(London_means['Year'] + 0.15, London_means['Ozone'], width=0.3, label='Ozone (O3)', color='orange')
axes[0].set_xticks(London_means['Year'])
axes[0].set_title('London 2023-2024')
axes[0].set_ylabel('Mean Value')
axes[0].legend()

# Mexico City subplot
axes[1].bar(Mexico_means['Year'] - 0.15, Mexico_means['Temperature'], width=0.3, label='Temperature (℃)', color='blue')
axes[1].bar(Mexico_means['Year'] + 0.15, Mexico_means['Ozone'], width=0.3, label='Ozone (O3)', color='orange')
axes[1].set_xticks(Mexico_means['Year'])
axes[1].set_title('Mexico city 2023-2024')
axes[1].legend()

# Plot labeling 
plt.suptitle('Mean Temperature and Ozone Comparison (2023-2024)', fontsize=16) #writing a single title for both subplots in fond 16
plt.show()

# Comment on the plot
# This figure compares the temperature and ozone concentration of London and Mexico City during two consecutive years (2023 and 2024).
# The data of each country is represented it a bar subplot. We can see that the temperaure change and ozone levels of London increase at similir rates in one year
#while there is no significant correlation between the temperature change and ozone levels of Mexcio City because as the temperature drops, the ozone level doesn't decrease at teh same rate.


