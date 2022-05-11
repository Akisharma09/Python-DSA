# In python we have see a lot of variables and methods having leading or trailing underscores. In this article we will try to understand each.
## Type of underscore objects:
- Single leading underscore: _var, _method
- Single trailing underscore: var_, method_
- Double leading underscore: __var, __method
- Double leading and trailing Underscore: __var__, __method__ 
- Single Underscore: _

## Single leading underscore: _var, _method()
Single leading underscore tells programmer that this variable is only for internal use of class and should not be used outside it's scope. This does not enforce 
python interpretter to make this variable of method private, it's just a hint to python programmers's or PEP8(Python Enhancements Proposals) standards of programming.

## Single trailing underscore: var_, method_()
Single trailing underscore is basically used for naming variables that are already reserved such as count is a reserved keyword, so we can name it count_. 

## Double leading underscore: __var, __method 
Double trailing underscore is used for name mangling. What is name Mangling? python interpretter convert double underscore variables and method in a way so that when 
the variable is used in a subclass, these methods and variables are not overridden. eg:
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 13
        self.__baz = 42
    
t = Test()
print(t.foo) #11
print(t._bar) #13
print(t.__baz) #AttributeError: 'Test' object has no attribute '__baz'

__baz was not found because python interpretter renamed it as _Test__baz

print(t._Test__baz) # 42

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
 
t2 = ExtendedTest()
print(t2.foo) # 'overridden'
print(t2._bar) # 'overridden'
print(t2.__baz) #AttributeError: 'ExtendedTest' object has no attribute '__baz'

print(t2._ExtendedTest__baz) # 'overridden'
print(t2._Test__baz) # '42'
