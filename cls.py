class Parent:
    def last_name(self):
        print("Potokii")

class Child(Parent):
    def first_name(self):
        print("Ivan")

ivan = Child()

ivan.last_name()
ivan.first_name()