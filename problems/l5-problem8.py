#import time

def isIn(char, aStr):
  mid = len(aStr)/2
  #print char, aStr, mid
  #time.sleep(1)
  if aStr == "":
    return False
  elif char == aStr[mid]:
    return True
  elif char < aStr[mid]:
    #print "lower \n"
    return isIn(char, aStr[:mid])
  else:
    #print "higher \n"
    return isIn(char, aStr[mid+1:])

#print isIn("j", "i")
