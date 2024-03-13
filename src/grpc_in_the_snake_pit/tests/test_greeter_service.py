import pytest

from concurrent import futures
import grpc
import grpc_testing
from grpc_in_the_snake_pit import helloworld_pb2
from grpc_in_the_snake_pit import helloworld_pb2_grpc

# Import the server's service implementation
from grpc_in_the_snake_pit.server import GreeterService

class TestGreeterService:
    @pytest.fixture(scope="class")
    def server(self):
        """Creates mock server for testing."""
        servicers = {
            helloworld_pb2.DESCRIPTOR.services_by_name["Greeter"]: GreeterService()
        }
        server = grpc_testing.server_from_dictionary(
            servicers, grpc_testing.strict_real_time()
        )
        yield server

    def test_say_hello(self, server):
        """Test the SayHello method."""
        request = helloworld_pb2.HelloRequest(name="test")

        sayhello_method = server.invoke_unary_unary(
            method_descriptor=
                helloworld_pb2.DESCRIPTOR
                .services_by_name["Greeter"]
                .methods_by_name["SayHello"],
                invocation_metadata={},
                request=request,
                timeout=1
        )

        response, metadata, code, details = sayhello_method.termination()

        assert response.message == "Hello, test!", "The response message was not as expected."
        assert code == grpc.StatusCode.OK, "The response code was not as expected."
