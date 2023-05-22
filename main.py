import grpc
import logging
import json
from concurrent import futures
from cap import aiservice_pb2_grpc
from cap import aiservice_pb2
from inference.predict import predict


class InferenceService(aiservice_pb2_grpc.InferenceService):

    def Predict(self,
                request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        data = dict(pdf=[request.prompt_input.data])
        prediction = predict(data)
        return aiservice_pb2.PredictResponse(result=json.dumps(prediction))


def serve():
    port = '50051'
    s = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aiservice_pb2_grpc.add_InferenceServiceServicer_to_server(InferenceService(), s)
    s.add_insecure_port('[::]:' + port)
    s.start()
    print("Server started, listening on " + port)
    s.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
