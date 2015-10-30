def getSublists(L, n):
  """
  L is not empty
  0 < n <= len(L)
  returns a list of all possible sublists in L of length n without skipping elements in L
  """
  ll = []
  for i in range(len(L) - n + 1):
    sl = []
    for j in range(i, i + n):
      sl.append(L[j])
    ll.append(sl)
  return ll

def longestRun(L):
  """
  L is not empty
  returns the length of the longest run of increasing numbers in L
  """
  cr = lr = 1
  i = 0

  while i < len(L) - 1:
    if L[i] <= L[i + 1]:
      cr += 1
      if cr > lr:
        lr = cr
    else:
      cr = 1
    i += 1

  return lr


test1 = ([1, 1, 1, 1, 4], 2)
test2 = ([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4)

#print getSublists(test2[0], test2[1])
print longestRun(test1[0])
