class Person1:
    pass  # An empty block

p = Person1()
print(p)


class Person2:
    def say_hi(self):
        print('Hello, how are you?')

p = Person2()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()


class Person3:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person3('bh')
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()