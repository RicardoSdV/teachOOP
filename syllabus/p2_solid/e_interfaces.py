"""
'Clients should not be forced to depend on interfaces they do not use.'

So, what that means is that each interface should do one thing, (back to the
single responsibility) and that you should have many, such that depending on
what you need in a class you can inherit from or compose the class with
the interfaces you require for that specific class.
"""