import google_auth_oauthlib.flow
import googleapiclient.discovery
from apiclient.discovery import build


#from secrets import spotify_token, spotify_user_id
secret = 'client_secret.json'


'''
Terminal based Youtube -> Spotify 
On terminal, extract youtube video you like, and this will download the equivalent Spotify videos. 
-Features: can go on account and also extract liked videos
-Features: can go on playlist and convert playlist to a Spotify playlist
'''


class CreatePlayList: 

	def __init__(self):
		api_key = "key"
		#youtube = build('youtube', 'v3', developerKey = api_key)

		self.youtuber = build('youtube', 'v3', developerKey = api_key)
		self.songs = [] #store info into a list 


	def query(self, searchTerm):#, start_time, end_time):
		#start_time = datetime(year = 2005, month = 1, day = 1).strftime("%Y-%m-%dT%H:%M:%SZ") #whitespace sensitive
		#end_time = datetime(year = 2006, month = 1, day = 1).strftime("%Y-%m-%dT%H:%M:%SZ")
		res = self.youtuber.search().list(part = 'snippet', q = searchTerm, type = 'video', maxResults = 10).execute()#, publishedAfter = start_time, publishedBefore = end_time).execute() 
		#print(res)
		return res 

	def extractTitle(self, resource):
		for item in resource['items']:
			for x in item['snippet']['title']:
				self.songs.append(x)

			#print(item['snippet']['title'])


if __name__ == '__main__':
	cp = CreatePlayList()
	#	print(cp.__dict__) # to view the attributes in dictionary format and the type of variables they're storing

	resources = cp.query('Dancing Queen')

	cp.extractTitle(resources)
	print(cp.__dict__) 






