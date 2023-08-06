from obj import Person
from studentclass import Student
from teacher import teacher
def main():
    k = Person("Khoula",24)
    p2 = Person("Hamza")
    stud1 = Student("Nidhal",20,2021)
    stud2 = Student("Ahmed",21,2023)
    print(stud1.say_hi())
    print(Student.say_hi(stud2))
    print(stud1.run())
    
    t1 = teacher("Amal",30,16)
    print(t1.say_hi())
    print(t1.run())

    print(p2.descrip())
    print(k.get_name())
    k.set_name("Khoula Mohammed")
    print(k.get_name())
    print(k.descrip())
    k.run()
    print(k.say_hi())
    
    
main()