from spotipy import Spotify
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth


username = 'gfcarter2023'
clientID = 'd915608996ca4262a94e20f152eb6277'
clientSecret = 'de1f2a9f0b384cb0815860e540d956ff'
device_name = 'GRIFFINS-PC'
redirect_uri = 'http://google.com/callback/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

auth_manager = SpotifyOAuth(
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username)
spotify = spotipy.Spotify(auth_manager=auth_manager)

devices = spotify.devices()
deviceID = None
for d in devices['devices']:
    d['name'] = d['name'].replace('’', '\'')
    if d['name'] == device_name:
        deviceID = d['id']
        break

class InvalidSearchError(Exception):
    pass


def get_playlist_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired album
    """

    # Replace all spaces in name with '+'
    original = name
    playlists = spotify.user_playlists(username)

    for playlist in playlists['items']:
        playlist_name = playlist['name'].lower()
        if name.lower() == playlist_name:
            album_uri = playlist['uri']
            return album_uri
    raise InvalidSearchError(f'No artist named "{original}"')


def get_artist_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired artist
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='artist')
    if not results['artists']['items']:
        raise InvalidSearchError(f'No artist named "{original}"')
    artist_uri = results['artists']['items'][0]['uri']
    print(results['artists']['items'][0]['name'])
    return artist_uri

def get_track_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: track name
    :return: Spotify uri of the desired track
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='track')
    print(results)
    if not results['tracks']['items']:
        raise InvalidSearchError(f'No track named "{original}"')
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri


def play_album(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_artist(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_track(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, uris=[uri])

def findSong(query):
    try:
        spotify.shuffle(True, deviceID)
        name = query.replace("play ", "")
        if query.split(' ')[1] == 'album':
            name = name.replace("album ", "")
            uri = get_playlist_uri(spotify=spotify, name=name)
            play_album(spotify=spotify, device_id=deviceID, uri=uri)
        elif query.split(' ')[1] == 'artist':
            name = name.replace("artist ", "")
            uri = get_artist_uri(spotify=spotify, name=name)
            play_artist(spotify=spotify, device_id=deviceID, uri=uri)
        elif query.split(' ')[1] == 'song':
            name = name.replace("song ", "")
            uri = get_track_uri(spotify=spotify, name=name)
            play_track(spotify=spotify, device_id=deviceID, uri=uri)
        else:
            print('Specify either "album", "artist" or "play". Try Again')
    except InvalidSearchError:
        print('InvalidSearchError. Try Again')
