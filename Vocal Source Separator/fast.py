#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 5 00:14:36 2018

"""
import os
import speech_recognition as sr
from multiprocessing.dummy import Pool
pool = Pool(8) # Number of concurrent threads

recogniser = sr.Recognizer()
files = sorted(os.listdir('parts/'))

with open("api-key.json") as api_key:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = api_key.read()

def transcriber(data):
    index, file = data
    filename = "parts/" + file
    print(filename + " started\n")
    # Loading the audio file
    with sr.AudioFile(filename) as sourcefile:             
        audiofile = recogniser.record(sourcefile)
    #print("hi")    
    # Transcribing the audio file
    text = recogniser.recognize_google_cloud(audiofile, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    print(filename + " done\n")
    print(text)
    return {
        "index": index,
        "text": text
    }

complete_text = pool.map(transcriber, enumerate(files))
pool.close()
pool.join()

trnscript = ""
for a in sorted(complete_text, key=lambda x: x['index']):
    total_seconds = a['index'] * 30
    ''' You can find an easy way to get 
    hours, minutes and seconds from seconds at
    https://stackoverflow.com/questions/775049/python-time-seconds-to-hms'''
    
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    # Formating the time as h:m:s - 30 seconds of text
    trnscript = trnscript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(hours, minutes, seconds, a['text'])

print(trnscript)

with open("transcript.txt", "w") as file:
    file.write(trnscript)
