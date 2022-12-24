'''
class collections.OrderedDict([items])
Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.

New in version 3.1.

popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

move_to_end(key, last=True)
Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:

>>>
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d)
'acdeb'
d.move_to_end('b', last=False)
''.join(d)
'bacde'
New in version 3.2.

In addition to the usual mapping methods, ordered dictionaries also support reverse iteration using reversed().

OrderedDict objects
Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations. They have become less important now that the built-in dict class gained the ability to remember insertion order (this new behavior became guaranteed in Python 3.7).

Some differences from dict still remain:

The regular dict was designed to be very good at mapping operations. Tracking insertion order was secondary.

The OrderedDict was designed to be good at reordering operations. Space efficiency, iteration speed, and the performance of update operations were secondary.

The OrderedDict algorithm can handle frequent reordering operations better than dict. As shown in the recipes below, this makes it suitable for implementing various kinds of LRU caches.

The equality operation for OrderedDict checks for matching order.

A regular dict can emulate the order sensitive equality test with p == q and all(k1 == k2 for k1, k2 in zip(p, q)).

The popitem() method of OrderedDict has a different signature. It accepts an optional argument to specify which item is popped.

A regular dict can emulate OrderedDict’s od.popitem(last=True) with d.popitem() which is guaranteed to pop the rightmost (last) item.

A regular dict can emulate OrderedDict’s od.popitem(last=False) with (k := next(iter(d)), d.pop(k)) which will return and remove the leftmost (first) item if it exists.

OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.

A regular dict can emulate OrderedDict’s od.move_to_end(k, last=True) with d[k] = d.pop(k) which will move the key and its associated value to the rightmost (last) position.

A regular dict does not have an efficient equivalent for OrderedDict’s od.move_to_end(k, last=False) which moves the key and its associated value to the leftmost (first) position.

Until Python 3.8, dict lacked a __reversed__() method.
'''