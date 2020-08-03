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
from artist_matching_songs import artistmatchingsongs
from find_artist import find_artist
import numpy
import sklearn
from sklearn.metrics import mean_squared_error

#so here we need to implement artist_matching_songs, find_artist together to generate
#similar songs (from Pakistani artists rn) for a given, chosen song by a Notemad user.