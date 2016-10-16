import httplib, urlparse , json, sys
import time, os

arg_filename = 'voice_arg.tmp'
result_filename = 'voice_result.tmp'

apiKey = "cf704acb40a24cdab3b4f8f8d41d3cb5"
voicePath = ""

def main(text, uid):
    params = ""
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"
    conn = httplib.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    accesstoken = data.decode("UTF-8")
    body = "<speak version='1.0' xml:lang='en-us'><voice xml:lang='en-us' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>"+text+"</voice></speak>"

    headers = {"Content-type": "application/ssml+xml", 
               "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm", 
               "Authorization": "Bearer " + accesstoken, 
               "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
               "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
               "User-Agent": "TTSForPython"}

    conn = httplib.HTTPSConnection("speech.platform.bing.com")
    conn.request("POST", "/synthesize", body, headers)
    response = conn.getresponse()

    data = response.read()
    open(voicePath+uid+".wav","wb").write(data)
    conn.close()

if __name__ == '__main__':
    # add by swf
    while True:
        time.sleep(0.1)
        if os.path.exists(arg_filename):
            f = open(arg_filename, 'r+')
            arg1 = f.readline().strip('\n')
            arg2 = f.readline().strip('\n')
            main(arg1, arg2)
            f.close()
            os.remove(arg_filename)
    #f(len(sys.argv)<3):
    #   exit()
    #main(sys.argv[1], sys.argv[2])
