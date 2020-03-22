from influxdb import InfluxDBClient

client = InfluxDBClient(host="localhost", port=8086)

database_name = "pythondemo"

# Which databses exist?
print(client.get_list_database())

#client.create_database(database_name)
client.switch_database(database_name)

# Is the database empty?
print(client.query('select * from pythondemo'))
