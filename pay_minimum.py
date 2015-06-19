balance = float(raw_input("Insert value for balance: "))
annualInterestRate = float(raw_input("Insert value for annual interest rate: "))
monthlyPaymentRate = float(raw_input("Insert value for monthly payment rate: "))

month = 0
totalPaid = 0

for month in range(0, 12):
  minimumMonthlyPayment = monthlyPaymentRate * balance
  monthlyUnpaidBalance = balance - minimumMonthlyPayment
  monthlyInterest = (annualInterestRate / 12.0) * monthlyUnpaidBalance
  balance = monthlyUnpaidBalance + monthlyInterest
  month += 1
  totalPaid = minimumMonthlyPayment
  
  print "Month: " + str(month)
  print "Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2))
  print "Remaining balance: " + str(round(balance, 2))
  
print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))