'''
ChainMap objects
New in version 3.3.

A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.

The class can be used to simulate nested scopes and is useful in templating.

class collections.ChainMap(*maps)
A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

The underlying mappings are stored in a list. That list is public and can be accessed or updated using the maps attribute. There is no other state.

Lookups search the underlying mappings successively until a key is found. In contrast, writes, updates, and deletions only operate on the first mapping.

A ChainMap incorporates the underlying mappings by reference. So, if one of the underlying mappings gets updated, those changes will be reflected in ChainMap.

All of the usual dictionary methods are supported. In addition, there is a maps attribute, a method for creating new subcontexts, and a property for accessing all but the first mapping:

maps
A user updateable list of mappings. The list is ordered from first-searched to last-searched. It is the only stored state and can be modified to change which mappings are searched. The list should always contain at least one mapping.

new_child(m=None, **kwargs)
Returns a new ChainMap containing a new map followed by all of the maps in the current instance. If m is specified, it becomes the new map at the front of the list of mappings; if not specified, an empty dict is used, so that a call to d.new_child() is equivalent to: ChainMap({}, *d.maps). If any keyword arguments are specified, they update passed map or new empty dict. This method is used for creating subcontexts that can be updated without altering values in any of the parent mappings.

Changed in version 3.4: The optional m parameter was added.

Changed in version 3.10: Keyword arguments support was added.

parents
Property returning a new ChainMap containing all of the maps in the current instance except the first one. This is useful for skipping the first map in the search. Use cases are similar to those for the nonlocal keyword used in nested scopes. The use cases also parallel those for the built-in super() function. A reference to d.parents is equivalent to: ChainMap(*d.maps[1:]).

'''