# I am going to create 4 input lines. Each line will use an input function and will be saved under the variable names; name, age, house number, street name
#i am then going to use an f string function to get the full sentence as requested in the task 
name = input ("what is your name:")
age = input("please enter your age: ")
house_number = input ("what is your house number: ")
street_name = input ("enter your street name: ")
to_print = f"This is {name}. They are {age} years old and live at {house_number} on {street_name}"
print(to_print)