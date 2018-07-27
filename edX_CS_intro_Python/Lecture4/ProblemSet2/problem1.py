 # Test Case 1:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
    
# Result Your Code Should Generate Below:
# Remaining balance: 31.38

def year1Balance(b, air, mpr):
    month = 12
   
    while month > 0:
        MonthlyInterestRate= (air) / 12.0
        MinimumMonthlyPayment = (mpr) * (b)
        MonthlyUnpaidBalance = b - (MinimumMonthlyPayment)
        b = (MonthlyUnpaidBalance) + (MonthlyInterestRate * MonthlyUnpaidBalance)
        # print('Remaining balance:' ,round(b,2))
        month -= 1

    return b

print('Remaining balance:' , round(year1Balance(balance, annualInterestRate, monthlyPaymentRate),2))