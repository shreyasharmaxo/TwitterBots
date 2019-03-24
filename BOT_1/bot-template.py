from secret import *
import tweepy
import nltk.chat as chat


auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)


#home = api.home_timeline()
usert = api.user_timeline()
#mentions = api.mentions_timeline()

#keep auth_user_id and replied tweet id
auth_user_id = api.me().id
replied = []

#make a chatbot
chatbot = chat.eliza.eliza_chatbot


def process_text(text):
	url = " https://t.co/"
	index = text.find(url)
	while index != -1:
		#remove url part
		text = text[:index] + text[index+24:]
		index = text.find(url)
	return text

#get all status_id (tweet_id) from reply history
def get_list_of_status_id_from_reply(status_id):
	id_list = []
	while status_id != None:
		id_list.append(status_id)
		tweet = api.get_status(status_id)
		status_id = tweet.in_reply_to_status_id
		
	return id_list

#check auth_user_id in reply history (will not check the tweet(status) of passed status_id)
def check_user_id_from_reply(status_id):
	while status_id != None:
		tweet = api.get_status(status_id)
		status_id = tweet.in_reply_to_status_id
		user_id = tweet.in_reply_to_user_id
		if user_id == auth_user_id:
			return True
		
	return False


def get_user_mentions_id(li):
	id_list = []
	for user in li:
		user_id = user['id']
		id_list.append(user_id)
	return id_list


for i in usert:
	#already replied
	if i.id in replied:
		continue


	#check @auth_user_id and reply 
	if i.entities['user_mentions'] != []:
		if auth_user_id in get_user_mentions_id(i.entities['user_mentions']):
			response = "tb: "
			response = response + chatbot.respond(process_text(i.text))
			api.update_status(response, in_reply_to_status_id = i.id)

	#not a reply, ignore
	if i.in_reply_to_status_id == None:
		continue

	if i.user.id == auth_user_id:
		#respond of user
		replied_status_id = get_list_of_status_id_from_reply(i.in_reply_to_status_id)
		replied = replied + replied_status_id
	else:
		#respond of others
		if i.in_reply_to_user_id == auth_user_id:
			#this is a reply to user's tweet
			response = "tb: "
			response = response + chatbot.respond(process_text(i.text))
			api.update_status(response, in_reply_to_status_id = i.id)

		elif check_user_id_from_reply(i.in_reply_to_status_id):
			#a reply to tweet that user in reply history
			response = "tb: "
			response = response + chatbot.respond(process_text(i.text))
			api.update_status(response, in_reply_to_status_id = i.id)



