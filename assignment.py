                       # Question 1:
                       # Write a Python program to find those numbers which are divisible by 
                       # 7 and multiples of 5, between 1500 and 2700 (both included).


# for number in range(1500,2701):
#     if number // 7 and number % 5 == 0:
#        print(number,"Is Divisible by 7 and Multiple of 5")









                        #  Question 2:
                    #    Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
                    #    [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
                    #    Expected Output :
                    #    60°C is 140 in Fahrenheit
                    #    45°F is 7 in Celsius

# celsius = int(input("Enter temperature in Celsius"))
# fahrenheit = int(input("Enter temperature in Fahrenheit"))

# toFahrenheit = (celsius * 9/5) + 32
# toCelsius = (fahrenheit - 32) * 5/9 
# print(celsius,"C", "=" , toFahrenheit , "Fahrenheit")
# print(fahrenheit,"F", "=" , toCelsius , "Celsius")









                        #   Question 3:
                        # Write a Python program to guess a number between 1 and 9.
                        # Note : User is prompted to enter a guess. If the user guesses
                        #  wrong then the prompt appears again until the guess is correct, 
                        #  on successful guess, user will get a "Well guessed!" message, and the program will exit.

# for i in range(1,10):
#     user = int(input("Guess number"))
#     if user >= 1 and user <=9:
#         print("Write")
#         break
#     else:
#         print("worng")
#         continue








                            #   Question 4:
                            # Write a Python program to construct the following pattern, using a nested for loop.
                            #                         * 
                            #                         * * 
                            #                         * * * 
                            #                         * * * * 
                            #                         * * * * * 
                            #                         * * * * 
                            #                         * * * 
                            #                         * * 
                            #                         *

# n = 5

# for i in range(n):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('') 









                                # Question 5:
                            #   Write a Python program that accepts a word from the user and reverses it.

# user = input("Enter your name")
# reversedword = user[::-1]
# print(reversedword)












                          # Question 6:
                        # Write a Python program to count the number of even and odd numbers in a series of numbers
                        # Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
                        # Expected Output :
                        # Number of even numbers : 5
                        # Number of odd numbers : 4

# number = 1,2,3,4,5,6,7,8,9,10


# even = 0
# odd = 0
# for i in number:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even numbers is :",even)
# print("Odd numbers is :",odd)









                        #   Question 7:
                        #   . Write a Python program that prints each item and its corresponding type from the following list.
                        #   Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource',
                        #    (0, -1), [5, 12], {"class":'V', "section":'A'}]
        
# list = [1452, 11.23, 1+2j, True, "Asad", (0, -1), (5, 12), {"class":"V", "section":"A"}]

# for item in list:
#     print(item, " : ", type(item))









                            # Question 8:
                            # Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
                            # Note : Use 'continue' statement.
                            # Expected Output : 0 1 2 4 5


# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i)







                            # Question 9:
                            # . Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead
                            #  of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

# for number in range(1,51):
#     if number % 3 == 0:
#        print(number, "Fizz")
#     elif number % 5 == 0:
#         print(number, "Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#         print(number, "FizzBuzz")







              # Question 10:
            #    Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
            #    The program will print the numbers that are divisible by 5 in a comma separated sequence.
            #    Sample Data : 0100,0011,1010,1001,1100,1001
            #    Expected Output : 1010

# numbers = input("Enter comma separated 4 digit binary numbers: ")

# numbers2 = numbers.split(",")
# divisiblebyfive = []

# for number in numbers2:
#     if int(number) % 5 == 0:
#         divisiblebyfive.append(number)
#         print(divisiblebyfive)








                # Question 11:
                # Write a Python program that accepts a string and calculates the number of digits and letters.
                # Sample Data : Python 3.2
                # Expected Output :
                # Letters 6
                # Digits 2

# user = input("Enter a string and digit")

# countletters = 0
# countdigits = 0
# for char in user:
#    if char.isalpha():  
#      countletters += 1
#    elif char.isdigit():  
#      countdigits += 1

