'''gTTS

gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. 
Or simply pre-generate Google Translate TTS request URLs to feed to an external program. http://gtts.readthedocs.org/'''

from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')