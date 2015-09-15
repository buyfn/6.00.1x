def f(x):
  import math
  return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
  '''
  returns: float, the amount of radiation exposed to
  '''
  radiation = 0
  time = start
  while time < stop:
    radiation += f(time)*step
    time += step
  return radiation

def testRE(cases):
  for case in cases:
    print radiationExposure(case[0], case[1], case[2])

test_cases = [(0, 5, 1),
    (5, 11, 1),
    (0, 11, 1),
    (40, 100, 1.5)]

testRE(test_cases)
