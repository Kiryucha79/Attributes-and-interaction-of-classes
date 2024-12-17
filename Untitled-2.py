class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __add__(self, student):
        self.grades == student.grades

    def __str__(self):
        return f"имя: {self.name} + фамилия: {self.surname} + курсы: {self.finished_courses} + оценка: {self.grades}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_attached = []

    def __str__(self):
        return f"имя: {self.name} + фамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = []

    def __str__(self):
        return f"имя: {self.name} + фамилия: {self.surname} + курсы: {self.courses_attached} + оценка: {self.grades}"

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, lecturer) and course in self.finished_courses and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Git']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_in_progress += ['Python']
cool_lecturer.finished_courses += ['Git']
cool_lecturer.grades1 = ['9']
cool_lecturer.grades2 = ['10']

print(best_student1.name, best_student1.surname, best_student1.courses_in_progress, best_student1.finished_courses)
print()

print(cool_lecturer.name, cool_lecturer.surname, cool_lecturer.finished_courses + cool_lecturer.grades2)
print(cool_lecturer.name, cool_lecturer.surname, cool_lecturer.courses_in_progress + cool_lecturer.grades1)
print()

# Задание №3

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.finished_courses += ['Git']
student1.courses_in_progress += ['Python']
student1.grades['Git'] = [7,9,10,8]
student1.grades['Python'] = [9,5,7,9]

# далее выполняем конкатенацию - объединение строк
full_name = student1.name + " " + student1.surname
message1 = full_name, student1.finished_courses, student1.grades['Git']
message2 = full_name, student1.courses_in_progress, student1.grades['Python']
# выводим на печать
print(message1)
print(message2)
print()

student2 = Student('Pol', 'Anderson', 'your_gender')
student2.finished_courses += ['Git']
student2.courses_in_progress += ['Python']
student2.grades['Git'] = [9,9,10,8]
student2.grades['Python'] = [8,4,7,6]

full_name2 = student2.name + " " + student2.surname
message3 = full_name2, student2.finished_courses, student2.grades['Git']
message4 = full_name2, student2.courses_in_progress, student2.grades['Python']
# выводим на печать
print(message3)
print(message4)
print()

# выводим данные лектора
lecturer1 = Lecturer('Aleksandr', 'Popov')
lecturer1.courses_attached += ['Git']
lecturer1.grades3 = [6,4,5,7]

lecturer2 = Lecturer('Lev', 'Tolstoi')
lecturer2.courses_in_progress += ['Python']
lecturer2.grades4 = [4,2,8,9]

full_name3 = lecturer1.name + " " + lecturer1.surname
full_name4 = lecturer2.name + " " + lecturer2.surname
message5 = full_name3, lecturer1.courses_attached, lecturer1.grades3
message6 = full_name4, lecturer2.courses_in_progress, lecturer2.grades4
print(message5)
print(message6)
print()

# выводим средний балл студентам по курсам Gir и Python:
average1 = sum(student1.grades['Git']) / len(student1.grades['Git'])
print(average1)
average2 = sum(student1.grades['Python']) / len(student1.grades['Python'])
print(average2)
# Средний бал за домашние задания:
average_score1 = sum(student1.grades['Git'] + student1.grades['Python']) / len(student1.grades['Git'] + student1.grades['Python'])
print(average_score1)

average3 = sum(student2.grades['Git']) / len(student2.grades['Git'])
print(average3)
average4 = sum(student2.grades['Python']) / len(student2.grades['Python'])
print(average4)
average_score2 = sum(student2.grades['Git'] + student2.grades['Python']) / len(student2.grades['Git'] + student2.grades['Python'])
print(average_score2)
print()

# сравниваем средний бал
print(student1.grades['Git'] < student2.grades['Git'])
print(student1.grades['Git'] == student2.grades['Git'])
print()

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

student1 = Student('Ruoy', 'Eman')
print(student1)
student2 = Student('Pol', 'Anderson')
print(student2)

class Student:
    def __init__(self, grades):
        self.grades = grades

    def __str__(self):
        return (f'Средняя оценка за домашние задания: Git {average1}, Python {average2}')


student = Student('10')
print(student)


class Student:
    def __init__(self, courses_in_progress):
        self.courses_in_progress = courses_in_progress

    def __str__(self):
        return f'Курсы в процессе изучения: {self.courses_in_progress}'


student = Student('Python, Git')
print(student)

class Student:
    def __init__(self, finished_courses):
        self.finished_courses = finished_courses

    def __str__(self):
        return f'Завершенные курсы: {self.finished_courses}'


student = Student('Введение в программирование')
print(student)