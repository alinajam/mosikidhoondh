#given a song, and a foreign artist similar to the artist of that song 
#(determined by find_artist), find the songs from that foreign artist that
#are most similar to the song using MSE. 
#WORKS 3.8
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

def artistmatchingsongs(songid, artist):
    client_id = '85725aa023e545729e6630b2a369cf90'
    client_secret = '1abf0e31be774f2d9fb434adb538ae87'
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False
    frgnarttracksids = [] #list of ids of 20 songs of foreign artist. 
    frgnarttrackvectors = []
    artistname = (sp.artist(artist))['name']
    topforsongs = sp.search(q=artistname, limit=3, type='track')
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
    #now we get features of the first user-submitted track.        
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
    vectorindex = 0
    for vector in frgnarttrackvectors:
        vectorindex = vectorindex + 1
        mse = mean_squared_error(usrsongvector, vector)
        isless = mse < 0.99
        if (isless == True):
            lowmseindices.append(vectorindex - 1)
    songidstoreturn = []
    for index in lowmseindices:
        songidstoreturn.append(frgnarttracksids[index])
    return songidstoreturn

artistmatchingsongs('0xtIp0lgccN85GfGOekS5L', '6nyfDdTwCLGrbCFikT8PTK')