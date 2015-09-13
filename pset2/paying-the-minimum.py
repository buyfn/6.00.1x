def credit_calculator(b, annual_ir, monthly_pr):
  '''
  funciton definition
  '''

  total_paid = 0

  for month in range(1, 13):
    payment = b * monthly_pr
    total_paid += payment
    b = b - payment
    b = b + b*annual_ir/12
    print "Month: " + str(month) 
    print "Payment: " + str(round(payment, 2))
    print "Balance: " + str(round(b, 2)) + "\n"

  print "Total paid: " + str(round(total_paid, 2))
  print "Remaining balance: " + str(round(b, 2))

credit_calculator(balance, annualInterestRate, monthlyPaymentRate)
