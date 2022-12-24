'''
class collections.Counter([iterable-or-mapping])
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

Elements are counted from an iterable or initialized from another mapping (or counter):

c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError:

>>>
c = Counter(['eggs', 'ham'])
c['bacon']                              # count of a missing element is zero
0
Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:

>>>
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry
'''



