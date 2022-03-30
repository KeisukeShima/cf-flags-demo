class Index(object):
  def uncovered_if(self, var=True):
      if var:
        return False
      else:
        return True

  def fully_covered(self):
      return True

  def uncovered(self):
      return True

  def another_uncovered_function(self):
      return True

  def another_covered_function(self):
      return True
