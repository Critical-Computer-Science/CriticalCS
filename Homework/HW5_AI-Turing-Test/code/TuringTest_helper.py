import random
import names

class Human:
	def __init__(self):
		self.name=names.get_full_name()
		self.responses={"How long have you been working here?":["Just started","Just over a year now","A couple of years","Long as I can remember"],"What subject(s) do you teach?":["Arts","Science","English and history","Music"],"What kind of housing do you live in?":["Shared apartment","Private apartment","Shared house","Private house"],"What's your highest educational degree?":["Bachelor's of Science","Master's of Education","Master's of Mathematics","PhD in Applied Sciences"]}

	def getFirstName(self):
		return self.name.split(' ')[0]

	def getLastName(self):
		return self.name.split(' ')[1]

	
	def ask(self, question):
		if question not in self.responses.keys():
			return "I'm sorry, I don't really know"
		return random.choice(self.responses[question])

	def __str__(self):
		return self.name+" (Human)"

class Robot:
	def __init__(self):
		self.name=names.get_full_name()
		self.responses={"How long have you been working here?":["Fresh off the factory line","Been here 1 year","2 years now","Long as I can remember"],"What subject(s) do you teach?":["Math","Science","English and history","Music"],"What kind of housing do you live in?":["Shared apartment","Private apartment","Shared house","Private house"],"What's your highest educational degree?":["Bachelor's of Science","Master's of Education","Master's of Mathematics","PhD in Applied Sciences"]}

	def getFirstName(self):
		return self.name.split(' ')[0]

	def getLastName(self):
		return self.name.split(' ')[1]

	def ask(self, question):
		if question not in self.responses.keys():
			return "I'm sorry, I don't really know"
		return random.choice(self.responses[question])

	def __str__(self):
		return self.name + " (Robot)"

class District:
	def __init__(self, name):
		self.name=name
		self.teachers=[]
		self.budget=0
		for i in range(10):
			choice=random.choice([0,1])
			if choice==0:
				self.teachers.append(Robot())
				self.budget+=15000
			else:
				self.teachers.append(Human())
				self.budget+=25000

	def __str__(self):
		retstring=""
		retstring+="Name: {}\n".format(self.name)
		retstring+="Teachers\n"
		for teacher in self.teachers:
			retstring+=str(teacher)+"\n"
		retstring+="Appropriate budget: ${},000".format(self.budget//1000)
		return retstring.strip()