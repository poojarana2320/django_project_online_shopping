class Person():
	def __init__(self,name):
		self.name=name
	@classmethod
	def class_method(cls,name):
		print name
	@staticmethod
	def static_method(age):
		print age
person1 = Person("Pooja")
print person1.name
Person.class_method("shiv")
Person.static_method(23)
