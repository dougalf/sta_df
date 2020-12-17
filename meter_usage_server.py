#!/usr/bin/python3
"""Spectral Tech Assignment Dougal Featherstone - gRPC server"""

from concurrent import futures
import logging

import grpc

import meter_usage_pb2
import meter_usage_pb2_grpc
import meter_usage_server_resources


class MeterUsageServicer(meter_usage_pb2_grpc.MeterUsageServicer):
    """Provides methods of the meter usage servicer."""

    def __init__(self):
        self.db = meter_usage_server_resources.MeterUsageDBCSV()
        self.db.open("meterusage.csv")

    def ListMeterUsage(self, request, context):
        for data_point in self.db.data_points:
            yield data_point


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_usage_pb2_grpc.add_MeterUsageServicer_to_server(
            MeterUsageServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
