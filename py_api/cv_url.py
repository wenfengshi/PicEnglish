import httplib, urlparse, urllib2 , base64,sys,urllib
import time, os

arg_filename = 'cv_url_arg.tmp'
result_filename = 'cv_url_result.tmp'

def main(imgUrl):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '670c1e10410948859759d9eae3939ea8',
    }

    params = urllib.urlencode({
        'visualFeatures': 'Tags,Description',
        'details': 'Celebrities',
    })

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{\"url\":\"%s\"}"%imgUrl, headers)
        response = conn.getresponse()
        data = response.read()
        # add by swf
        f = open(result_filename, 'w')
        f.write(str(data))
        f.close()  
        #print(str(data))
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    # add by swf
    while True:
        time.sleep(0.01)
        if os.path.exists(arg_filename):
            f = open(arg_filename, 'r+')
            arg1 = f.readline().strip('\n')
            main(arg1)
            f.close()
            os.remove(arg_filename)
#    if(len(sys.argv)<2):
#        exit()
#    main(sys.argv[1])

