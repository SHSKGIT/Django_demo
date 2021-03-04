import threading
import mailchimp3
from django.conf import settings

class SendSubscribeMailAgent(object):
	def __init__(self, email):
		self.email = email
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True                     
		thread.start()                                 

	def run(self):
		API_KEY = settings.MAILCHIMP_API_KEY
		LIST_ID = settings.MAILCHIMP_SUBSCRIBE_LIST_ID_R
		client = mailchimp3.MailChimp(mc_api=API_KEY, mc_user=settings.MAILCHIMP_USERNAME)
		try:
			client.lists.members.create(LIST_ID, {
                'email_address': self.email.email,
                'status': 'subscribed',
                'merge_fields': {
                    'FNAME': self.email.first_name,
                    'LNAME': self.email.last_name,
                },
            })
		except:
			return False


class SendSubscribeMailUser(object):
	def __init__(self, email):
		self.email = email
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True                     
		thread.start()                                 

	def run(self):
		API_KEY = settings.MAILCHIMP_API_KEY
		LIST_ID = settings.MAILCHIMP_SUBSCRIBE_LIST_ID_U
		client = mailchimp3.MailChimp(mc_api=API_KEY, mc_user=settings.MAILCHIMP_USERNAME)
		try:
			client.lists.members.create(LIST_ID, {
                'email_address': self.email.email,
                'status': 'subscribed',
                'merge_fields': {
                    'FNAME': self.email.first_name,
                    'LNAME': self.email.last_name,
                },
            })
		except:
			return False