# print("Letters are :",countletters)
# print("Digits are :",countdigits)









                # Question 12:
                #  Write a Python program to check the validity of passwords input by users.
                #  Validation :
                #  At least 1 letter between [a-z] and 1 letter between [A-Z].
                #  At least 1 number between [0-9].
                #  At least 1 character from [$#@].
                #  Minimum length 6 characters.
                #  Maximum length 16 characters.



# password = input("Enter a password: ")

# Check length
# if len(password) < 6 or len(password) > 16:
#     print("Incorrect: Password must be between 6 and 16 characters long.")
# else:
#     upper = False
#     lower = False
#     digit = False
#     special = False

#     for char in password:
#         if char.isupper():
#             upper = True
#         elif char.islower():
#             lower = True
#         elif char.isdigit():
#             digit = True
#         elif char in "$@#":
#             special = True

#     # Check if all conditions are met
#     if upper and lower and digit and special:
#         print("Everything is right!")
#     else:
#         if not upper:
#             print("Incorrect: At least 1 uppercase letter must be included.")
#         if not lower:
#             print("Incorrect: At least 1 lowercase letter must be included.")
#         if not digit:
#             print("Incorrect: At least 1 digit must be included.")
#         if not special:
#             print("Incorrect: At least 1 special character (@, $, #) must be included.")










        #    Question 13:
        #     Write a Python program to find numbers between 100 and 400 (both included) 
        #     where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.


# list = []

# for i in range(100,401):
#     convert = str(i)
#     if (int(convert[0]) % 2 == 0) and (int(convert[1]) % 2 == 0) and (int(convert[2]) % 2 == 0):
#         list.append(convert)
# print(",".join(list)) 

# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str = result_str + "*" 
#         else:
#             result_str = result_str + " "  
#     result_str = result_str + "\n"  
# print(result_str)

# result_str = ""

# result_str= ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " "  
#     result_str = result_str + "\n"  
# print(result_str)

# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
#             result_str = result_str + "*" 
#         else:
#             result_str = result_str + " "  
#     result_str = result_str + "\n"  
# print(result_str)


# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " "  
#     result_str = result_str + "\n"  
# print(result_str)


# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (column == 1 or (row == 6 and column != 0 and column < 6)):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " "  
#     result_str = result_str + "\n"  
# print(result_str) 

# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
#             result_str = result_str + "* "  
#         else:
#             result_str = result_str + "  "  
#     result_str = result_str + "\n"  
# print(result_str)


# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " "  
#     result_str = result_str + "\n"  
# print(result_str) 

# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "  

#     result_str = result_str + "\n" 
# print(result_str)



# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " " 

#     result_str = result_str + "\n"  
# print(result_str)



# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or 
#             (column == 1 and (row == 1 or row == 2 or row == 6)) or 
#             (column == 5 and (row == 0 or row == 4 or row == 5))):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " "  

#     result_str = result_str + "\n"  
# print(result_str)


# row = 15    
# col = 18   
# result_str = "" 

# for i in range(1, row+1):
#     if ((i <= 3) or (i >= 7 and i <= 9) or (i >= 13 and i <= 15)):
#         for j in range(1, col):
#             result_str = result_str + "o"  
#         result_str = result_str + "\n"  
#     elif (i >= 4 and i <= 6):
#         for j in range(1, 5):
#             result_str = result_str + "o"  
#         result_str = result_str + "\n"  
#     else:
#         for j in range(1, 14):
#             result_str = result_str + " "  
#         for j in range(1, 5):
#             result_str = result_str + "o"  
#         result_str = result_str + "\n"  
# print(result_str)


# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 3 or (row == 0 and column > 0 and column <6)):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str)


# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " " 
#     result_str = result_str + "\n" 
# print(result_str)



# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((column == 1 or column == 5) and (row > 4 or row < 2)) or 
#             row == column and column > 0 and column < 6 or 
#             (column == 2 and row == 4) or 
#             (column == 4 and row == 2)):
#             result_str = result_str + "*" 
#         else:
#             result_str = result_str + " " 

#     result_str = result_str + "\n" 
# print(result_str) 



# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row + column == 6):
#             result_str = result_str + "*" 
#         else:
#             result_str = result_str + " " 

#     result_str = result_str + "\n" 
# print(result_str) 










            # Question 31:
            # . Write a Python program to calculate a dog's age in dog years.
            # Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
            # Expected Output:
            # Input a dog's age in human years: 15                                    
            # The dog's age in dog's years is 73

# age = int(input("Enter a dog's age in human years: "))

# totalage = age * 5.25
# print("Dog's age in Dog's years is ", totalage)








              # Question 32:
              # . Write a Python program to check whether an alphabet is a vowel or consonant.
              # Expected Output:
              # Input a letter of the alphabet: k                                       
              # k is a consonant.                   


# vowel = input("enter any letter from a to z")

# for i in vowel:
#   if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#     print(i, "is vowel")
#   else:
#     print(i, "is consonant")










                # Question 33:
                # Write a Python program to convert a month name to a number of days.
                # Expected Output:
                # List of months: January, February, March, April, May, June, July, August
                # , September, October, November, December                                
                # Input the name of Month: February                                       
                # No. of days: 28/29 days


# user = input("Enter a month")
# if user == "january":
#     print("No of days is 31 in", user)
# elif user == "february":
#     print("No of days is 28 or 29 in", user)
# elif user == "march":
#     print("No of days is 31 in", user)
# elif user == "april":
#     print("No of days is 30 in", user)
# elif user == "may":
#     print("No of days is 31 in", user)
# elif user == "june":
#     print("No of days is 30 in", user)
# elif user == "july":
#     print("No of days is 31 in", user)
# elif user == "august":
#     print("No of days is 31 in", user)
# elif user == "september":
#     print("No of days is 30 in", user)
# elif user == "october":
#     print("No of days is 31 in", user)
# elif user == "november":
#     print("No of days is 30 in", user)
# elif user == "december":
#     print("No of days is 31 in", user)
# else:
#     print("Invalid month name.")








                # Question 34:
                #  Write a Python program to sum two integers. However, 
                #  if the sum is between 15 and 20 it will print() 20.

# first = int(input("enter first no"))
# second = int(input("enter first no"))

# if (first >=15 and second <= 20) or (second >=15 and first <= 20):
#   print("20")
# else:
#   final =  first + second
#   print(final)







                # Question 35:
                # . Write a Python program to check if a triangle is equilateral, isosceles or scalene.
                #  Note :
                #  An equilateral triangle is a triangle in which all three sides are equal.
                #  A scalene triangle is a triangle that has three unequal sides.
                #  An isosceles triangle is a triangle with (at least) two equal sides.


# x = int(input("enter x side"))
# y = int(input("enter y side"))
# z = int(input("enter z side"))

# if x == y and y == z and z == x:
#   print("It is Equilateral traingle")
# elif x != y and y != z and z != x:
#   print("It is scalene triangle")
# elif (x == y) or (y == z) or (z == x):
#     print("It is an isosceles triangle")









                  # Question 36:
                  #  Write a Python program to display the astrological sign for a given date of birth.

# month = input("Enter a month of your DOB: ").lower()
# date = int(input("Enter a day of your DOB: "))

