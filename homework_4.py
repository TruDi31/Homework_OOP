class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def _calculate_avg_grade(self):
        all_grades = [
            grade
            for grades in self.grades.values()
            for grade in grades
        ]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        in_progress = ', '.join(self.courses_in_progress) or "нет курсов"
        finished = ', '.join(self.finished_courses) or "нет курсов"

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _calculate_avg_grade(self):
        all_grades = [
            grade
            for grades in self.grades.values()
            for grade in grades
        ]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calculate_avg_hw_grade(students, course):
    total_grade = 0
    total_count = 0

    for student in students:
        if course in student.grades:
            grades = student.grades[course]
            total_grade += sum(grades)
            total_count += len(grades)

    return total_grade / total_count if total_count > 0 else 0


def calculate_avg_lecture_grade(lecturers, course):
    total_grade = 0
    total_count = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            grades = lecturer.grades[course]
            total_grade += sum(grades)
            total_count += len(grades)

    return total_grade / total_count if total_count > 0 else 0


# Создание экземпляров
student1 = Student('Ruoy', 'Eman', 'M')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Anna', 'Smith', 'F')
student2.courses_in_progress = ['Python', 'Java']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached = ['Python', 'Git']

lecturer2 = Lecturer('John', 'Doe')
lecturer2.courses_attached = ['Python', 'Java']

reviewer1 = Reviewer('Peter', 'Parker')
reviewer1.courses_attached = ['Python', 'Git']

reviewer2 = Reviewer('Mary', 'Jane')
reviewer2.courses_attached = ['Java', 'Python']

# Вызов методов
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 8)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 8)

# Вывод информации
print("Проверяющие:")
print(reviewer1)
print()
print(reviewer2)
print()

print("Лекторы:")
print(lecturer1)
print()
print(lecturer2)
print()

print("Студенты:")
print(student1)
print()
print(student2)
print()

# Сравнение
print("Сравнение студентов:")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 < student2: {student1 < student2}")
print()

print("Сравнение лекторов:")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print()

# Использование функций
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

avg_hw_python = calculate_avg_hw_grade(students_list, 'Python')
avg_lecture_python = calculate_avg_lecture_grade(lecturers_list, 'Python')

print(f"Средняя оценка за домашние задания (Python): {avg_hw_python:.1f}")
print(f"Средняя оценка за лекции (Python): {avg_lecture_python:.1f}")