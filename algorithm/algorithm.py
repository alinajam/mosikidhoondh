"""
Generates the list of recommended songs from foreign country artist given
list of favorite songs provided by user.
"""
from typing import Dict, Any

from spotipy.oauth2 import SpotifyClientCredentials
from collections import Counter
import math
import json
import spotipy
import time
import sys
from artist_matching_songs import artistmatchingsongs
from find_artist import find_artist
import numpy
import sklearn
from sklearn.metrics import mean_squared_error
from foreigntracks import findforeigntracks, findforeignartists


#so here we need to implement artist_matching_songs, find_artist together to generate
#similar songs (from Pakistani artists rn) for a given, chosen song by a Notemad user.
client_id = '85725aa023e545729e6630b2a369cf90'
client_secret = '1abf0e31be774f2d9fb434adb538ae87'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

foreigntracks = findforeigntracks('Pakistan')
foreignartists = findforeignartists('Pakistan')
simratios: Dict[foreignartists, find_artist]
print('enter artist')

artist = input()
searchbynameresult = sp.search(artist, type='artist')
artistitems = searchbynameresult['artists']['items']
artist = artistitems[0]
artist_uri = artist['uri']
trackresults = sp.artist_top_tracks(artist_uri)

print(trackresults)

for fa in foreignartists:
    simratio = find_artist(artist, fa)
    simratios[fa].append(simratio)

return simratios
