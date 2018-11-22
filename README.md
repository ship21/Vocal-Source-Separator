# Vocal-Source-Separator
Vocal Source Separator is a software that takes an audio file as input and can recognise vocals from it and converts them into a text file.

**INTRODUCTION :** 
Speech is a complex phenomenon. It is always useful to have speech in the form of text to study. Lengthy audio files containing music and important speech only at certain points is difficult to comprehend as audio but suppose we have a system which is separating the vocal/speech part into a text file, then it will be so much easier to study the important information. This can be seen from the following example. Suppose a person had an hour and a half audio recording from a hand-over meeting with his former co-worker. He remembered that he mentioned something at some point, but was dreading listening through 1.5-hour audio file to find it. By running the recording through this system, he can quickly find the needed keywords. This idea is used as a motivation for this project.

**IMPLEMENTATION DETAILS :**
Following are the technologies used in this project:
1. Backend was developed using python language.
2. Google cloud speech API
3. Python modules like Numpy, Librosa, Matplotlib’s pyplot, speech recognition, PyQt5
4. Software required- Qt Designer (For GUI)


**STEPS :**
1. There is a "main.py" file which is the main file(GUI file) from where the execution actually starts.(You need to make the necessary changes in it according to your computer).
2. There are two buttons "Get Graphs" and "Convert" which calls the two separate python scripts for converting an audio file to its text and getting graphs.
3. There are some steps you need to follow to use The GOOGLE CLOUD SPEECH API.
    **-Sign Up for a Free Tier Account**
        Google Cloud offers a Free Tier plan, which i have used. An account is required to get an API key.
    **-Generate an API Key**
        Follow these steps to generate an API key:
          Sign-in to Google Cloud Console
          Click “API Manager”
          Click “Credentials”
          Click “Create Credentials”
          Select “Service Account Key”
          Under “Service Account” select “New service account”
          Name service (whatever you’d like)
          Select Role: “Project” -> “Owner”
          Leave “JSON” option selected
          Click “Create”
          Save generated API key file
          Rename file to api-key.json
          Make sure to move the key into speech-to-text cloned repo, if you plan to test this code.
 4. **Convert Audio File to Wav format :** Also this google api only accepts the audio files in .wav file so you need to covert it to .wav format using any of the softwares available onlie like audacity.
 5. **Install required Python modules :** I added requirements.txt in example repo with all needed libraries. It can be used      to install all via:

   pip3 install -r requirements.txt
 6. There are two version of the Script one is slow and other one is somewhat fast.I have attached both of them.
 





  
