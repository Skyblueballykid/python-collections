'''
UserString objects
The class, UserString acts as a wrapper around string objects. The need for this class has been partially supplanted by the ability to subclass directly from str; however, this class can be easier to work with because the underlying string is accessible as an attribute.

class collections.UserString(seq)
Class that simulates a string object. The instance’s content is kept in a regular string object, which is accessible via the data attribute of UserString instances. The instance’s contents are initially set to a copy of seq. The seq argument can be any object which can be converted into a string using the built-in str() function.

In addition to supporting the methods and operations of strings, UserString instances provide the following attribute:

data
A real str object used to store the contents of the UserString class.

Changed in version 3.5: New methods __getnewargs__, __rmod__, casefold, format_map, isprintable, and maketrans.
'''