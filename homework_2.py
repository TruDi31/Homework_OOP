class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        if self.grades:
            total_grades = sum(sum(grades) for grades in self.grades.values())
            total_count = sum(len(grades) for grades in self.grades.values())
            return total_grades / total_count if total_count > 0 else 0
        return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        if self.grades:
            total_grades = sum(sum(grades) for grades in self.grades.values())
            total_count = sum(len(grades) for grades in self.grades.values())
            return total_grades / total_count if total_count > 0 else 0
        return 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


if __name__ == "__main__":
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    student = Student('Алёхина', 'Ольга', 'Ж')

    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']

    print(student.rate_lecture(lecturer, 'Python', 7))   # None
    print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
    print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
    print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

    print(lecturer.grades)  # {'Python': [7]}