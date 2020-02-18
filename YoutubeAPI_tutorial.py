from apiclient.discovery import build


api_key = "AIzaSyCJOu3dpuyJPDX3GavmoefFTk20PSbZYfI"


youtube = build('youtube', 'v3', developerKey = api_key)


print(type(youtube))

req = youtube.search().list(q = 'Billy Eilish', part = 'snippet', type = 'video') #q = query, part = parts are objects that contain nested properties of videos, just to limit bandwith use
#note that for searches, part must 'id', 'snippet', or 'id, snippet'. 
print(type(req))

res = req.execute()

#print(res) #JSON format for result of search from Youtube API
#print(res['items'])
#print(len(res['items'])) #this shows that you max the maximum number of results you're pulling is 5 


#req = youtube.search().list(q = 'Billy Eilish', part = 'snippet', type = 'video', maxResults = 10) #to get the top 10 results

# to view all video titles in results
for item in res['items']:
	print(item['snippet']['title'])


channelId = 'UCr2dD3s19bdcw4qjuUTQKiQ'

contentdata = youtube.channels().list(id = channelId, part = 'contentDetails').execute() #contentDetails only applicable for IDs
playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
videos = [ ]
next_page_token = None

print(contentdata)