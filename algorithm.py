"""
Generates the list of recommended songs from foreign country artist given
list of favorite songs provided by user.
"""
from spotipy.oauth2 import SpotifyClientCredentials
from collections import Counter
import math
import json
import spotipy
import time
import sys
import numpy
import sklearn
from sklearn.metrics import mean_squared_error

#for the artist of a given user-submitted song, find the similarity ratio for a foreign
#artist whose song is on the foreign playlist. 
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
    similarityratio = counter_cosine_similarity(counterA, counterB) * 100
    return similarityratio

#helper function for find_artist (calculates similarity of genre lists)
def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

#given a song, and a foreign artist similar to the artist of that song 
#(determined by find_artist), find the songs from that foreign artist that
#are most similar to the song using MSE. 
def artistmatchingsongs(songid, artist):
    client_id = '85725aa023e545729e6630b2a369cf90'
    client_secret = '1abf0e31be774f2d9fb434adb538ae87'
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False
    frgnarttracksids = [] #list of ids of 20 songs of foreign artist. 
    frgnarttrackvectors = []
    topforsongs = sp.search(q=artist, limit=20, type='track')
    tpforsngtrackinfo = topforsongs['tracks']
    infonarroweddown = tpforsngtrackinfo['items']
    for i in range(0, len(infonarroweddown)):
        individualsong = infonarroweddown[i]
        indsongid = individualsong['id']
        frgnarttracksids.append(indsongid)    
    foreignsongdata = sp.audio_features(frgnarttracksids)
    for track in foreignsongdata:
        ftrlisttobevector = []
        for feature in track:
            if feature == 'type':
                break
            ftrlisttobevector.append(track[feature])
        songvector = numpy.array(ftrlisttobevector)
        frgnarttrackvectors.append(songvector)
    songaudioftrs = sp.audio_features(songid)
    usrsongvector = []
    for feature in songaudioftrs:
        ftrlisttobevector = []
        for feature in track:
            if feature == 'type':
                break
            ftrlisttobevector.append(track[feature])
    usrsongvector = numpy.array(ftrlisttobevector)
    #now we compare usrsongvector to frgn artist songs' vectors w/ MSE calculation. 
    #want MSEs that are the lowest. 
    lowmseindices = []
    for vector in frgnarttrackvectors:
        mse = mean_squared_error(usrsongvector, vector)
        if mse < 0.4:
            lowmseindices.append(frgnarttrackvectors.index(vector))
    songidstoreturn = []
    for index in lowmseindices:
        songidstoreturn.append(frgnarttracksids[index])
    return songidstoreturn

    
