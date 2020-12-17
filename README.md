# sta_df
Spectral Technical Assignment - Dougal Feathertone.

# Description
Language-independent gRPC-based microservice.

Serves the time based electricity consumption data found in meterusage.csv.
* gRPC server that reads the csv file.
* HTTP server that requests the data from the gRPC server
and serves if via JSON.
* Single page HTML doc that requests the JSON file and diplays it as a table.


# Installation
See requirements.txt

# Usage
## Start the gRPC server
In directory sta_df
`make
./meter_usage_server.py`
## Start the HTTP server
In directory sta_df
`export FLASK_ENV=development
export FLASK_APP=run.py
flask run --host=0.0.0.0`
## Request the data
In a brower go to:
`http://<server hostname>:5000/`

# TDB
* Request list of available timestamps.
* Request slices of the dataset eg
  * the single reading for a given timestamp,
  * X readings after a given timestamp.
  * readings for a range between 2 timestamps,
* Graph the data on the front end.
* Add access authentication on the HTTP server.
* Security audit.
* Create unit tests, integrate with Github CI/CD
* Better error handling throughout.
* Check that time data is deliebrately UTC.

# Developer's guide
## meter_usage.proto
_Describes the instantiation of gRPC protocol used._

Currently just an empty request message
which is answered with a stream of (timestamp, electricity usage) tuples
giving all the entries in the csv file.

## meter_usage_server.py
_gRPC server._
On start-up reads the meterusage.csv (see meter_usage_server_resources.py)
into a list of Protocol Buffer tuples of (time, meterusage).
Function ListMeterUsage returns the entire list.

You can test this is working using
`meter_usage_client.py`

## run.py
_Built within the Flask framework._
Servers the single file "index.html". See app/views.py and app/templates/.
index.html includes Javascript function meter_usage,
see app/static/meter_usage.js.
This function is called on page load by the browser
and makes a HTTP GET request to /get_meter_usage.
The server calls the run funciton in meter_usage_client.py
which executes the RPC on the server, converts the result to JSON
and returns that to the browser.
The browser then accesses the DOM to display the result in tabular form.
