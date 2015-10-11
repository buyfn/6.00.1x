class intSet(object):
  def __init__(self):
    self.vals = []

  def insert(self, e):
    if e not in self.vals:
      self.vals.append(e)

  def member(self, e):
    return e in self.vals

  def remove(self, e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(str(e) + 'not found')

  def __str__(self):
    self.vals.sort()
    return '{' + ', '.join([str(e) for e in self.vals]) + '}'

  def intersect(self, other):
    intersection = intSet()
    for e in self.vals:
      if e in other.vals:
        intersection.insert(e)
    return intersection

  def __len__(self):
    return len(self.vals)
