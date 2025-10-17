
# Comparing the mean of the hospital admissions in rural and urban areas from 2020 to 2023

# Introducing modules for data manipulation

import pandas as pd
import matplotlib.pyplot as plt

# Loading the data using Pandad module

data= pd.read_csv (r'C:\Users\anani\OneDrive\Documents\GitHub\deliverable-2\air_quality_health_dataset.csv')

#Inspecting data

print(data.head(3))
print(data.info) 
print(data.columns)

# Filtering the dataset for the years from 2020 to 2023

data['date']= pd.to_datetime(data['date']) #Converting the date colunm into datetime using to_datetime function
data['Year']= data['date'].dt.year # Extracting only the year value using the .dt.year accessor, thus creating a new colunm for it
data_filtering_Q1 = data[(data['Year']>=2020) & (data['Year']<= 2023)].copy() # Selecting the years we are intressted in and making a copy of the dataset to not modify the original.


print(data[['date', 'Year']])

print(data_filtering_Q1)

# Grouping the population density (area type) with the Year
Num_Row = len(data)

Rural = data_filtering_Q1[data_filtering_Q1['population_density'] == 'Rural'] #Creating a new dataset where the population denisty column only including rural area.
Urban = data_filtering_Q1[data_filtering_Q1['population_density'] == 'Urban'] #Creating a new dataset where the population denisty column only including urban area.

# Extracing the mean value of the hospital admissions data of each area type for from 2020 to 2023
# Each line of code use the function loc. known as location to locate the rows corresponding to the targated year then including its hospital admission data
Mean_Rural_2020 = Rural.loc[Rural['Year'] == 2020, 'hospital_admissions'].mean()
Mean_Rural_2021 = Rural.loc[Rural['Year'] == 2021, 'hospital_admissions'].mean()
Mean_Rural_2022 = Rural.loc[Rural['Year'] == 2022, 'hospital_admissions'].mean()
Mean_Rural_2023 = Rural.loc[Rural['Year'] == 2023, 'hospital_admissions'].mean()

Mean_Urban_2020 = Urban.loc[Urban['Year'] == 2020, 'hospital_admissions'].mean()
Mean_Urban_2021 = Urban.loc[Urban['Year'] == 2021, 'hospital_admissions'].mean()
Mean_Urban_2022 = Urban.loc[Urban['Year'] == 2022, 'hospital_admissions'].mean()
Mean_Urban_2023 = Urban.loc[Urban['Year'] == 2023, 'hospital_admissions'].mean()

# Creating tables for each area type using the pandas DataFrame function
# The table contains 3 colunms and 4 rows to substitute the mean value of each area type

Mean = pd.DataFrame({"Year" : [2020, 2021, 2022, 2023],
                         "Rural Hospital Admission" : [Mean_Rural_2020, Mean_Rural_2021, Mean_Rural_2022, Mean_Rural_2023],
                         "Urban Hospital Admission" : [Mean_Urban_2020, Mean_Urban_2021, Mean_Urban_2022, Mean_Urban_2023]
                         })


# Plotting the data 

# Plotting the Mean table made in the last step using matplotlib.pyplot
Mean.plot(kind='bar', x='Year', color = ['orange', 'blue']) 

# Labeling the plot

plt.title("Hospital Admissions by Year: Rural vs Urban")
plt.xlabel("Year")
plt.ylabel("Hospital Admissions")
plt.legend(title="Area")
plt.show()

# The significace of the plot
# Returning to the analyze question, we can not fully  confirm that the number of the hospital admissions in the rural region is lower than the ones of in urban region. The manipulation of the data demonstrates quite the opposite.
# By taking a sample of hospital admissions between the year 2020 and 2023, the generated bar plot shows a gradual decrease of the hospotial admission in the rural region as each year passes while they remain greater than the records of the urban region. This is true up until the 2023, where the average hospital admissions is higher than the rural mean.

