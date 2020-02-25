import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl




from secrets import spotify_token, spotify_user_id

'''
Some notes on the Youtube API
-create project and get API key on Youtube API 

'''

class CreatePlayList: 
### Constructor

	def __init__(self):

## Pull youtube client and store information in a dictionary
		self.youtube_client = self.get_youtube_client()
		self.all_song_info = {}



	def get_youtube_client(self):
		pass

	def get_liked_videos(self):
		pass

	def get_spotify_uri(self, song_name, artist):
		pass

	def create_playlist(self):
		pass


	def add_song_to_playlist(self):
		pass


if __name__ == '__main__':
	cp = CreatePlayList()
	cp.add_song_to_Playlist(): 