# if (month == "march" and date >= 21) or (month == "april" and date <= 19):       
#     print("Your Astrological Sign is Aries")
# elif (month == "april" and date >= 20) or (month == "may" and date <= 20):
#     print("Your Astrological Sign is Taurus")
# elif (month == "may" and date >= 21) or (month == "june" and date <= 20):
#     print("Your Astrological Sign is Gemini")
# elif (month == "june" and date >= 21) or (month == "july" and date <= 22):
#     print("Your Astrological Sign is Cancer")
# elif (month == "july" and date >= 23) or (month == "august" and date <= 22):
#     print("Your Astrological Sign is Leo")
# elif (month == "august" and date >= 23) or (month == "september" and date <= 22):
#     print("Your Astrological Sign is Virgo")
# elif (month == "september" and date >= 23) or (month == "october" and date <= 22):
#     print("Your Astrological Sign is Libra")
# elif (month == "october" and date >= 23) or (month == "november" and date <= 21):
#     print("Your Astrological Sign is Scorpio")
# elif (month == "november" and date >= 22) or (month == "december" and date <= 21):
#     print("Your Astrological Sign is Sagittarius")
# elif (month == "december" and date >= 22) or (month == "january" and date <= 19):
#     print("Your Astrological Sign is Capricorn")
# elif (month == "january" and date >= 20) or (month == "february" and date <= 18):
#     print("Your Astrological Sign is Aquarius")
# elif (month == "february" and date >= 19) or (month == "march" and date <= 20):
#     print("Your Astrological Sign is Pisces")
# else:
#     print("Invalid date or month. Please enter a valid date.")










            # Question 37:
            #  Write a Python program to display the sign of the Chinese Zodiac for the given year in which you were born.

# year = int(input("Enter your birth year: "))

# if year % 12 == 0:
#         print("Monkey")
# elif year % 12 == 1:
#         print("Rooster")
# elif year % 12 == 2:
#         print("Dog")
# elif year % 12 == 3:
#         print("Pig")
# elif year % 12 == 4:
#         print("Rat")
# elif year % 12 == 5:
#         print("Ox")
# elif year % 12 == 6:
#         print("Tiger")
# elif year % 12 == 7:
#         print("Rabbit")
# elif year % 12 == 8:
#         print("Dragon")
# elif year % 12 == 9:
#         print("Snake")
# elif year % 12 == 10:
#         print("Horse")
# elif year % 12 == 11:
#         print("Goat")










                # Question 38:
                # Write a Python program to find the median of three values.
                # Expected Output:        


# one = float(input("Input first number: "))
# two = float(input("Input second number: "))
# three = float(input("Input third number: "))

# if one > two:
#     if one < three:
#         median = one
#     elif two > three:
#         median = two
#     else:
#         median = three
# else:
#     if one > three:
#         median = one
#     elif two < three:
#         median = two
#     else:
#         median = three
# print(median)








            # Question 39:
            # Write a Python program to get the next day of a given date.
            

# year = int(input("Enter a year: "))

# month = int(input("Enter a month: "))
# if month in (1, 3, 5, 7, 8, 10, 12):
#     monthlength = 31
# elif month == 2:
#     monthlength = 28  
# else:
#     monthlength = 30

# day = int(input("Enter a day: "))
# if day < monthlength:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print(year, month, day)

            








              # Question 40:
              # Write a Python program to calculate the sum and average of n integer numbers 
              # (input from the user). Input 0 to finish.

# n = int(input("Enter a number (0 to finish): "))

# sum = 0
# while n!= 0:
#    sum = sum + n
#    n = int(input("Enter a number (0 to finish): "))
#    n2 = int(input("Enter a second no"))
#    totalsum = n + n2
#    average = n / n2
#    print(totalsum)
#    print(average)










            # Question 41:
            # Write a Python program to create the multiplication table (from 1 to 10) of a number.


# user = int(input("Enter a number"))

# sum = 1
# while sum <= 10:
#    print(user, "x", sum, "=", user * sum)
#    sum += 1









              # Question 42:
              # Write a Python program to construct the following pattern, using a nested loop number.
              # Expected Output:
              #                     1
              #                     22
              #                     333
              #                     4444
              #                     55555
              #                     666666
              #                     7777777
              #                     88888888
              #                     999999999


# for i in range(1, 9 + 1):
#    print(str(i) * i)


