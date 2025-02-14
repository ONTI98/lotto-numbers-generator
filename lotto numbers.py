#generate random numbers 

import random
from time import *

numbers=[]

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
      33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]

list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
      33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]

def generate_number(name_of_list):
    while True:

        ask=input("would you like to generate number (Y/N)?")

        if ask.upper() == "Y":
            generate_number=random.choice(name_of_list)
            numbers.append(generate_number)
            print(numbers)
        else:
            sleep(3)
            print(f"Your lucky numbers are {numbers}")
            print("GOOD LUCK!!!")
            break 

generate_number(name_of_list=list1)



