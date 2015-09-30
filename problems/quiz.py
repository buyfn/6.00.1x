def f(x):
  while x > 3:
    f(x + 1)
    print x

def Square(x):
  return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
  if n == 0:
    return 0
  return SquareHelper(n-1, x) + x

def evalQuadratic(a, b, c, x):
  return a * x * x + b * x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
  return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)

def primesList(N):
  def isPrime(n):
    for divisor in range(2, n):
      if n % divisor == 0:
        return False
    return True

  primes = []
  for number in range (2, N + 1):
    if isPrime(number):
      primes.append(number)

  return primes

def count7(N):
  if len(str(N)) <= 1:
    if str(N) == "7":
      return 1
    else:
      return 0
  else:
    return count7(str(N)[0]) + count7(str(N)[1:])

def uniqueValues(aDict):
  uniquesList = []
  for key in aDict:
    if aDict.values().count(aDict[key]) == 1:
      uniquesList.append(key)
  return uniquesList

def satisfiesF(L):
  toRemove = []
  for elt in L:
    if not f(elt):
      toRemove.append(elt)

  for elt in toRemove:
    L.remove(elt)
  return len(L)

#run_satisfiesF(L, satisfiesF)

def f(s):
  return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L
