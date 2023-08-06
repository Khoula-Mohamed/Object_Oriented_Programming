from obj import Person

class teacher(Person):
    def __init__(self,tname, tage, experince):
         super().__init__(tname,tage)
         self.experince = experince
         
    def say_hi(self):
        print(super().say_hi())
        return f"{self.name} is a teacher"