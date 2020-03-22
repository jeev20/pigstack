# pigstack
```
P - Python
I - influxDB
G - grafana
```
Python integration with influxDB and grafana for timeseries visualization. 

![alt text](https://github.com/jeev20/pigstack/blob/master/grafanaDasboard/dashboard-banner.PNG "Dashboard_banner")
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
Although this repository uses a simple python example (server ping status) the integration used can be ported to many other use cases. 

### Prerequisites
1. Python 3.6 or greater
2. InfluxDB 1.7.10 or greater 
3. Grafana 6 or greater 

The only python dependency is influxdb and can be installed by using 

```
$ pip install influxdb
```

### Installing

Clone this repository and navigate into the folder.
```
$ git clone https://github.com/jeev20/pigstack
$ cd pigstack
```

Specify a database name and uncomment line 10 in ```createDatabase.py```
```
database_name = <Your databasename>
client.create_database("database_name")
``` 
Ensure your instance of influxDB service is running and the port is set to default 8086. If you are using a different port for influxDB, you can change the port used in ```updateDatabase.py``` (line 18)

```
database_name = <Your databasename>

client = InfluxDBClient(host="localhost",
                        port=8086,
                        username=<yourusername>,
                        password=<yourpassword>)   
```
Edit the text document with ip addresses you are interested to ping
```
$ cd data
ips.txt
```

Followed by

```
python updateDatabase.py
```
The following output will be printed to console
```
03/22/2020, 15:02:35 : Server status for facebook.com written to pythondemo database
03/22/2020, 15:02:38 : Server status for host.docker.internal written to pythondemo database
03/22/2020, 15:02:57 : Server status for 192.168.21.18 written to pythondemo database
03/22/2020, 15:03:08 : Server status for stackoverflow.com written to pythondemo database
03/22/2020, 15:03:11 : Server status for youtube.com written to pythondemo database
```
Now that your influxDB database is updated. The last part is to visualize the data. 
### Visualizing with grafana

Folks at grafana have written a detailed walkthrough on how to use the influxDB Data source within grafana. 
```
https://grafana.com/docs/grafana/latest/features/datasources/influxdb/
```

You could also use the dashboard attached in this repository by either copying the contents of this json file or importing it as a json file in grafana. 

```
grafanaDasboard/serverpingstatus.json
```

![alt text](https://github.com/jeev20/pigstack/blob/master/grafanaDasboard/dashboard.PNG "Dashboard")

## Authors

* *Initial work* - [jeev20](https://github.com/jeev20)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jeev20/pigstack/blob/master/LICENSE) file for details

## Acknowledgments

* https://gist.github.com/PurpleBooth - for the wonderful readme template 
* https://www.youtube.com/watch?v=PTUhiDnYrbs (https://github.com/labeveryday) - for the base code used in pingServer.py
* https://www.youtube.com/watch?v=O20Y1XR6g0A for python integration with influxDB
* Thanks to folks at grafana and influxDB! 
