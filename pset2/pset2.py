import time

piay_tests = [(5000, 0.2),
    (3329, 0.2),
    (4773, 0.2),
    (3926, 0.2),
    (320000, 0.2),
    (999999, 0.18)]

def paying_minimum(b, annual_ir, monthly_pr):
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


def pay_in_a_year(balance, annual_ir):
  '''
  calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months
  '''
  payment = 0
  while True:
    b = balance
    for month in range(1, 13):
      b -= payment
      b += b*annual_ir/12
    if b <= 0:
      return payment
    else:
      payment += 10

def pay_in_a_year_bissection(balance, annual_ir):
  '''
  calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months using bissection search
  '''
  lo = balance / 12
  hi = balance*(1 + annual_ir/12)**12 / 12
  b = balance
  while abs(b) >= 0.01:
    b = balance
    payment = (lo + hi) / 2
    for month in range (1, 13):
      b -= payment
      b += b*annual_ir/12
    if b > 0:
      lo = payment
    else:
      hi = payment
  return round(payment, 2)

#print pay_in_a_year_bissection(5000, 0.2)

def piay_test(func, cases):
  '''
  runs pay_in_a_year function for specified cases
  '''
  for case in cases:
    print "initial balance: " + str(case[0])
    print "annual rate: " + str(case[1])
    print "minimal payment: " + str(func(case[0], case[1])) + "\n"

#paying_minimun(balance, annualInterestRate, monthlyPaymentRate)
piay_test(pay_in_a_year_bissection, piay_tests)
#print pay_in_a_year(balance, annualInterestRate)
