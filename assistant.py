import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pandas as pd
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

from SpotifyCommands import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query

def wishMe():
    speak("Welcome Griffin")

def runSpotify():
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
    spotify = sp.Spotify(auth_manager=auth_manager)

    # Selecting device to play from
    devices = spotify.devices()
    deviceID = None
    for d in devices['devices']:
        d['name'] = d['name'].replace('’', '\'')
        if d['name'] == device_name:
            deviceID = d['id']
            break
        name = ' '.join(words[2:])
        try:
            if query[1] == 'album':
                uri = get_playlist_uri(spotify=spotify, name=name)
                play_album(spotify=spotify, device_id=deviceID, uri=uri)
            elif query[1] == 'artist':
                uri = get_artist_uri(spotify=spotify, name=name)
                play_artist(spotify=spotify, device_id=deviceID, uri=uri)
            elif query[1] == 'song':
                uri = get_track_uri(spotify=spotify, name=name)
                play_track(spotify=spotify, device_id=deviceID, uri=uri)
            else:
                print('Specify either "album", "artist" or "play". Try Again')
        except InvalidSearchError:
            print('InvalidSearchError. Try Again')


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()

    while True:

        query = takeCommand().lower()

        if "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
            continue

        elif "play" in query:
            runSpotify()


whatToDo = ""