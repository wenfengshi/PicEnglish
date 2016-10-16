import grpc, sys
import semantic_sim_pb2

_TIMEOUT_SECONDS = 10

def simimain(sent_pair):
    channel = grpc.insecure_channel('%s:%d' % ('54.222.198.42', 50067))
    stub = semantic_sim_pb2.SemanticSimStub(channel)
    response = stub.Communicate(semantic_sim_pb2.ASRRequest(message=sent_pair), _TIMEOUT_SECONDS)
    #print(response.message)
    return response.message

if __name__ == '__main__':
    if(len(sys.argv)<3):
        exit()
    sent_pair = sys.argv[1]+'###'+sys.argv[2]
    simimain(sent_pair) 
