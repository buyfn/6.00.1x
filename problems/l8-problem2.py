cases = [[[0, 2, 4], 1], 
  [[0, 2, 4], 4], 
  [[0, 2, 4], 0]]

def FancyDivide(numbers, index):
  try: 
    try:
      denom = numbers[index]
      for i in range(len(numbers)):
        numbers[i] /= denom
    finally:
      raise Exception("0")
  except Exception, e:
    print e

def FancyDivideTest(cases):
  for case in cases:
    print case
    FancyDivide(case[0], case[1])

#FancyDivide([0, 2, 4], 1)
FancyDivideTest(cases)
