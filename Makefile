OFILES = meter_usage_pb2.py meter_usage_pb2_grpc.py

$(OFILES): meter_usage.proto
	python3 -m grpc_tools.protoc -I.  --python_out=. --grpc_python_out=. meter_usage.proto

clean:
	rm $(OFILES)
