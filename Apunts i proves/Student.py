from Person import  *

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)