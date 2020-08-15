#For a given country, finds top playlists on Spotify with music from that country,
#and pulls however many songs desired from these playlists. Number of playlists, 
#songs on playlists can be modified by changing 'limit' 
#parameter. (also, 'Pakistan' is starter case. can append more) 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '85725aa023e545729e6630b2a369cf90'
client_secret = '1abf0e31be774f2d9fb434adb538ae87'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))



foreigntracks = []
foreignartists = []
playliststochoosefrom = []
country = ''
name = ''
track = ''

def findforeigntracks(country):
    rawresults = sp.search(q=country + ' Music', type='playlist', limit=3)
    playlisturls = rawresults['playlists']['items']

    for i in range(0, len(playlisturls)):
        playliststochoosefrom.append(playlisturls[i]['id'])

    for playlist in playliststochoosefrom:
        tracksfromplaylist = sp.playlist_tracks(playlist, limit=3)
        for i in range(0, len(playliststochoosefrom)):
            foreigntracks.append(tracksfromplaylist['items'][i]['track']['id'])


    return foreigntracks

#findforeigntracks('Pakistan')

def findForeignArtists(country):
    rawresults = sp.search(q=country + ' Music', type='playlist', limit=8)
    playlisturls = rawresults['playlists']['items']

    for i in range(0, len(playlisturls)):
        playliststochoosefrom.append(playlisturls[i]['id'])

    for playlist in playliststochoosefrom:
        tracksfromplaylist = sp.playlist_tracks(playlist, limit=5) #get limit number of tracks from playlist. 
        tracksnarroweddown = tracksfromplaylist['items']
        for i in range(0, len(tracksnarroweddown)):
            foreignartists.append(tracksnarroweddown[i]['track']['artists'][0]['id'])
    return foreignartists

#returns artist Spotify URI given track URI
def findArtist(track):
    result = sp.track(track)
    modifiedresult = result['album']['artists'][0]['external_urls']['spotify']
    return modifiedresult


def getAlbums(name):
    result = sp.search(q='artist:' + name)  # search query
    result['tracks']['items'][0]['artists']
    artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
    sp_albums = sp.artist_albums(artist_uri, album_type='album')
    album_names = []
    album_uris = []
    for i in range(len(sp_albums['items'])):
        album_names.append(sp_albums['items'][i]['name'])
        album_uris.append(sp_albums['items'][i]['uri'])
    print(album_uris)
    print(album_names)

#print(findForeignArtists('Pakistan'))