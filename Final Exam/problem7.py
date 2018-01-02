class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        for i in self.vals.keys():
            if i == e and self.vals[i] > 0:
                self.vals[i] = 0

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        for i in self.vals.keys():
            if i == e and self.vals[i] > 0:
                return True
        return False

myAset = ASet()
myAset.insert(4)
myAset.insert(4)
myAset.insert(5)
myAset.insert(5)
myAset.insert(6)
print(myAset.vals)
print(myAset)
print(myAset.is_in(4))
print(myAset.is_in(5))
print(myAset.is_in(6))
print(myAset.is_in(7))
myAset.insert(7)
myAset.remove(7)
print(myAset.vals)
print(myAset.is_in(7))