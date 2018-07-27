import math

# Test Case 1:
balance = 4773
annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

def fixedPayment(b, air):
    MinimumFixedMonthlyPayment = b/11
    # while b >= 0:
    #     month = 11
    #     while month > 0:
    #         MonthlyInterestRate= (air) / 12.0
    #         MonthlyUnpaidBalance = b - (MinimumFixedMonthlyPayment)
    #         b = (MonthlyUnpaidBalance) + (MonthlyInterestRate * MonthlyUnpaidBalance)
    #         month -= 1
    #     # print('Lowest Payment:' ,round(b,2))
    #     MinimumFixedMonthlyPayment += 10
    return int(math.ceil(MinimumFixedMonthlyPayment / 10.0)) * 10

print('Lowest Payment:' , fixedPayment(balance, annualInterestRate))