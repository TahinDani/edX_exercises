# Write a program that calculates the minimum fixed monthly payment needed in order pay off 
# a credit card balance within 12 months. By a fixed monthly payment, we mean a single number 
# which does not change each month, but instead is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal


def fixedMonthlyPayment(balance, annualInterestRate):
    previous_balance = balance
    monthly_interest_rate = annualInterestRate / 12
    fixed_monthly_payment = 0
    while previous_balance > 0:
        # if debt not payable with previous fixed_montly_payment increase it by 10 and reset balance to original
        fixed_monthly_payment += 10
        previous_balance = balance
        # try to pay the debt with current fixed_monthy_payment in 12 months:
        for i in range(12):
            monthly_unpaid_balance = previous_balance - fixed_monthly_payment
            updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
            previous_balance = updated_balance
            if previous_balance < 0:
                print("Lowest Payment: " + str(fixed_monthly_payment))
                break

fixedMonthlyPayment(3329, 0.2) #310
fixedMonthlyPayment(4773, 0.2) #440
fixedMonthlyPayment(3926, 0.2) #360
