age = int(input("please enter your age between 1 and 100:"))
if age >= 100:
    print ("sorry, you're dead")#this condition works
elif age >= 65:
    print ("Enjoy you're retirement")#this condition works
elif age >=40<65:
    print("You're over the hill!")#this condition works
elif age == 21:
    print ("Congrats on your 21st") #this condition works
elif age < 13:
    print ("You qualify for the kiddie discount") #this condition works
else:
    print ("age is but a number") #this condition works

#it appears that python only works properly for the above programme if the ages are entered in a decending order. I tried all other ways and it did not work properly
