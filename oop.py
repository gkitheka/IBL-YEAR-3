class Student:
    def __init__(self, name, estates, course):
        if not name:
            raise ValueError("please provide your name")
        self.name = name
        self.course = course
        self.estates = estates

    def __str__(self):
        return f"{self.name} is from {self.estates} and is doing{self.course}"

    #Getter for the estate
    @property
    def estates(self):
        return self._estates
    
    #Setter for estate
    @estates.setter
    def estates(self, estates):
        if estates not in ["tena", "south B", "umoja 1", "umoja 2", "karen"]:
            raise ValueError("invalid Estate")
        self._estates = estates


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("what is your name?").strip()
    estates = input("which estate do you come from?").strip()
    course = input("what course do you do?").strip()
    return(name, estates, course)

if __name__ == "__main__":
    main()