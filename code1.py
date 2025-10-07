# Jasmine Duong Brisebois, Anahita Niavarani, Ruby Freedman
# deliverable-2
#A project to observe the relation between the air quality of multiple cities around the world and respiratory health outcomes.
import numpy as np
city, date, AQI, PM2.5, ozone, temperature, hospital_admitions, pop_density = np.loadtxt("air_quality_health_dataset.csv", skiprows=5, usecols= (0,1,2,3,6,7,9,10), unpack= True)
