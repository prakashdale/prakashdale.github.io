"""
There are several APIs available to convert text to speech in python. 
One of such APIs is the Google Text to Speech API commonly known as the gTTS API. 
gTTS is a very easy to use tool which converts the text entered, 
into audio which can be saved as a mp3 file.

The gTTS API supports several languages including English, 
Hindi, Tamil, French, German and many more. 
The speech can be delivered in any one of the two available audio speeds, fast or slow.

pip install gTTS
"""

from gtts import gTTS
import os

myText = "Welcome to python programming"

language = "en"

myObj = gTTS(text=myText, lang=language, slow=False)

myObj.save("mytext.mp3")

# Playing the converted file
#os.system("mpg321 mytext.mp3")



