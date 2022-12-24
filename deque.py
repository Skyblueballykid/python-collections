'''
deque objects

class collections.deque([iterable[, maxlen]])
Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end. Bounded length deques provide functionality similar to the tail filter in Unix. They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

Deque objects support the following methods:

append(x)
Add x to the right side of the deque.

appendleft(x)
Add x to the left side of the deque.

clear()
Remove all elements from the deque leaving it with length 0.

copy()
Create a shallow copy of the deque.

New in version 3.5.

count(x)
Count the number of deque elements equal to x.

New in version 3.2.

extend(iterable)
Extend the right side of the deque by appending elements from the iterable argument.

extendleft(iterable)
Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

index(x[, start[, stop]])
Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found.

New in version 3.5.

insert(i, x)
Insert x into the deque at position i.

If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.

New in version 3.5.

pop()
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft()
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value)
Remove the first occurrence of value. If not found, raises a ValueError.

reverse()
Reverse the elements of the deque in-place and then return None.

New in version 3.2.

rotate(n=1)
Rotate the deque n steps to the right. If n is negative, rotate to the left.

When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

Deque objects also provide one read-only attribute:

maxlen
Maximum size of a deque or None if unbounded.

New in version 3.1.

In addition to the above, deques support iteration, pickling, len(d), reversed(d), copy.copy(d), copy.deepcopy(d), membership testing with the in operator, and subscript references such as d[0] to access the first element. Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.

Starting in version 3.5, deques support __add__(), __mul__(), and __imul__().
'''

'''
> python3
Python 3.8.9 (default, Feb 18 2022, 07:45:33)
[Clang 13.1.6 (clang-1316.0.21.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from collections import deque
>>> d = deque()
>>> d.append('a')
>>> d.append(1)
>>> d
deque(['a', 1])
>>> d.appendleft(2)
>>> d
deque([2, 'a', 1])
>>> d.count(2)
1
>>> d.extend(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> d.extend([x for x in range(5))
  File "<stdin>", line 1
    d.extend([x for x in range(5))
                                 ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> d.extend([x for x in range(5)])
>>> d
deque([2, 'a', 1, 0, 1, 2, 3, 4])
>>> d.count(1)
2
>>> e = copy(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'copy' is not defined
>>> copy(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'copy' is not defined
>>> d.clear()
>>> d
deque([])
>>> d.extend([x for x in range(5)])
>>> d
deque([0, 1, 2, 3, 4])
>>> d.extendleft([x for x in range(5)])
>>> d
deque([4, 3, 2, 1, 0, 0, 1, 2, 3, 4])
>>> d.index(4)
0
>>> d.index(3)
1
>>> d.insert(1,55)
>>> d
deque([4, 55, 3, 2, 1, 0, 0, 1, 2, 3, 4])
>>> d.pop()
4
>>> d.popleft()
4
>>> d.remove(55)
>>> d
deque([3, 2, 1, 0, 0, 1, 2, 3])
>>> d.rotate()
>>> d
deque([3, 3, 2, 1, 0, 0, 1, 2])
>>> d.rotate(n=5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: rotate() takes no keyword arguments
>>> d.rotate(5)
>>> d
deque([1, 0, 0, 1, 2, 3, 3, 2])
>>>
'''

'''
deque Recipes
This section shows various approaches to working with deques.

Bounded length deques provide functionality similar to the tail filter in Unix:

def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)
Another approach to using deques is to maintain a sequence of recently added elements by appending to the right and popping to the left:

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # https://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n
A round-robin scheduler can be implemented with input iterators stored in a deque. Values are yielded from the active iterator in position zero. If that iterator is exhausted, it can be removed with popleft(); otherwise, it can be cycled back to the end with the rotate() method:

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()
The rotate() method provides a way to implement deque slicing and deletion. For example, a pure Python implementation of del d[n] relies on the rotate() method to position elements to be popped:

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
To implement deque slicing, use a similar approach applying rotate() to bring a target element to the left side of the deque. Remove old entries with popleft(), add new entries with extend(), and then reverse the rotation. With minor variations on that approach, it is easy to implement Forth style stack manipulations such as dup, drop, swap, over, pick, rot, and roll.


'''