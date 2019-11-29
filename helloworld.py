class HelloWorld:

    def __init__(self, name):
        self.name = name.capitalize()
       
    def sayHi(self):
        print "Hello " + self.name + "!"

hello = HelloWorld("world")
hello.sayHi()