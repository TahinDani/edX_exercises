# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly 
# payment required by the credit card company each month.
# The following variables contain values as described below:

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    PreviousBalance = balance
    for i in range(12):
        MonthlyInterestRate = annualInterestRate/12
        MinimumMonthlyPayment = monthlyPaymentRate*PreviousBalance
        MonthlyUnpaidBalance = PreviousBalance - MinimumMonthlyPayment
        PreviousBalance = MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance
        #print(round(PreviousBalance, 2))
    print("Remaining balance: " + str(round(PreviousBalance, 2)))

remainingBalance(42, 0.2, 0.04) #31.38
