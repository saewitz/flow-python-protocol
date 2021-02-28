import grpc
import access_pb2
import access_pb2_grpc

channel = grpc.insecure_channel('access.devnet.nodes.onflow.org:9000')
stub = access_pb2_grpc.AccessAPIStub(channel)
print("Latest block header height: " + str(stub.GetLatestBlockHeader(access_pb2.GetLatestBlockHeaderRequest()).block.height))