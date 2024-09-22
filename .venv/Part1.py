#Write a program that calculates the total amount of a meal purchased at a restaurant.
#The program should ask the user to enter the charge for the food and
#then calculate the amounts with an 18 percent tip and 7 percent sales tax.
#Display each of these amounts and the total price.

#Define while loop condition as false
numberEntered = False

#while loop verifies a number was entered
while numberEntered == False:
    mealCharge = str(input('Enter the amount charged for the meal\n'))  #Ask the user to input the food charge
    numberEntered = mealCharge.isnumeric()                              #Verify entry is a number, exit loop if True
    if numberEntered == False:
        print('You did not enter a number, please enter a number.')   #Inform user they did not enter a number

mealChargeReal = float(mealCharge)                                   #convert numeric charge to a float
print('Charge before tax $' + '{:.2f}'.format(mealChargeReal))       #print total entered to 2 decimal points
chargeSalesTax = mealChargeReal * 0.07                               #calculate sales tax
print('7% Sales Tax $' + '{:.2f}'.format(chargeSalesTax))            #print sales tax to 2 decimal points
totalWithTax = mealChargeReal + chargeSalesTax                       #calculate total with tax
print('Total with 7% Sales Tax $' + '{:.2f}'.format(totalWithTax))   #print total with tax to 2 decimal points
chargeTip = totalWithTax * 0.18                                      #calculate 18% tip
print('18% Tip $' + '{:.2f}'.format(chargeTip))                      #print 18% tip to 2 decimal points
grandTotal = totalWithTax + chargeTip                                #calculate total with tip
#Print Grand Total
print('Meal Total with 7% Sales Tax and 18% Tip $' + '{:.2f}'.format(grandTotal))