class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avr_grade(self):
        self.grade_avr = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.grade_avr

    def __str__(self):
        res = f'Имя: {self.name}' \
              f'\n Фамилия: {self.surname}' \
              f'\n Средняя оценка за домашние задания: {self.avr_grade()}' \
              f'\n Курсы в процессе изучения: {",".join(self.courses_in_progress)}' \
              f'\n Завершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не является студентом!")
            return
        return self.avr_grade() < other.avr_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def avr_grade(self):
        self.grade_avr = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.grade_avr

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.avr_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не является лектором!")
            return
        return self.avr_grade() < other.avr_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res


kevin = Student('Kevin', 'Little', 'male')
kevin.finished_courses += ['Java', 'English for Programmers']
kevin.courses_in_progress += ['GIT', 'Python', 'Introduction to Programming']

stuart = Student('Stuart', 'Bing', 'male')
stuart.finished_courses += ['Introduction to Programming']
stuart.courses_in_progress += ['GIT', 'Python', 'English for Programmers']

bob = Reviewer('Bob', 'Smith')
bob.courses_attached += ['GIT', 'English for Programmers']

tim = Reviewer('Tim', 'Black')
tim.courses_attached += ['Introduction to Programming', 'Python']

dave = Lecturer('Dave', 'Gellar')
dave.courses_attached += ['Python', 'English for Programmers', 'GIT']

jerry = Lecturer('Jerry', 'Mister')
jerry.courses_attached += ['GIT', 'Introduction to Programming']

bob.rate_hw(kevin, 'GIT', 10)
bob.rate_hw(stuart, 'English for Programmers', 9)
tim.rate_hw(kevin, 'Python', 7)
tim.rate_hw(stuart, 'Python', 6)

kevin.avr_grade()
stuart.avr_grade()
print(kevin < stuart)
print(kevin)
print(stuart)

kevin.rate_lecturer(dave, 'GIT', 8)
kevin.rate_lecturer(jerry, 'GIT', 9)
stuart.rate_lecturer(dave, 'Python', 10)
stuart.rate_lecturer(jerry, 'GIT', 7)

dave.avr_grade()
jerry.avr_grade()
print(dave < jerry)
print(dave)
print(jerry)

student_list = [kevin, stuart]


def course_avr_grade1(student_list, course):
    sum_ = 0
    count = 0
    for student in student_list:
        for i in student.grades[course]:
            sum_ += i
            count += 1
    return round(sum_ / count, 1)


print(course_avr_grade1(student_list, 'Python'))

lecturer_list = [dave, jerry]


def course_avr_grade2(lecturer_list, course):
    sum_ = 0
    count = 0
    for lecturer in lecturer_list:
        for i in lecturer.grades[course]:
            sum_ += i
            count += 1
    return round(sum_ / count, 1)


print(course_avr_grade2(lecturer_list, 'GIT'))