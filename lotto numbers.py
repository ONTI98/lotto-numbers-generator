#generate random numbers
  
import random
from time import *

def main ():
    generate_powerball_number(list_name=powerball_number)
     
    generate_numbers(name_of_list=first_five)

    print()

powerball=[]
numbers=[]
previous_number=None

first_five=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
      33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

powerball_number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def generate_numbers(name_of_list):
    counter= 0
    while True:

        while counter <= 4:
                
                random_number=random.choices(first_five)
                numbers.append(random_number)

                counter +=1

                if counter == 5:
                #remove certain elements from list
                    numbers2=[i[0] for i in numbers ]
                    print(f"Lucky numbers: {numbers2}")

                else:
                     break

def generate_powerball_number(list_name):
        
    generate_powerball_number=random.choice(list_name)       
    powerball.append(generate_powerball_number)
    print(f"Powerball: {powerball}")

main ()


