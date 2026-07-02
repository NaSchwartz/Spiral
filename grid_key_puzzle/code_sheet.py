import os
from typing import List
from random import randint

# Note: for 5 digit codes, bitarrays are more memory efficiant that lists when at least ~11% of them are meant to be used.
from bitarray import bitarray

#############################################
# Basic Printing

# Add leading zeros to an int of desired length
def int_to_string(input_number:int, digit_length:int) -> str:
    string = str(input_number)
    while(len(string)<digit_length):
        string = "0" + string
    return string

# Write all numbers from 0 to some limit with leading zeros
def print_numbers(filename:str, digit_length:int, limit:int):
    with open(filename, "w") as file:
        for i in range(limit):
            file.write(int_to_string(i, digit_length)+"\n")
    print(f"\nDone! See result in {filename}\n")


#############################################
# Random Printing

# generate a random number in some range of desired length
def generate_random_number(limit:int) -> int:
    return randint(0, limit)

# print a sample of (unique) random numbers from a range of 0 to some limit
def print_random_numbers(filename:str, digit_length:int, limit:int, sample_amount:int):
    
    # Initialize biarray for each number
    barr = bitarray(limit)
    # open file to write in
    file = open(filename, "w")
    
    # loop for each number to generate
    for i in range(sample_amount):
        while True:
            # generate a random number in range
            num = generate_random_number(limit)
            # if already chosen, try again
            if barr[num]:
                continue
            # if not chosen, mark it and print it
            else:
                barr[num] = True
                file.write(int_to_string(num, digit_length)+"\n")
                break
    # done with printing, close file and print end message
    file.close()
    print(f"\nDone! See result in {filename}\n")


#############################################
# Random Printing for Puzzle

# Same as print_random_numbers, but can insert a list of predetermined numbers at some point
def puzzle_print_random_numbers(filename:str, digit_length:int, limit:int, sample_amount:int,
                                insert_point:int, numbers:List[int]):
    
    # Initialize biarray for each number
    barr = bitarray(limit)
    # mark each number in given list
    for i in numbers:
        barr[i] = True
    # open file to write in
    file = open(filename, "w")

    # loop for each number to generate
    for i in range(sample_amount):

        # when i == insert_point, insert numbers in list (in given order)
        if i == insert_point:
            for j in numbers:
                file.write(int_to_string(j, digit_length)+"\n")
                # increment i to keep up in outer loop
                i += 1
        
        while True:
            # generate a random number in range
            num = generate_random_number(limit)
            # if already chosen, try again
            if barr[num]:
                continue
            # if not chosen, mark it and print it
            else:
                barr[num] = True
                file.write(int_to_string(num, digit_length)+"\n")
                break
    # done with printing, close file and print end message
    file.close()
    print(f"\nDone! See result in {filename}\n")


#############################################
# Main

if __name__ == "__main__":
    # predetermined_list = [111,222,333,444,555,666,777,888,999,000]
    # puzzle_print_random_numbers("numbers.txt", 5, 99999, 419, 3, predetermined_list)
    
    # introduction
    print("I added no input validation because I'm lazy lol\n"
            +"Let's handle some important infomation first...\n")
    # get recurring info first
    filenameP = input("Insert the name of the file to pint on (include .txt):\t")
    digit_lengthP = int(input("Insert number of digits in each code:\t"))
    limitP = int(input("Insert the upper limit for each code:\t"))

    while True:
        os.system('clear')
        # give the user their options
        num = input("Select an option to print stuff:\n"
                +"[1] print all numbers from 0 to the given range\n"
                +"[2] print a random sample of numbers from 0 to the given range\n"
                +"[3] print a random smaple of numbers from 0 to the given range, with an amount of preset numbers\n"
                +"[4] Quit\n")
        match(num):
            case "1":
                print_numbers(filenameP, digit_lengthP, limitP)
            case "2":
                # get sample amount and preform action
                sample_amountP = int(input("Insert the number of random codes to print:\t"))
                print_random_numbers(filenameP, digit_lengthP, limitP, sample_amountP)
            case "3":
                # get sample_amount and insert_point
                sample_amountP = int(input("Insert the number of random codes to print:\t"))
                insert_pointP = int(input("Insert the index to insert predetermined codes (indexing starts at 0):\t"))

                # get the list of codes from the user
                numbersP = list()
                index_display = 0
                while True:
                    number = input(f"Enter the number at list index {index_display}, or type \"quit\" to quit:\t")
                    if number.lower() == "quit":
                        break
                    else:
                        numbersP.append(int(number))
                        index_display += 1
                
                # preform action
                puzzle_print_random_numbers(filenameP, digit_lengthP, limitP, sample_amountP, insert_pointP, numbersP)
            case "4":
                break
            case _:
                continue
        input("Press \"Enter\" to continue.")