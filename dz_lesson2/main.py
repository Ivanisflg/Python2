from colorama import Fore
from student import Student

student1 = Student(name="Vasya", birth_year=2010, team=0, ball=0,color=Fore.LIGHTGREEN_EX)
student2 = Student(name="Petya", birth_year=2013, team=1, ball=2,color=Fore.LIGHTCYAN_EX)

print(student1)
print(student2)
