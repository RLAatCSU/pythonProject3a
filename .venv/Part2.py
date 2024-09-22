#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13
#and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general
#version of the above problem. Ask the user for the time now (in hours) and then ask for the number of hours
#to wait for the alarm. Your program should output what the time will be on a 24-hour clock when the alarm
#goes off.

#Define while loop condition as false and current time as an integer outside 0 - 24
numberEntered = False
currentTimeInt = 24

#while loop verifies a number was entered and between 0 and 23
while numberEntered == False:
    currentTime = str(input('Enter the current time in hours (0-23)\n'))  #Ask the user to input the current time
    numberEntered = currentTime.isnumeric()                               #Verify entry is a number, exit loop if True
    if numberEntered == False:
        print('You did not enter a positive whole number.')               #Inform user they did not enter a whole number
    if numberEntered == True:
        currentTimeInt = int(currentTime)                                 #convert number entered to an integer

    if numberEntered == True and (currentTimeInt < 0 or currentTimeInt > 23): #see if time entered is 0 - 23
        numberEntered = False                                             #reset while loop condition if number entered
        print('You did not enter a number between 0 and 23.')             #is not between 0 and 23, stay in loop

#Define while loop condition as false
numberEntered = False

#while loop verifies a number was entered
while numberEntered == False:
    alarmHours = str(input('Enter the number of hours until the alarm\n'))#Ask the user to input the food charge
    numberEntered = alarmHours.isnumeric()                                #Verify entry is a number, exit loop if True
    if numberEntered == False:
        print('You did not enter a positive whole number.')               #Inform user they did not enter a number


alarmHoursInt = int(alarmHours)                                    #convert number entered to an integer
alarmAdder = alarmHoursInt % 24                                    #find remainder of alarm hours to add to current time
alarmTimeTotal = currentTimeInt + alarmAdder                       #add current time to alarm time adder
alarmTimeOfDay = alarmTimeTotal % 24                               #alarm time of day is remainder of total time
print('The time of day the alarm will go off is',alarmTimeOfDay, '(0-23)') #Print Result