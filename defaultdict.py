'''
defaultdict objects

class collections.defaultdict(default_factory=None, /[, ...])
Return a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.

The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.

defaultdict objects support the following method in addition to the standard dict operations:

__missing__(key)
If the default_factory attribute is None, this raises a KeyError exception with the key as argument.

If default_factory is not None, it is called without arguments to provide a default value for the given key, this value is inserted in the dictionary for the key, and returned.

If calling default_factory raises an exception this exception is propagated unchanged.

This method is called by the __getitem__() method of the dict class when the requested key is not found; whatever it returns or raises is then returned or raised by __getitem__().

Note that __missing__() is not called for any operations besides __getitem__(). This means that get() will, like normal dictionaries, return None as a default rather than using default_factory.

defaultdict objects support the following instance variable:

default_factory
This attribute is used by the __missing__() method; it is initialized from the first argument to the constructor, if present, or to None, if absent.

Changed in version 3.9: Added merge (|) and update (|=) operators, specified in PEP 584.
'''