import datetime

class Student:
    def __init__(self, id, last_name, name, middle_name, year, address, t_number, faculty, course, group):
        self.id = id
        self.last_name = last_name
        self.name = name
        self.middle_name = middle_name
        self.year = year
        self.address = address
        self.t_number = t_number
        self.faculty = faculty
        self.course = course
        self.group = group

    def get_year(self):
        return datetime.date.today().year - self.year

    def get_faculty(self):
        return self.faculty

    def get_group(self):
        return self.group

    def __str__(self):
        return self.last_name + " " + self.name + " " + self.middle_name + " " + str(self.get_year()) + " " + self.address + " " + str(self.t_number)

spisok = [
Student(1, "Grey", "Garry", "Igorevich", 1988, "Minsk", 80292222221, "History", 1, 2),
Student(2, "Green", "Larry", "Leonidovich", 1998, "Gomel", 80292222222, "History", 1, 2),
Student(3, "Black", "Barry", "Vich", 1991, "Minsk", 80292222224, "History", 1, 3),
Student(4, "White", "Sasha", "Igorevich", 1996, "Rome", 80292222225, "Math", 1, 4),
Student(5, "Red", "Dasha", "Igorevna", 1993, "Riga", 80292222226, "Chemistry", 2, 1),
Student(6, "Braun", "Masha", "Igorevna", 1988, "Miami", 80292222227, "Chemistry", 2, 2),
Student(7, "Blue", "Pasha", "Viktorovich", 1990, "Tokio", 80292222228, "Math", 2, 3),

]


v = input("Write faculty: Math, History or Chemistry")
for Student in spisok:
    if Student.get_faculty() == v:
        print(Student)


v2 = int(input("Write group from 1 to 4"))
for Student in spisok:
    if Student.get_group() == v2:
       print("GROP # " + str(v2) + str(Student))











