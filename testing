#Import the necessary library
import numpy as np
from numpy.core.fromnumeric import argmax


#Manually add the Summer Olympics, London 2012 dataset as arrays
countries = np.array(['Great Britain','China','Russia','United States','Korea','Japan', 'Germany'])
gold_medal = np.array([29,38,24,46,13,7,11])
silver_medal = np.array([17,28,25,28,8,14,11])
bronze_medal = np.array([19,22,32,29,7,17,14])

#Use the argmax() method to find the highest number of gold medals
max_gold = argmax(gold_medal)
print("Name of country with maximum gold: ", countries[max_gold])

gold_medal_20 = countries[gold_medal>20]
print(gold_medal_20)


#Use a for loop to create the required output
for i in range(len(countries)):
    country = countries[i]
    gold = gold_medal[i]
    silver = silver_medal[i]
    bronze = bronze_medal[i]
    print("country Name with number of medals:- {} -  gold {} : silver {} : bronze {}".format(country,gold,silver,bronze))

#Use a for loop to create the required output
for i in range(len(countries)):
    country = countries[i]
    gold = gold_medal[i]
    silver = silver_medal[i]
    bronze = bronze_medal[i]
    total_medals = gold+silver+bronze
    print("country Name with total number of medals:- {} -   {} ".format(country,total_medals))
