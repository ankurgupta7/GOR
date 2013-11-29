
class User:
		users=0
	def __init__(self):
		self.userId=User.users+1
		self.curPriority=4 ## default value given in the question
		self.curQuesNoInCurrentPriority=0 # the above two variables uniquesly identify the ques user is currently doing
		self.priorityChangeFlag=0 #when this flag reaches +-2 , currentPriority level will change for this user.
		self.marks=0 #so that marks are calculated and stored on the fly  and list of questions attemped need be maintained
		self.curQuesInEachPriorityLevel=[-1]*Server.noOfPriorityLevels  # an array, which is used to decide which question is to be served to the user.
																# questions are served serially in one priority, so this array saves for each priority level,
																#what was the last ques user attempted from that priority. (array[priority]+1) will be served from questions[priority]
		User.users+=1

class _question_:
	def __init__(self,problemStatement,options):
		self.problemStatement=problemStatement
		self.options=options
class Question:
	questions=0
	def __init__(self,prior,ans,problemStatement,options):
		self.quesId=Question.questions + 1
		Question.questions += 1
		self.priority=prior
		self.answer=ans
		self.question=_question_(problemStatement,options)

class Server:
	noOfPriorityLevels=10
	DynamicQuestionTable=[[]]*noOfPriorityLevels ## storing questions in a dynamically expanding questions base. a list of questions provided by 
											##  the institute can be easily represented in this fashion.
	usersList=[] ##storing users in a dynamically expanding userList. eaach time a user comes in, he ll inititaed and added to this list

	def __init__(qList,n):
		addQuestionsToTable(qList)
		addUsers(n)
	def addQuestionsToTable(qList): ## to dynamically add questions in the system
		for q in qList:
			q=q.split('~')
			addQuestionToTable(q[0],q[1],q[2],q[3])
	def addQuestionToTable(prior,ans,problemStatement,options):
		q=Question(prior,ans,problemStatement,options)
		Server.DynamicQuestionTable[prior].append(q)
	def addUsers(n): #to dyanamically add n no of users in the system
		for i in range(n):
			Server.userList[i]=User()
	def giveQuesToUser(userId): ## method is called when user demands for next question
		user=userList[userId]
		priority=user.curPriority
		nextQuesIndex=user.curQuesInEachPriorityLevel[priority] + 1 ## assuming there are always sufficient number of  questions in each priority level.
		nextQues=DynamicQuestionTable[priority][nextQuesIndex]
		user.curQuesInEachPriorityLevel[priority] += 1
		user.curQuesNoInCurrentPriority=nextQuesIndex
		print(userid,'Got question', nextQues.question.problemStatement)
		print(nextQues.question.options)
		return [priority,nextQuesIndex,userId]
	def getAnswerFromUser(qPriority,qIndex,userId,ansByUser): ##method is called when user submits an answer
		rightAnswerFlag=getAnswerForQues(qPriority,qIndex,ansByUser)
		updateMarksForUser(userId,rightAnswerFlag,qPriority)
		updatePriorityAndFlagForUser(userId, rightAnswerFlag)

	def getAnswerForQues(qPriority,qIndex,ansByUser):
		correctAns=DynamicQuestionTable[qPriority][qIndex].answer
		if( correctAns==ansByUser):
			return 1
		else:
			return 0
	def updateMarksForUser(userId,rightAnswerFlag,qPriority):
		user=userList[userId]
		if(rightAnswerFlag==1):
			user.marks+=qPriority
	def updatePriorityAndFlagForUser(userId, rightAnswerFlag):
		user=userList[userId]	
		user.priorityChangeFlag+=rightAnswerFlag
		if(user.priorityChangeFlag == 2 || user.priorityChangeFlag ==-2):
			user.curPriority+=int((user.priorityChangeFlag)/2)
			user.priorityChangeFlag=0


# DynamicQuestionTable=[[]]*noOfPriorityLevels ## storing questions in a dynamically expanding questions base. a list of questions provided by 
# 											##  the institute can be easily represented in this fashion.
# usersList=[] ##storing users in a dynamically expanding userList. eaach time a user comes in, he ll inititaed and addede to this list
if __name__=='__main__':

	server=Server(qList,10)
	[qPriority,qIndex,userId]=server.giveQuesToUser(1)
	ansByUser=input('Type the answer to this question: ')

	server.getAnswerFromUser(qPriority,qIndex,userId,ansByUser)