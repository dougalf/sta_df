#!/usr/bin/python3

import json
from app import app
import meter_usage_client


def json_meter_usage_data():
    return meter_usage_client.run()

@app.route('/get_meter_usage', methods=['GET'])
def meter_usage():
    return json_meter_usage_data()

if __name__ == '__main__':
    app.run()
