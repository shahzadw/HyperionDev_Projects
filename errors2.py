# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #synatx error. no "" therefore not a string. 
animal_type = "cub"
number_of_teeth = 16 

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #logical error, needs to be casted as an f string. also incorrect substitutions so the sentence isnt printing correctly grammatically

print (full_spec) #syntax error no ()

