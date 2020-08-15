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
from artist_similarity import artist_similarity
import numpy
import sklearn
from sklearn.metrics import mean_squared_error
from foreigntracks import findforeigntracks, findForeignArtists, findArtist

client_id = '85725aa023e545729e6630b2a369cf90'
client_secret = '1abf0e31be774f2d9fb434adb538ae87'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# songlist is user-submitted songlist, country is user-chosen country. 
def algorithm(songlist, country):
    foreignsongids = []
    for song in songlist:
        initialsimratios = []
        highratartistindices = []
        highratartists = []
        songartist = findArtist(song)
        foreignartists = findForeignArtists(country) #a list of artist URIs from chosen country. 
        for foreignartist in foreignartists:
            simratio = artist_similarity(songartist, foreignartist)
            initialsimratios.append(simratio)
        index = 0
        for ratio in initialsimratios:
            if ratio >= 0.6:
                highratartistindices.append(index)
            index = index + 1
        for index in highratartistindices:
            highratartists.append(foreignartists[index])
        #at this point you have highratartists—the artists that have high sim
        #ratio with song artist. begin phase 2. 
        for artist in highratartists:
            someforeignids = artistmatchingsongs(song, artist)
            for id in someforeignids:
                foreignsongids.append(id)
    return foreignsongids            

#One More Year, Fake Plastic Trees, Desperado, Woods
testsonglist = ['5ozqshq2dtU7SYCpCBu0NE', '045sp2JToyTaaKyXkGejPy', '4mCf3vQf7z0Yseo0RxAi3V', '3Qa944OTMZkg8DHjET8JQv']   

print(algorithm(testsonglist, 'Pakistan'))