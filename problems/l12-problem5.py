def genPrimes(): 
  primes = [] 
  n = 1 
  while True:
    n += 1
    isPrime = True
    for prime in primes:
      if n % prime == 0:
        isPrime = False
        break
    if isPrime:
      try:
        print len(primes), '\t', n, '\t', (n - primes[-1])
      except:
        pass
      yield n
      primes.append(n)

for prime in genPrimes():
  pass
