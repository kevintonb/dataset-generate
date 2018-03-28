from __future__ import division
import csv
import random as rd

#Avergage score of all the features that are included
avg=[]

#Features for incubators
preferred_total_market=[]
preferred_current_stage=[]


#Initializing features
total_market=[]
available_market=[]
business_model=[]
current_stage=[]
label=[]

record_count=input("Enter number of records to generate \n ")

for i in range(0,record_count):
	'''
	Adding generated values
	Modify the Random Value range to get desired range of values
	'''

	#For Incubators
	preferred_total_market.append(rd.randint(0,3))
	preferred_current_stage.append(rd.randint(0,3))

	#For Entrepreneurs
	total_market.append(rd.randint(0,3))
	available_market.append(rd.randint(0,3))
	business_model.append(rd.randint(0,3))
	current_stage.append(rd.randint(0,3))

	#Converting into Integer Datatype
	preferred_total_market=list(map(int,total_market))
	preferred_current_stage=list(map(int,available_market))

	total_market=list(map(int,total_market))
	available_market=list(map(int,available_market))
	business_model=list(map(int,business_model))
	current_stage=list(map(int,current_stage))

	avg_value=(total_market[i]+available_market[i]+business_model[i]+current_stage[i])/4
	score=((avg_value)*100/3)
	if score<=55 and preferred_total_market[i]==total_market[i]:
		score=score+10
	if score<=65 and preferred_current_stage==current_stage:
		score=score+5

	avg.append(score)
	avg=list(map(int,avg))

	label.append(score)

label=list(map(int,label))

with open("data-generated.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	rows = zip(preferred_total_market,preferred_current_stage,total_market,available_market,business_model,current_stage,label)
	for row in rows:
		wr.writerow(row)

with open("features.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	rows = zip(preferred_total_market,preferred_current_stage,total_market,available_market,business_model,current_stage)
	for row in rows:
		wr.writerow(row)

with open("labels.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	rows = zip(label)
	for row in rows:
		wr.writerow(row)
