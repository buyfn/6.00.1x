class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
  if newFrob.myName() < atMe.myName():
    if atMe.getBefore() == None:
      newFrob.setAfter(atMe)
      atMe.setBefore(newFrob)
    else:
      insert(atMe.getBefore(), newFrob)
  else:
    if atMe.getAfter() == None:
      newFrob.setBefore(atMe)
      atMe.setAfter(newFrob)
    elif newFrob.myName() < atMe.getAfter().myName():
      newFrob.setAfter(atMe.getAfter())
      newFrob.setBefore(atMe)
      atMe.getAfter().setBefore(newFrob)
      atMe.setAfter(newFrob)
    else:
      insert(atMe.getAfter(), newFrob)

def findFront(start):
  if start.getBefore() == None:
    return start
  else:
    return findFront(start.getBefore())

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

print findFront(ruth).myName()
