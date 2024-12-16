# базовый класс:
class Mentor:             # Класс Mentor - родительский класс
    # конструктор:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return (self.firstName + ' ' + self.lastName)

# производный класс:
class Lecturer(Mentor):  # дочерний класс
    def __init__(self, firstName, lastName, Course):
        super().__init__(firstName, lastName)
        self.Course = []
        self.Course = Course

    def getCourse(self):
        return self.Course

# производный класс
class  Reviewer(Mentor):    # дочерний класс
    def __init__(self, firstName, lastName, Experts):
        super().__init__(firstName, lastName)
        self.Experts =  Experts

    def getExperts(self):
        return self.Experts

lecturer1 = Lecturer("Тимур", "Анвартдинов", "Python, знакомство с консолью")
print(lecturer1.firstName, lecturer1.lastName, lecturer1.Course)

lecturer2 = Lecturer("Олег", "Булыгин", "Основы языка программирования Python")
print(lecturer2.firstName, lecturer2.lastName, lecturer2.Course)

lecturer3 = Lecturer("Алёна", "Батицкая", "GIT - система контроля версий")
print(lecturer3.firstName, lecturer3.lastName, lecturer3.Course)

reviewer1 = Reviewer("Ксения", "Дементьева", "Python, знакомство с консолью")
print(reviewer1.firstName, reviewer1.lastName, reviewer1.Experts)

reviewer2 = Reviewer("Олег", "Пустовалов", "Python, знакомство с консолью")
print(reviewer2.firstName, reviewer2.lastName, reviewer2.Experts)

reviewer3 = Reviewer("Сергей", "Быков", "Python, знакомство с консолью")
print(reviewer3.firstName, reviewer3.lastName, reviewer3.Experts)

reviewer4 = Reviewer("Денис", "Рудаков", "Python, знакомство с консолью")
print(reviewer4.firstName, reviewer4.lastName, reviewer4.Experts)

reviewer5 = Reviewer("Алёна", "Батицкая", "GIT - система контроля версий")
print(reviewer5.firstName, reviewer5.lastName, reviewer5.Experts)