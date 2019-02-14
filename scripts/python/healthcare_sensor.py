from faker import Faker
fake = Faker()
import pandas as pd
import random
import sqlalchemy
import pyodbc
import datetime
import time

#Generate 100k records of fake data every 1-2 minutes  and import them to the database

def DataGeneration():
	print("Start of fake data generation at: " +datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'))
	#Create a dictionary to hold the fake data
	Healthcare_dict=[]
	#Populate the dictionary with 100.000 records of fake data
	for i in range(100000):
		Healthcare_dict.append({'time':datetime.datetime.now(),
		'SystolicBloodPressure':random.randint(90, 190)
		,'DiastolicBloodPressure':random.randint(40, 140)
		,'HeartRate': random.randint(50, 250)})
	#Convert the dictionary to a data frame
	Healthcare_df=pd.DataFrame(Healthcare_dict)
	#Reset the index - it should be always between 1 and 100.000 as this is the PatientId
	Healthcare_df.reset_index(drop=True)
	#Reassign the index value to start from 1
	Healthcare_df.index = range(1,len(Patient_df)+1)
	print("End of fake data generation at: "+datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'))
	DatabaseImport(Healthcare_df)
	
def DatabaseImport(Healthcare_df):
	print("Importing to SQL Server..")
	#Connect to SQL Server and import the data
	engine = sqlalchemy.create_engine("mssql+pyodbc://etl:Let523!@localhost/HealthcareDB?driver=SQL+Server+Native+Client+11.0")
	Healthcare_df.to_sql('HealthcareData',engine,schema='dbo',if_exists='append', index=True, index_label='PatientId') #use the index of the data frame as the Id of the table
	print("Import is done at:"+datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'))

def main():
	#Counter to control the number of imports to the database	
	counter=0
	while counter<3:
		try:
			DataGeneration() #Generate data and call DatabaseImport() function to import data
			print("Collecting new data..")
			time.sleep(60) 	 #Wait 1 minute	- and start again till the user manually breaks the execution or the counter reaches the threshold
			counter=counter+1
		except KeyboardInterrupt:
			print('Manual break by user')
			return

if __name__== "__main__":
	main()
