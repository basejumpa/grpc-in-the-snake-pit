import grpc
from grpc_in_the_snake_pit import helloworld_pb2
from grpc_in_the_snake_pit import helloworld_pb2_grpc

def run():
    # Connect to server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        # Synchronous call
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='World'))
        print(f"Call SayHello(\"World\") returned \"{response.message}\"")
        return response.message  # Add this line to return the message for testing

        # Asynchronous call
        # async for response in stub.SayHelloAsync(helloworld_pb2.HelloRequest(name='Async World')):
        #    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
