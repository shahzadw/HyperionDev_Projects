str_manip = input("enter a sentence: ")
str_length =len(str_manip)
print(str_length)
last_letter = (str_manip[-1:]) #this is how to access the last letter of the sentence added by the user 
print (last_letter)
replace_letter = str_manip.replace(last_letter, "@") #last_letter will not be a string as it is a variable 
print (replace_letter)

#print(str_manip[str_length:13:-1]) #this is now giving the desired output but only as a hard code so won't be able to use this
#print (str_manip[str_length:-3]) #recognised a little later that i just needed to do this as done on line 4 however this still did not work

print(str_manip [::-1][:3]) #finally got this to work, but needed assistance from a friend in the community. The idea is that the string is reversed. then :3 asks python to read the reversed string 

#create a five letter word that is made up of the first three characters and the last two characters of str_manip

new_string_1 = str_manip[0:3]
new_string_2 = str_manip [-3:] #to slice the last 3 characters of a string 
print(new_string_1 + new_string_2)

