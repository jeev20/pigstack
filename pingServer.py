import os
from random import randint


def server_status(ip):
    """
    Ping the given server and read the stdout
    return: a json formatted string required by influxDB
    """
    ping = os.popen(f"ping {ip}").read()
    if "Sent = 4" and "Received = 4" in ping:
        server = ip
        value = 100
    elif "Sent = 3" and "Received = 3" in ping:
        server = ip
        value = 75
    elif "Sent = 2" and "Received = 2" in ping:
        server = ip
        value = 50
    elif "Sent = 1" and "Received = 1" in ping:
        server = ip
        value = 25
    else:
        server = ip
        value = 0

    json_body = [
        {
            "measurement": server,
            "tags": {
                "tag1" :"pingstatus"
            },
            "fields": {
                "value": value
            }
        }
        ]
    return json_body

