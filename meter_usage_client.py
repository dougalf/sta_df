#!/usr/bin/python3
"""Spectral Tech Assignment Dougal Featherstone - gRPC client"""

import logging

import grpc
from google.protobuf import json_format

import meter_usage_pb2
import meter_usage_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = meter_usage_pb2_grpc.MeterUsageStub(channel)
        # In the future we may pass parameters like the start timestamp
        # and number of data_points to return.
        # For now just send an empty placeholder.
        empty = meter_usage_pb2.MeterUsageRequest()
        data_points = stub.ListMeterUsage(empty)
        ret = '['
        for data_point in data_points:
            ret += json_format.MessageToJson(data_point) + ','
        ret = ret[:-1] + ']'
        return ret


if __name__ == '__main__':
    logging.basicConfig()
    run()
