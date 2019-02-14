from faker import Faker
import pandas as pd
import random
import sqlalchemy
import pyodbc
import datetime

#Generate 100k records of fake data and do an one-time import to the database

def DataGeneration():
	fake = Faker()
	print("Start of fake data generation at: " +datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'))
	#Create a dictionary to hold the fake data
	Patient_dict=[]
	#Populate the dictionary with 100.000 records of fake data
	for i in range(100000):
		Patient_dict.append({'Name':fake.name()
		,'PhoneNumber':fake.phone_number()
		,'Address':fake.address()
		,'City':fake.city()
		,'BirthDate':fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90)
		,'Height':random.randint(150, 200)
		,'Weight':random.randint(45, 120)})
	#Convert the dictionary to a data frame
	Patient_df=pd.DataFrame(Patient_dict)
	#Reassign the index value to start from 1
	Patient_df.index = range(1,len(Patient_df)+1)
	print("End of fake data generation at: "+datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'))
	DatabaseImport(Patient_df)

def DatabaseImport(Patient_df):	
	print("Importing to SQL Server..")
	#Connect to SQL Server and import the data
	engine = sqlalchemy.create_engine("mssql+pyodbc://etl:Let523!@localhost/HealthcareDB?driver=SQL+Server+Native+Client+11.0")
	Patient_df.to_sql('Patient',engine,schema='dbo',if_exists='append', index=True, index_label='Id') #use the index of the data frame as the Id of the table
	print("Import is done at:"+datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'))


def main():
	DataGeneration() #Generate data and call DatabaseImport() function to import data


if __name__== "__main__":
	main()