from apiclient.discovery import build
from datetime import datetime

# Import API key 
api_key = "key"
youtube = build('youtube', 'v3', developerKey = api_key)
print(type(youtube))

'''
#Lesson 1 - Basic search calling 

req = youtube.search().list(q = 'Billy Eilish', part = 'snippet', type = 'video') #q = query, part = parts are objects that contain nested properties of videos, just to limit bandwith use
#note that for searches, part must 'id', 'snippet', or 'id, snippet'. 
print(type(req))

res = req.execute()

print(res) #JSON format for result of search from Youtube API
print(res['items'])
print(len(res['items'])) #this shows that you max the maximum number of results you're pulling is 5 

#you can shorten the execute to 1 line

req = youtube.search().list(q = 'Billy Eilish', part = 'snippet', type = 'video', maxResults = 10).execute() #to get the top 10 results
print(req)

'''



'''
# Lesson 2 - to view all video titles in results
for item in res['items']:
	print(item['snippet']['title'])


channelId = 'UCr2dD3s19bdcw4qjuUTQKiQ'

contentdata = youtube.channels().list(id = channelId, part = 'contentDetails').execute() #contentDetails only applicable for IDs
playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
videos = [ ]
next_page_token = None

print(contentdata)
'''






'''
# Lesson 3 - to view videos in a certain range of time 

# YYYY-MM-DDThh:mm:ss.sZ format .. from documentation, example: 1970-01-01T00:00:00Z
start_time = datetime(year = 2005, month = 1, day = 1).strftime("%Y-%m-%dT%H:%M:%SZ") #whitespace sensitive
end_time = datetime(year = 2006, month = 1, day = 1).strftime("%Y-%m-%dT%H:%M:%SZ")

res = youtube.search().list(part = 'snippet', q = 'Billy Eilish', type = 'video', publishedAfter = start_time, publishedBefore = end_time).execute() 



print(res)


for item in sorted(res['items'], key = lambda x:x['snippet']['publishedAt']):
	print(item['snippet']['title'], item['snippet']['publishedAt'], item['id']['videoId']) #going into item -> id -> videoId

'''

# Lesson 4 - getting videos from channels

channelId = 'UCkUq-s6z57uJFUFBvZIVTyg'

res = youtube.channels().list(id = channelId, part = 'contentDetails').execute() #extract playlist id: UUkUq-s6z57uJFUFBvZIVTyg
playlistName = 'UUkUq-s6z57uJFUFBvZIVTyg' # alternatively you can: 'PLyb_C2HpOQSDlnrNJ_ERqTAkIe21xyRhi',  go into a playlist to extract this value
res2 = youtube.playlistItems().list(playlistId = playlistName, part = 'snippet').execute()

#print(res)
#print(res2)

def getChannelVideos(channelID):
	res = youtube.channels().list(id = channelID, part = 'contentDetails').execute()
	playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

	video = []
	next_page_token = None

	while 1: 
		res = youtube.playlistItems().list(playlistId = playlist_id, part = 'snippet', pageToken = next_page_token).execute()
		video += res['items']
		#next_page_token = res['nextPageToken'] #don't do this as sometimes you return nothing
		next_page_token = res.get('nextPageToken')

		if next_page_token is None: ##don't do if next_page_token == None
			break

	return video 

videos = getChannelVideos('UCkUq-s6z57uJFUFBvZIVTyg')
for video in videos:
	print(video['snippet']['title'])