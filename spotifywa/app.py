from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__, static_folder="/Users/joelsaarinen/projects/spotifywa/static")

@app.route("/", methods=["POST", "GET"])
def home():
  if request.method == "POST":
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
  else:
    return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)