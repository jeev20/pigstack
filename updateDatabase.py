from influxdb import InfluxDBClient
from pingServer import server_status
import os
import time

database_name = "pythondemo"

# Reading a text file. This file can be modified as required
current_folder = os.path.dirname(__file__)
def read_text_file(filename):
    ips = []
    filepath = os.path.join(current_folder, f"data/{filename}")
    with open(filepath) as file:
        for line in file:
            ips.append(line.strip())

    return ips

# Initialzing the client object
client = InfluxDBClient(host="localhost",
                        port=8086,
                        username='GRAFANA',
                        password='password')

# Change to the relevant database
client.switch_database(database_name)

t=time.time()
while True:
    if time.time()-t>300:
        ips = read_text_file("ips.txt")
        for i in range(0, len(ips)):
            payload = server_status(ips[i])
            client.write_points(payload)
            named_tuple = time.localtime() # get struct_time
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            print(f"{time_string} : Server status for {ips[i]} written to {database_name} database")
        t=time.time()
        print("")
