#for the artist of a given user-submitted song, find the similarity ratio for a foreign
#artist whose song is on the foreign playlist. 
#WORKS 3.8
from spotipy.oauth2 import SpotifyClientCredentials
from collections import Counter
import math
import json
import spotipy
import time
import sys
import cossim
import numpy
import sklearn
from sklearn.metrics import mean_squared_error


def find_artist(songartist, foreignartist):
    songartistgenres = []
    foreignartistgenres = []
    indsongartgenres = []
    indforartgenres = []
    client_id = '85725aa023e545729e6630b2a369cf90'
    client_secret = '1abf0e31be774f2d9fb434adb538ae87'
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    relatedartistdata = sp.artist_related_artists(songartist)
    relatedartnames = relatedartistdata['artists']
    for i in range(0, len(relatedartnames)):
        songartistgenres.append(relatedartnames[i]['genres'])
    forartistdata = sp.artist_related_artists(foreignartist)
    forartnames = forartistdata['artists']
    for i in range(0, len(forartnames)):
        foreignartistgenres.append(forartnames[i]['genres'])
    for genre in songartistgenres:
        for subgenre in genre:
            if subgenre not in indsongartgenres:
                indsongartgenres.append(subgenre)
    for genre in foreignartistgenres:
        for subgenre in genre:
            if subgenre not in indforartgenres:
                indforartgenres.append(subgenre)
    singlewordartgenres = [word for line in indsongartgenres for word in line.split()]                         
    singlewordforartgenres = [word for line in indforartgenres for word in line.split()]
    counterA = Counter(singlewordartgenres)
    counterB = Counter(singlewordforartgenres)

    similarityratio = cossim.counter_cosine_similarity(counterA, counterB) * 100
    #print(similarityratio)
    return similarityratio

#below: potential test case
#find_artist('5INjqkS1o8h1imAzPqGZBb', '6nyfDdTwCLGrbCFikT8PTK')