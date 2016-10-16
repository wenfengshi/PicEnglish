import grpc, sys
import semantic_sim_pb2
import time, os

arg_filename = 'simi_arg.tmp'
result_filename = 'simi_result.tmp'

_TIMEOUT_SECONDS = 10

def main(sent_pair):
    channel = grpc.insecure_channel('%s:%d' % ('54.222.198.42', 50067))
    stub = semantic_sim_pb2.SemanticSimStub(channel)
    response = stub.Communicate(semantic_sim_pb2.ASRRequest(message=sent_pair), _TIMEOUT_SECONDS)
    # add by swf
    f = open(result_filename, 'w')
    f.write(str(data))
    f.close()  
    #print(response.message)

if __name__ == '__main__':
    # add by swf
    while True:
        time.sleep(0.01)
        if os.path.exists(arg_filename):
            f = open(arg_filename, 'r+')
            arg1 = f.readline().strip('\n')
            arg2 = f.readline().strip('\n')
            sent_pair = arg1+'###'+arg2
            main(sent_pair)
            f.close()
            os.remove(arg_filename)
    
#if(len(sys.argv)<3):
#    exit()
#sent_pair = sys.argv[1]+'###'+sys.argv[2]
#main(sent_pair) 
