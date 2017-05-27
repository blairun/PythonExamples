class A(object):
    def a1(self):
        """ This is an instance method. """
        print("Hello from an instance of A")

    @classmethod
    def a2(cls):
        """ This a classmethod. """
        print("Hello from class A")

class B(object):
    def b1(self):
        print(A().a1()) # => prints 'Hello from an instance of A'
        print(A.a2()) # => 'Hello from class A'
