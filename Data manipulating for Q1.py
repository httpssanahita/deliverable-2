# Analyze question: Is the number of respiratory hospital admissions in rural regions lower compared to the records of the urban areas?
# Comparing the mean of the records in each areas over 2 years

# Introducing modules for data manipulation

import pandas as pd
import matplotlib.pyplot as plt


data= pd.read_csv (r'C:\Users\anani\OneDrive\Documents\GitHub\deliverable-2\air_quality_health_dataset.csv')
#Inspecting data

print(data.shape) 
print(data.head(10))
print(data.info)