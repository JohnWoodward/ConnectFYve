import os
import sys
import spotipy.util as util
import webbrowser
util.prompt_for_user_token(username,scope,client_id='97ef4ffd06bd471897a4e35d9bf7f48f',client_secret='11832f659f1f4389af7722394c041527',redirect_uri='https://www.google.com/')
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None




##############