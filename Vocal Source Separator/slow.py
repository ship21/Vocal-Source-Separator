#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19 00:20:48 2018

"""
import os
from tqdm import tqdm
import speech_recognition as sr

recogniser = sr.Recognizer()
files = sorted(os.listdir('parts/'))

with open("api-key.json") as api_key:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = api_key.read()

complete_text = []

for file in tqdm(files):
    filename = "parts/" + file
    # Loading  audio file
    with sr.AudioFile(filename) as sourcefile:            
        audiofile = recogniser.record(sourcefile)          
    # Transcribing the audio file
    text = recogniser.recognize_google_cloud(audiofile, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    #print(text)
    complete_text.append(text)
    
#print(complete_text)

trnscript = "\n"
for a, text in enumerate(complete_text):
    #print(a)
    #print(text)
    total_seconds = a * 30
    ''' You can find an easy way to get 
    hours, minutes and seconds from seconds at
    https://stackoverflow.com/questions/775049/python-time-seconds-to-hms'''
    
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    # Formating the time as h:m:s - 30 seconds of text
    trnscript = trnscript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(hours, minutes, seconds, text)

print(trnscript)

with open("transcript.txt", "w") as file:
    file.write(trnscript)
