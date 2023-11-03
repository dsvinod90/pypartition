# PyPartition

An API based (Flask) approach that provides a plug-and-play solution to partition postgres database.

## System Architecture
![pyPartition System Architecture-2](https://github.com/dsvinod90/pypartition/assets/26185142/390d9d66-1fd7-4cbc-9f23-68038fe60879)


## Pre-requisites:
- Python (preferably v3.9)
- PostgreSQL (preferably v16.0)

## Run server:
In order to run the server, create a `.env` file in the root directory of the project folder and provide the details for `POSTGRES_USER` and `POSTGRES_PASSWORD`. This file will not be committed to the repository as it has been added to `.gitignore`.

Syntax to run the server (in debug mode): `flask --app flaskr run --debug`

This syntax will serve the flask app by default on port 5000.

*Note: Before running the flask server, please ensure that Postgres is running.*

## Sample API Contract
### Define partition table by range
#### Request
```curl
curl -i --location 'http://localhost:5000/api/define_table' \
--header 'Content-Type: application/json' \
--data '{
    "table_name": "measurement",
    "partition_type": "range",
    "partition_column": "log_date",
    "db_connection": {
        "host_name": "localhost",
        "port_number": 5432,
        "db_name": "test"
    },
    "attributes": {
        "city_id": "int not null",
        "log_date": "date not null",
        "peak_temp": "int",
        "unit_sales": "int"
    }
}'
```
### Create partitions by range
#### Request
```curl
curl -i --location 'http://localhost:5000/api/create_range_partition' \
--header 'Content-Type: application/json' \
--data '{
    "table_name": "measurement_y2006m03",
    "parent_table_name": "measurement",
    "partition_type": "range",
    "from_value": "2006-03-01",
    "to_value": "2006-04-01", 
    "db_connection": {
        "host_name": "localhost",
        "port_number": 5432,
        "db_name": "test"
    }
}'
```
### Sample responses
#### Success Response
```
HTTP/1.1 201 CREATED
Server: Werkzeug/3.0.1 Python/3.9.6
Date: Fri, 03 Nov 2023 22:55:07 GMT
Content-Type: application/json
Content-Length: 27
Connection: close

{
  "message": "success"
}
```
#### Error Response (Validation Error)
```
HTTP/1.1 400 BAD REQUEST
Server: Werkzeug/3.0.1 Python/3.9.6
Date: Fri, 03 Nov 2023 22:56:10 GMT
Content-Type: application/json
Content-Length: 115
Connection: close

{
  "message": {
    "partition_type": [
      "Missing data for required field."
    ]
  },
  "status": "error"
}
```

## Postman Collection:
[pypartition.postman_collection.json.zip](https://github.com/dsvinod90/pypartition/files/13222682/pypartition.postman_collection.json.zip)

