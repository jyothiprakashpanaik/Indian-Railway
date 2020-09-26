import os
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)


def margeAudio(audios):
    combined = AudioSegment.empty()
    for audio in audios :
        combined += AudioSegment.from_mp3(audio)
    return combined

    
def generateSkeleton():
    '''generate krupaya dhyan dhejeya'''
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 generating Krypaya dhayan 
    start = 19000
    finish = 23000
    audioProcess = audio[start:finish]
    audioProcess.export("1_annon.mp3",format="mp3")
    # 2 from city

    # 3 ke rasthe
    start = 29250
    finish = 29900
    audioProcess = audio[start:finish]
    audioProcess.export("3_annon.mp3",format="mp3")
    # 4 to city 

    # 5 ko jana avli 
    start = 30500
    finish = 31500
    audioProcess = audio[start:finish]
    audioProcess.export("5_annon.mp3",format="mp3")
    # 6,7 train number and name
    
    # 8 apani nertharith sami
    start = 32000
    finish = 33000
    audioProcess = audio[start:finish]
    audioProcess.export("8_annon.mp3",format="mp3") 
    # 9 time
    
    # 10 platforn number per avage 
    start = 37000
    finish = 38000
    audioProcess = audio[start:finish]
    audioProcess.export("10_annon.mp3",format="mp3")

    
    # 11 platform 

    # 12 per sa jayagi 
    start = 38500
    finish = 40000
    audioProcess = audio[start:finish]
    audioProcess.export("12_annon.mp3",format="mp3") 

def generateAnnoun(filename):
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        # 2 from city generate
        textToSpeech(item['from'],'2_annon.mp3')

        # 4 to city generator
        textToSpeech(item['to'],'4_annon.mp3')

        # 6,7 train name and number
        textToSpeech(item['train_no'] ,'6_annon.mp3')
        textToSpeech(item['train_name'] ,'7_annon.mp3')

        # 9 time 
        textToSpeech(item['time'],'9_annon.mp3')

        # 11 platform number
        textToSpeech(item['platform'],'11_annon.mp3')

        audio = [f"{i}_annon.mp3" for i in range(1,13)]

        anounouncement = margeAudio(audio)
        anounouncement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format = "mp3")

if __name__ == "__main__":
    print('Genrating Skeleton')
    generateSkeleton()
    print('Generating Announcemene')
    generateAnnoun('train_annon.xlsx')
