import grpc
import logging
import json
import os
from grpc_reflection.v1alpha import reflection
from concurrent import futures
from platform_srv import aiservice_pb2_grpc
from platform_srv import aiservice_pb2
from inference.predict import predict, init_predictor, ready

LISTEN_ADDRESS = os.getenv("PLATFORM_SRV_ADDR", "unix://var/run/inference.sock")


class InferenceService(aiservice_pb2_grpc.InferenceServiceServicer):

    def Predict(self, request, context):
        if not ready():
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("the server is not ready yet, bootstrap it first!")
            return
        data = dict(pdf=[request.file_input.path])
        prediction = predict(data)
        return aiservice_pb2.PredictResponse(result=json.dumps(prediction))

    def Ready(self, request, context):
        return aiservice_pb2.ReadyResponse(ready=ready())

    def Bootstrap(self, request, context):
        init_predictor()
        return aiservice_pb2.BootstrapResponse(ok=ready())


def serve():
    s = start_grpc_server()
    s.wait_for_termination()


def start_grpc_server() -> grpc.Server:
    print("Starting gRPC server...")
    port = '50051'
    s = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aiservice_pb2_grpc.add_InferenceServiceServicer_to_server(InferenceService(), s)
    enabled_reflection(s)
    s.add_insecure_port(LISTEN_ADDRESS)
    s.start()
    print("Server started, listening on 0.0.0.0:" + port)
    return s


def enabled_reflection(s: grpc.Server):
    service_name = (
        aiservice_pb2.DESCRIPTOR.services_by_name['InferenceService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_name, s)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
