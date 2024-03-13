import grpc
import pytest
from grpc_testing import server_from_dictionary

from grpc_in_the_snake_pit import helloworld_pb2
from grpc_in_the_snake_pit import helloworld_pb2_grpc

# Import the client functions you want to test
from grpc_in_the_snake_pit.client import run

class TestGreeterClient:
    @pytest.fixture(scope='class')
    def server(self):
        """Creates a mock server for testing."""
        service_descriptors = {
            helloworld_pb2.DESCRIPTOR.services_by_name['Greeter']: helloworld_pb2_grpc.add_GreeterServicer_to_server
        }
        return server_from_dictionary(service_descriptors, grpc.insecure_channel(''))

    @pytest.fixture(scope='class')
    def context(self, server):
        """Provides a testing context including the mock server."""
        return server.invoke_unary_unary(
            method_descriptor=(helloworld_pb2.DESCRIPTOR.services_by_name['Greeter'].methods_by_name['SayHello']),
            invocation_metadata={},
            request=helloworld_pb2.HelloRequest(name='test'),
            timeout=1
        )

    def test_say_hello(self, context):
        """Test the SayHello method."""
        # Setup the mock response
        context.set_response(helloworld_pb2.HelloReply(message='Hello, test!'), (), grpc.StatusCode.OK, '')

        # Execute the client function you wish to test
        response_message = run()  # Adjust this call based on your client script structure

        # Verify the response
        assert response_message == 'Hello, test!', "The response message was not as expected."
