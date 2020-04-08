from gtts import gTTS
import os
language='en'
text_1=input("Enter text")
output=gTTS(text=text_1,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")
