#!/usr/bin/python3
"""Interface functions for gRPC server"""
    
import csv
import datetime
import meter_usage_pb2
from google.protobuf.timestamp_pb2 import Timestamp


class MeterUsageDB():
    """Abstraction layer for meter usage data access."""
    def __init__(self):
        pass

class MeterUsageDBCSV(MeterUsageDB):
    """Currently the only data access method is via a CSV file."""
    def __init__(self):
        self.data_points = []
        super().__init__()

    def open(self, filename):
        with open(filename, newline='') as f:
            # csv first line should hold the field names: time, meterusage.
            # TBD better error handling
            reader = csv.DictReader(f, dialect='unix')
            try:
                for row in reader:
                    # WARN assumptions about data format in csv
                    # WARN assumption that date is UTC
                    time = Timestamp()
                    time.FromDatetime(datetime.datetime.strptime(
                            row['time'],
                            '%Y-%m-%d %H:%M:%S'))
                    meterusage = float(row['meterusage'])
                    data_point = meter_usage_pb2.DataPoint(
                            time=time,
                            meterusage=meterusage)
                    self.data_points.append(data_point)
            except csv.Error as e:
                sys.exit(f'file {filename}, line {reader.line_num}: {e}')

