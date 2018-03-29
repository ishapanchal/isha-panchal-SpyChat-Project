from datetime import datetime
import spy_friend

class Spy:
	def __init__(self, name, salutation, age, rating):
		self.name = name
		self.salutation = salutation
		self.age = age
		self.rating = rating
		self.is_online = True
		self.chats = []
		self.current_status_message = None

spy = Spy('Mick', 'Mr.', 24, 5.0)


class ChatMessage:

	def __init__(self, message, sent_by_me):
		self.message = message
		self.time = datetime.now()
		self.sent_by_me = sent_by_me
