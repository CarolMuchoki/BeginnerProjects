class Person:
    def __int__(self, name):
        self.name = name

    def talk(self):
        print('talk')


john = Person("John Smith")
print(john.name)
john.talk()




