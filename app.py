from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__, static_folder="/Users/joelsaarinen/projects/spotifywa/static")
import spotify

chosensongs = []

@app.route("/", methods=["POST", "GET"])
def home():
  #first type of POST request; search for artist top songs
  if request.method == "POST" and not "addbutton" in request.form:
    rawformdata = (request.form).values()
    value_iterator = iter(rawformdata)
    convformdata = next(value_iterator)
    client_id = '85725aa023e545729e6630b2a369cf90'
    client_secret = '1abf0e31be774f2d9fb434adb538ae87'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    searchbynameresult = spotify.search(q='artist:' + convformdata, type='artist')
    artistitems = searchbynameresult['artists']['items']
    artist = artistitems[0]
    artist_uri = artist['uri']
    trackresults = spotify.artist_top_tracks(artist_uri)
    return render_template("artistsearch.html", results=trackresults)
  elif request.method == "POST" and "addbutton" in request.form:
    rawformdata = (request.form).values()
    value_iterator = iter(rawformdata)
    songId = next(value_iterator)
    #trackurl = 'https://api.spotify.com/v1/tracks/' + songId
    client_id = '85725aa023e545729e6630b2a369cf90'
    client_secret = '1abf0e31be774f2d9fb434adb538ae87'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    relevanttrack = spotify.track(songId)
    chosensongs.append(relevanttrack)
    return render_template("playlistdisplay.html", playlist=chosensongs)
  else:
    return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)