#this file is for the practical task in the fourth folder 
#I shall plan the solution with a pseudocode as i think a bit of planning is required here
#i tried using the and statements before but realised later that the solution is based on the total time taken
#therefore i modified the code as below by adding the variable total_time_taken
#the logic that python reads programmes like below properly when numbers(in this case times) are set in decending order only
#the comment on line 5 is my observation, happy to hear alternatives 
cycling_time_mins = int(input("please enter your cycling time in minutes:"))
swimming_time_mins = int(input("please enter your swimming time in minutes:"))
running_time_mins = int(input("please enter your running time in minutes: "))     
total_time_taken = int(cycling_time_mins+swimming_time_mins+running_time_mins)
print (total_time_taken)              
if total_time_taken>=111:
    print ("no award")
elif 106<=total_time_taken<=110:
    print ("provincial scroll")
elif 101<=total_time_taken<=105:
    print ("Provincial Half Colours")
else:
    print ("Provincial Colours")

