'''
namedtuple() Factory Function for Tuples with Named Fields
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.

collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.

The field_names are a sequence of strings such as ['x', 'y']. Alternatively, field_names can be a single string with each fieldname separated by whitespace and/or commas, for example 'x y' or 'x, y'.

Any valid Python identifier may be used for a fieldname except for names starting with an underscore. Valid identifiers consist of letters, digits, and underscores but do not start with a digit or underscore and cannot be a keyword such as class, for, return, global, pass, or raise.

If rename is true, invalid fieldnames are automatically replaced with positional names. For example, ['abc', 'def', 'ghi', 'abc'] is converted to ['abc', '_1', 'ghi', '_3'], eliminating the keyword def and the duplicate fieldname abc.

defaults can be None or an iterable of default values. Since fields with a default value must come after any fields without a default, the defaults are applied to the rightmost parameters. For example, if the fieldnames are ['x', 'y', 'z'] and the defaults are (1, 2), then x will be a required argument, y will default to 1, and z will default to 2.

If module is defined, the __module__ attribute of the named tuple is set to that value.

Named tuple instances do not have per-instance dictionaries, so they are lightweight and require no more memory than regular tuples.

To support pickling, the named tuple class should be assigned to a variable that matches typename.

Changed in version 3.1: Added support for rename.

Changed in version 3.6: The verbose and rename parameters became keyword-only arguments.

Changed in version 3.6: Added the module parameter.

Changed in version 3.7: Removed the verbose parameter and the _source attribute.

Changed in version 3.7: Added the defaults parameter and the _field_defaults attribute.

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
x, y = p                # unpack like a regular tuple
x, y
(11, 22)
p.x + p.y               # fields also accessible by name
33
p                       # readable __repr__ with a name=value style
Point(x=11, y=22)
'''