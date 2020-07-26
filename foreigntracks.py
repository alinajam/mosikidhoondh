#For a given country, finds top playlists on Spotify with music from that country,
#and pulls however many songs desired from these playlists. Number of playlists, 
#songs on playlists can be modified by changing 'limit' 
#parameter. (also, 'Pakistan' is starter case. can append more) 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

foreigntracks = []
playliststochoosefrom = [] 
client_id = '85725aa023e545729e6630b2a369cf90'
client_secret = '1abf0e31be774f2d9fb434adb538ae87'
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
rawresults = spotify.search(q='playlist:Pakistan', type='playlist', limit=2)
playlisturls = rawresults['playlists']['items']
for i in range(0, len(playlisturls)):
    playliststochoosefrom.append(playlisturls[i]['id'])
for playlist in playliststochoosefrom:
    tracksfromplaylist = spotify.playlist_tracks(playlist, limit=3)
    for i in range(0, len(playliststochoosefrom)):
        foreigntracks.append(tracksfromplaylist['items'][i]['track']['id'])
print(foreigntracks)

