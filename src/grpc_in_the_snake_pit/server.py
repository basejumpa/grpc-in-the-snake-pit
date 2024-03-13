from concurrent import futures
import logging
import grpc
from grpc_in_the_snake_pit import helloworld_pb2
from grpc_in_the_snake_pit import helloworld_pb2_grpc

# Implement the service
class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print(f"Got call SayHello(\"{request.name}\"). Return: \"Hello, {request.name}!\"")
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

# Create a gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening...")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
