# Names: Jasmine Duong Brisebois, Anahita Niavarani, Ruby Freedman
# Deliverable-2: a project to observe the relation between the air quality of multiple cities around the world and respiratory health outcomes.

import pandas as pd

# Loading the dataset

data= pd.read_csv (r'C:\Users\anani\OneDrive\Documents\GitHub\deliverable-2\air_quality_health_dataset.csv')

# Attributing numpy arrays to each coloun

#Selecting all rows in a coloumn  using Numpy array slicing 
col2= data[:,1]
col3= data[:,2]
col4= data[:,3]
col5= data[:,6]
col6= data[:,7]
col7= data[:,9]

