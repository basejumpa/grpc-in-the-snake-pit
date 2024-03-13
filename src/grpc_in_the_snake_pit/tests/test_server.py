import pytest

from concurrent import futures
import grpc
import grpc_testing
from grpc_in_the_snake_pit import helloworld_pb2
from grpc_in_the_snake_pit import helloworld_pb2_grpc

# Import the server's service implementation
from grpc_in_the_snake_pit.server import Greeter

class TestGreeter:
    @pytest.fixture(scope="class")
    def server(self):
        """Creates and starts a gRPC server for testing."""
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        server.add_insecure_port("localhost:0")  # Use an ephemeral port
        server.start()
        yield server
        server.stop(None)

    @pytest.fixture(scope="class")
    def channel(self, server):
        """Creates a gRPC channel to the test server."""
        port = server._state.servers[0]._port
        return grpc.insecure_channel(f"localhost:{port}")

    def test_say_hello(self, channel):
        """Test the SayHello method."""
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="test"))
        assert response.message == "Hello, test!", "The response message was not as expected."
