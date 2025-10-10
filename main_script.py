# Names: Jasmine Duong Brisebois, Anahita Niavarani, Ruby Freedman
# Deliverable-2: a project to observe the relation between the air quality of multiple cities around the world and respiratory health outcomes.

import numpy as np

# Loading the dataset

data= np.loadtxt ("air_quality_health_dataset.csv", skiprows=1 , usecols=(1,2,3,6,7,9))

# Attributing numpy arrays to each coloun

#Selecting all rows in a coloumn  using Numpy array slicing 
col2= data[:,1]
col3= data[:,2]
col4= data[:,3]
col5= data[:,6]
col6= data[:,7]
col7= data[:,9]

print("Coloumn 1:", col3)