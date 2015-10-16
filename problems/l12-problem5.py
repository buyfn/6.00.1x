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
      yield n
      primes.append(n)

for prime in genPrimes():
  print prime
