'''

UserDict objects
The class, UserDict acts as a wrapper around dictionary objects. The need for this class has been partially supplanted by the ability to subclass directly from dict; however, this class can be easier to work with because the underlying dictionary is accessible as an attribute.

class collections.UserDict([initialdata])
Class that simulates a dictionary. The instance’s contents are kept in a regular dictionary, which is accessible via the data attribute of UserDict instances. If initialdata is provided, data is initialized with its contents; note that a reference to initialdata will not be kept, allowing it to be used for other purposes.

In addition to supporting the methods and operations of mappings, UserDict instances provide the following attribute:

data
A real dictionary used to store the contents of the UserDict class.

'''