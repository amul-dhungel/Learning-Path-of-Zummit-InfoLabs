import pandas as pd

# reading csv data
titanic_data = pd.read_csv('titanic.csv')
print(titanic_data.head())

# customizing headers
col_names = ['Id',
             'Survived',
             'Passenger Class',
             'Full Name',
             'Gender',
             'Age',
             'SibSp',
             'Parch',
             'Ticket Number',
             'Price', 'Cabin',
             'Station']

c_titanic_data = pd.read_csv('titanic.csv',names=col_names,skiprows=[0])

print(c_titanic_data.head())

# skipping multiples rows
c_titanic_data = pd.read_csv('titanic.csv',names=col_names,skiprows=[0,1,3])

print(c_titanic_data.head(10))

# removing headers
c_titanic_data = pd.read_csv('titanic.csv',names=col_names,skiprows=[0], header=None)
print(c_titanic_data.head(10))

# converting data frame into csv
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv('cities.csv', index=False)
citiesCSV = pd.read_csv('cities.csv')
print(citiesCSV.head())

# Handling missing values
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida'], ['Washington DC', pd.NA]], columns=['City', 'State'])
cities.to_csv('cities.csv', index=False, na_rep='Unknown')

