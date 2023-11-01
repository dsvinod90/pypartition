# PyPartition

An API based (Flask) approach that provides a plug-and-play solution to partition postgres database.

## Pre-requisites:
- Python (preferably v3.9)
- PostgreSQL (preferably v16.0)

## Sample Request-Response Cycle
### Define Table for Range Partitioning
#### Request
```curl
curl --location 'http://localhost:5000/api/define_table' \
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
#### Success Response
`Status: 201 CREATED`
```json
{
    "message": "success"
}
```
#### Error Response (Validation Error for request body)
`Status: 400 BAD REQUEST`
```json
{
    "message": {
        "partition_type": [
            "Missing data for required field."
        ]
    },
    "status": "error"
}
```

### Create Range Partition
#### Request
```curl
curl --location 'http://localhost:5000/api/create_range_partition' \
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
#### Success Response
`Status: 201 CREATED`
```json
{
    "message": "success"
}
```
#### Error Response (Validation Error for request body)
`Status: 400 BAD REQUEST`
```json
{
    "message": {
        "to_value": [
            "Missing data for required field."
        ]
    },
    "status": "error"
}
```

## Postman Collection:
[pypartition.postman_collection.json.zip](https://github.com/dsvinod90/pypartition/files/13222682/pypartition.postman_collection.json.zip)

