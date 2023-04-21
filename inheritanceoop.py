class Firstname:
    def __init__(self, name):
        if not name:
            raise ValueError("No name specified")
        self.name = name

class Student(Firstname):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def __str__(self):
        return f"{self.name} is studying {self.course}"

class Teacher(Firstname):
    def __init__(self, name, units):
        super().__init__(name)
        self.units =units

    def __str__(self):

class Teacher(Firstname):
    def __init__(self, name, units):
        super().__init__(name)
        self.units =units

    def __str__(self):
        return f"{self.name} is is teaching {self.units}"

def main():
    student = Student("Bostone", "Information Science")
    teacher = Teacher("Ochieng", "Python Programming")
    print(student)
    print(teacher)

if __name__ == "__main__":
    main()