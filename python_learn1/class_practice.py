class people:
    numberofstudent = 0
    numberofteacher = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("I am a person")

class teacher(people):
    def __init__(self, name, age):
        super().__init__(name, age)
        people.numberofteacher += 1

    def grade(self):
        print ("I am a teacher")

    def speak(self):
        print (f"I am {self.name} and I am {self.age} years old")

class student(people):
    def __init__(self, name, age):
        super().__init__(name, age)
        people.numberofstudent += 1

    def grade(self):
        print ("I am a student")

    def speak(self):
        print (f"I am {self.name} and I am {self.age} years old")


t1 = teacher("Jan", 49)
t2 = teacher("Joe", 39)
s1 = student("Bob", 15)
s2 = student("Jill", 13)
s3 = student("Bo", 9)
p1 = people("tom", 10)
print (people.numberofstudent, people.numberofteacher)

list1 = [t1, s1, p1, t2, s2, s3]

for x in list1:
    print(type(x))
    x.speak()

