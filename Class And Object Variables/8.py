class Person:

      def __init__(self, name, age):
          self.name = name
          self.age = age

class Student(Person):
      """A derived class for Student"""
      def __init__(self, name, age, school):
          Person.__init__(self, name, age)
          self.school = school
          
      def introduce(self):
      	  #Student.introduce(self)	
          return "My name is %s. I am %d years old. I am studying at %s." % (self.name,self.age,self.school)

class WorkingAdult(Person):
      """A derived class for WorkingAdult"""
      def __init__(self, name, age, job):
      	   Person.__init__(self, name, age)
      	   self.job = job	

      def introduce(self):
      	   return "My name is %s. I am %d years old. I am a %s." % (self.name,self.age,self.job.lower())	