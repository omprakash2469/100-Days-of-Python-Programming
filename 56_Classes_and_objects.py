# Instantiate a class
class Person:
    name  = "Omprakash Prajapati"
    age  = 21
    profession  = "Software Developer"
    location  = "Pune"

    def info(self):
        print(self.name, "is a", self.profession)


user = Person()

# Access value in class
user.name = "Kiran Kale"
user.profession = "Videographer"
user.info()