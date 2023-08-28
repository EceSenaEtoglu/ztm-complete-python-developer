#practice for understanding how to create generators (iterables)
class My_Range():
    def __init__(self,first,last):
      self.first = first
      self.last = last
      self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.first < self.last:
            num = self.current
            self.current += 1
            return num
        #stop generating
        raise StopIteration

generator = My_Range(1,200)
for item in generator:
    print(item)