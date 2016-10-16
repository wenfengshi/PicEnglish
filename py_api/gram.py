import grpc,sys
import grammar_service_pb2

import time, os

arg_filename = 'gram_arg.tmp'
result_filename = 'gram_result.tmp'

_TIMEOUT_SECONDS = 10

def main(txt):
    channel = grpc.insecure_channel('%s:%d' % ('54.222.198.42', 50054))
    stub = grammar_service_pb2.GrammarServiceStub(channel)
    response = stub.GrammarCorrect(grammar_service_pb2.GrammarCorrectRequest(content = txt, error_type = ""), _TIMEOUT_SECONDS)
    # add by swf
    f = open(result_filename, 'w')
    f.write(str(data))
    f.close()  
    #print(response.message)

if __name__ == '__main__':
    # add by swf
    while True:
        time.sleep(0.1)
        if os.path.exists(arg_filename):
            f = open(arg_filename, 'r+')
            arg1 = f.readline().strip('\n')
            main(arg1)
            f.close()
            os.remove(arg_filename)
    #if(len(sys.argv)<2):
    #    exit()
    #main(sys.argv[1])
