class Person:
    weight = 0
    name = ''
    age = 0


    def __init__(self, Name, Weight, Age, Money):
        self.name = Name
        self.weight = Weight
        self.age = Age
        self.money = Money


class Student:

    def __init__(self, name,):
        self.name = name
        self.happiness = 100
        self.sleep = 100
        self.power = 50
        self.tired = 0
        self.money = 100





    def work(self):
        self.power -= 10
        self.tired -= 20
        self.money += 50






    def relax(self, name, power, happiness, tired, student_):
        self.power += 20
        self.happiness += 10
        self.tired -= 20
        self.money -= 10



    def get_weight(self):
        self.weight += 10

    def get_age(self):
        self.age += 6


person1 = Person('Boris', 50, 14)
person2 = Person('Nikita', 60, 15)
student3 = Student('Alex')
student3.relax(student3.name, student3.power, student3.happiness, student3.tired, student3.money)
person1.name = 'Boris'
person2.name = 'Nikita'
person1.get_weight()
person1.get_age()
print(person1.name, person2.name)
print(person1.weight, person2.weight)
print(person1.age, person2.age)