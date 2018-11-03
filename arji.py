import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print (("Usage: %s username" % (sys.argv[0],)))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track(['name'] + ' - ' + track['artists'][0]['name']))
else:
    print (("Can't get token for", username))


print("hello world")


#import spotipy
#import spotipy.util as util
#util.prompt_for_user_token('crv8ki2aw6xt74djc35cg8o7q','user-library-read',client_id='97ef4ffd06bd471897a4e35d9bf7f48f',client_secret='11832f659f1f4389af7722394c041527',redirect_uri='https://www.google.com/')
#print("hello world")
import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)