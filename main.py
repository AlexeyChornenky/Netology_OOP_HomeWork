class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_rate = 0

    def rate_lection(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum_grade = 0
        length = 0
        for key in lector.grades.keys():
            for grad in lector.grades[key]:
                sum_grade += grad
                length += 1
        lector.avg_rate = round(sum_grade / length, 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_rate}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Так сравнивать некорректно!')
            return
        return self.avg_rate < other.avg_rate


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_rate = 0

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Так сравнивать некорректно!')
            return
        return self.avg_rate < other.avg_rate


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum_grade = 0
        lenght = 0
        for key in student.grades.keys():
            for grade in student.grades[key]:
                sum_grade += grade
                lenght += 1
        student.avg_rate = round(sum_grade / lenght, 1)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def average_rate_hw(list_students, course):
    grades_summary = []
    for student in list_students:
        for grade in student.grades[course]:
            grades_summary.append(grade)
    if len(grades_summary) > 0:
        return sum(grades_summary) / len(grades_summary)
    else:
        return 'Нет оценок'


def average_rate_lections(list_lectors, course):
    grades_summary = []
    for lector in list_lectors:
        for grade in lector.grades[course]:
            grades_summary.append(grade)
    if len(grades_summary) > 0:
        return sum(grades_summary) / len(grades_summary)
    else:
        return 'Нет оценок'


# Создание экземпляров
student1 = Student('Петя', 'Кнопкин', 'муж')
student1.courses_in_progress += ['Python', 'SQL']
student1.finished_courses += ['GIT']

student2 = Student('Соня', 'Табуреткина', 'жен')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['GIT']

lector1 = Lecturer('Надежда', 'Лекционная')
lector1.courses_attached += ['Python', 'SQL']

lector2 = Lecturer('Екатерина', 'Лекторная')
lector2.courses_attached += ['GIT', 'Python']

reviewer1 = Reviewer('Анатолий', 'Проверяльщиков')
reviewer1.courses_attached += ['Python', 'GIT']

reviewer2 = Reviewer('Николай', 'Оценщиков')
reviewer2.courses_attached += ['Python', 'SQL']


# Вызов методов
student1.rate_lection(lector1, 'Python', 8)
student1.rate_lection(lector1, 'SQL', 9)
student1.rate_lection(lector2, 'Python', 10)
student1.rate_lection(lector2, 'Python', 7)

student2.rate_lection(lector2, 'GIT', 8)
student2.rate_lection(lector1, 'Python', 10)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student1, 'SQL', 7)

reviewer2.rate_hw(student1, 'SQL', 8)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 6)


print(student1, '\n')
print(student2, '\n')
print(lector1, '\n')
print(lector2, '\n')
print(reviewer1, '\n')
print(reviewer2, '\n')
print(f"Средняя оценка за домашнюю работу у Сони больше, чем у Пети: {student2 > student1}\n")
print(f"Средняя оценка за лекции у Надежды больше, чем у Екатерины: {lector1 > lector2}\n")
print(f"Средняя оценка студентов за курс Python: {average_rate_hw([student1, student2], 'Python')}\n")
print(f"Средняя оценка лекторов за курс Python: {average_rate_hw([lector1, lector2], 'Python')}")