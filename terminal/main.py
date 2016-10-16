import sys, json
import cv_local,simi,voice
import pyaudio  
import wave

def play(voicePath):
    chunk = 1024  
    f = wave.open(voicePath,"rb")   
    p = pyaudio.PyAudio()  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    data = f.readframes(chunk)  
    while data != '':  
        stream.write(data)  
        data = f.readframes(chunk)  
    stream.stop_stream()  
    stream.close()  
    p.terminate()

cent=""
def docv(imgPath):
    res=json.loads(cv_local.require(imgPath))
    for w in res["tags"]:
        print(w["name"])
    cent=res["description"]["captions"][0]["text"]
    print(cent)
    play(voice.require(cent))
    
def docompare(imgPath,text):
    docv(imgPath)
    print(simi.require(cent,text))
    
if __name__=="__main__":
    if(len(sys.argv)==2):
        docv(sys.argv[1])
    if(len(sys.argv)==3):
        docompare(sys.argv[1],sys.argv[2])
