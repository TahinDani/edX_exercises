# Write a program that calculates the minimum fixed monthly payment needed in order pay off 
# a credit card balance within 12 months. By a fixed monthly payment, we mean a single number 
# which does not change each month, but instead is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal


def fixedMonthlyPayment(balance, annualInterestRate):
    MinimumFixedMonthlyPayment = 0
    PreviousBalance = balance
    MonthlyUnpaidBalance = balance
    while PreviousBalance > 0:
        MinimumFixedMonthlyPayment += 10
        for i in range(12):
            MonthlyInterestRate = annualInterestRate/12
            MonthlyUnpaidBalance = PreviousBalance - MinimumFixedMonthlyPayment
            PreviousBalance = MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance
        
    return MinimumFixedMonthlyPayment

print(fixedMonthlyPayment(3329, 0.2))
print(fixedMonthlyPayment(4773, 0.2))
