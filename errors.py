# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #this is a syntax error becuase the print statement is misisng brackets
print ("\n") #there are two syntax errors. Incorrect indentation and missing brackets. I have corrected them

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #syntax error. Incorrect indentation on lines 9, 10, 11, 14 and 15 which have been corrected. There is a runtime error here. although the string "24 years old" is correct, casting it into an integer is not possible because of the "years old" bit. correction: remove "years old". There is also an incorrect assignment, which is a syntax error "==" which should be "="
age = int(age_Str) 
print("I'm" + age_Str + "years old.") #incorrect variable used, changed to age_Str

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 #in inverted commas, makes this a string. removing commas. syntax error
total_years = age + years_from_now
str_total_years =str(total_years) #logical error, data was not casted as string for line 18 to work

print ("The total number of years:" + str_total_years) #syntax error, missing brackets and the data is cast as a string. removing ""

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 #runtime error, "total" is not a defined variable. changing it to total_years. Logical error as the 6 months in line 23 not accounted for. Adding this
str_total_months = str(total_months) #I have added this line because line 22 could not read string and integer(via variables) together, so casting it as a string
print ("In 3 years and 6 months, I'll be " + str_total_months + " months old") #syntax error, missing brackets

#HINT, 330 months is the correct answer
#the programme is debugged and giving the correct output 

