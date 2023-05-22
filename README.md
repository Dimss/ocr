# Cnvrg AI Services bundle package for OCR Service

### Inference
All the AI stuff under ./inference` dir 

### Platform integration
Under `./platform_srv` the [platform gRPC server implementation](https://github.com/Dimss/aisi/blob/main/proto/aiservice/v1/aiservice.proto). 


### AI Inference service lifecycle loop
```bash
export SRV_ADDR=20.1.158.162:50051

grpcurl \
 -plaintext \
 -d '{ "file_input": {"path": "/home/dkartsev/ocrnew/text-extraction/Datascience.pdf"} }' \
 $SRV_ADDR \
 aiservice.v1.InferenceService/Predict

grpcurl \
 -plaintext \
 $SRV_ADDR \
 aiservice.v1.InferenceService/Bootstrap

grpcurl \
 -plaintext \
 $SRV_ADDR \
 aiservice.v1.InferenceService/Ready

```