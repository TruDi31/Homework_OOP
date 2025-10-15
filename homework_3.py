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


if __name__ == "__main__":
    student1 = Student('Ruoy', 'Eman', 'M')
    student1.courses_in_progress = ['Python', 'Git']
    student1.finished_courses = ['Введение в программирование']
    student1.grades = {'Python': [9, 10, 10], 'Git': [10, 9]}

    student2 = Student('Anna', 'Smith', 'F')
    student2.courses_in_progress = ['Python']
    student2.grades = {'Python': [8, 9, 8]}

    lecturer1 = Lecturer('Some', 'Buddy')
    lecturer1.grades = {'Python': [9, 10, 9.9]}

    lecturer2 = Lecturer('John', 'Doe')
    lecturer2.grades = {'Python': [8, 9]}

    reviewer = Reviewer('Peter', 'Parker')

    print("Reviewer")
    print(reviewer)
    print("\nLecturer")
    print(lecturer1)
    print("\nStudent")
    print(student1)

    # сравнение
    print("\nСравнение студентов")
    print(f"student1 > student2: {student1 > student2}")
    print(f"student1 < student2: {student1 < student2}")
    print(f"student1 == student2: {student1 == student2}")

    print("\nСравнение лекторов")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")