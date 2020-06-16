from TuringTest_helper import *

'''
Do not modify the following code!!! Doing so will make life a lot harder
'''

districts=[District("Seattle, WA"), District("New York City, NY"), District("Los Angeles, CA"), District("Chicago, IL"), District("Miami, FL"), District("Portland, OR"), District("Washington D.C."), District("Austin, TX")]
questions=["How long have you been working here?","What subject(s) do you teach?","What kind of housing do you live in?","What's your highest educational degree?"]

'''
Your answer begins here
'''

'''
#SAMPLE ANSWER TO BE DELETED BEFORE PROVIDING CODE TO STUDENTS
budgets=[]
for i in range(0, len(districts)):
	district=districts[i]
	total=0
	guesses=[]
	for teacher in district.teachers:
		print(teacher.getFirstName(), teacher.getLastName())
		for question in questions:
			print(question)
			print(teacher.ask(question))
		guess=''
		while guess not in ["H","R"]:
			print("Do you think this teacher is a human (H) or a robot (R)? ", end=" ")
			guess=random.choice(["H","R"])
			print(guess)
			if guess not in ["H","R"]:
				print("Sorry, I didn't get that. Please enter your guess again")
			else:
				guesses.append(guess)
		print()
	for guess in guesses:
		if guess=="R":
			total+=15000
		else:
			total+=25000
	budgets.append(total)

for i in range(0,len(districts)):
	district=districts[i]
	print(district)
	if budgets[i]==district.budget:
		print("We have enough money to pay everyone a fair wage in {}!".format(district.name))
	elif budgets[i]>district.budget:
		print("We do not have the funds for the {} district budget. We will have a debt of ${},000".format(district.name, (budgets[i]-district.budget)//1000))
	else:
		print("The {} district will be underfunded by ${},000 next year".format(district.name, (district.budget-budgets[i])//1000))
	print()
'''



