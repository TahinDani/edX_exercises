# Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent 
# (no more multiples of $10) such that we can pay off the debt within a year.
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0

def bisectionFixedMontlyPayment(balance, annualInterestRate):
    monthly_interest_rate = annualInterestRate / 12
    monthly_payment_lower_bound = balance / 12.0
    monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    fixed_monthly_payment = 0
    previous_balance = balance
    while previous_balance != 0:
        # if debt not payable with previous fixed_montly_payment recalculate it and reset balance to original
        fixed_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2
        previous_balance = balance
        # try to pay the debt with current fixed_monthy_payment in 12 months:
        for i in range(12):
            monthly_unpaid_balance = previous_balance - fixed_monthly_payment
            updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
            previous_balance = updated_balance
        #print(round(previous_balance,2))
        if previous_balance >= -0.01 and previous_balance <= 0.01:
            print("Lowest Payment: " + str(round(fixed_monthly_payment,2)))
            break
        if previous_balance > 0.01:
            monthly_payment_lower_bound = fixed_monthly_payment
        if previous_balance < -0.01:
            monthly_payment_upper_bound = fixed_monthly_payment

bisectionFixedMontlyPayment(320000, 0.2) # 29157.09
bisectionFixedMontlyPayment(999999, 0.18) # 90325.03
