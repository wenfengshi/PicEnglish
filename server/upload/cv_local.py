import httplib, urlparse, urllib2 , base64,sys,urllib

def main(imgPath):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '670c1e10410948859759d9eae3939ea8',
    }

    params = urllib.urlencode({
        'visualFeatures': 'Tags,Description',
        'details': 'Celebrities',
    })

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, open(imgPath,"rb").read(), headers)
        response = conn.getresponse()
        data = response.read()
        print(str(data))
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    if(len(sys.argv)<2):
        exit()
    main(sys.argv[1])
