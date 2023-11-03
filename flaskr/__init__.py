import json
from functools import wraps
from typing import Dict

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from flaskr.connector import Connector
from flaskr.constants import Constants
from flaskr.declarative_partitioning.partition_by_range import PartitionByRange
from flaskr.declarative_partitioning.partition_by_hash import PartitionByHash
from flaskr.models.range_partition_schema import RangePartitionSchema
from flaskr.models.hash_partition_schema import HashPartitionSchema
from flaskr.models.table_schema import TableSchema

app = Flask(__name__)


def required_params(schema):
    """
    Decorator to validate request body.
    :param schema: Schema based on which validation will be done
    :return: None
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    "status": Constants.ERROR_MESSAGE.value,
                    "message": err.messages
                }
                return jsonify(error), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator
# pbr_object.create_partition_tables('measurement_y2006m03', 'measurement', '2006-03-01', '2006-04-01')


def establish_connection(db_connection_details: Dict):
    """
    Connect to database based on hostname, dbname and port number provided in the db_connection_details dictionary.
    :param db_connection_details: Dictionary with all the details required to connect to the database
    :return: Connection object
    """
    conn = Connector(db_connection_details['host_name'],
                     db_connection_details['db_name'],
                     db_connection_details['port_number'])
    return conn.connection


@app.route('/api/define_table', methods=['POST'])
@required_params(TableSchema())
def define_table():
    """
    Post endpoint to define a table in the database with given partition parameters and attributes.
    :return:
    """
    partition = None
    request_data = json.loads(request.data)
    connection = establish_connection(request_data['db_connection'])
    if request_data['partition_type'] == Constants.PARTITION_TYPE_RANGE.value:
        partition = PartitionByRange(connection)
    elif request_data['partition_type'] == Constants.PARTITION_TYPE_HASH.value:
        partition = PartitionByRange(connection)
    if partition and partition.define_table(request_data['table_name'],
                                            request_data['partition_column'],
                                            request_data['attributes']):
        return jsonify({"message": Constants.SUCCESS_MESSAGE.value}), Constants.CREATED.value
    else:
        return jsonify({"message": Constants.ERROR_MESSAGE.value}), Constants.INTERNAL_SERVER_ERROR.value


@app.route('/api/create_range_partition', methods=['POST'])
@required_params(RangePartitionSchema())
def create_partition():
    request_data = json.loads(request.data)
    connection = establish_connection(request_data['db_connection'])
    partition = PartitionByRange(connection)
    if partition.create_partition_tables(request_data['table_name'],
                                         request_data['parent_table_name'],
                                         request_data['from_value'],
                                         request_data['to_value']):
        return jsonify({"message": Constants.SUCCESS_MESSAGE.value}), Constants.CREATED.value
    return jsonify({"message": Constants.ERROR_MESSAGE.value}), Constants.INTERNAL_SERVER_ERROR.value

@app.route('/api/create_range_partition', methods=['POST'])
@required_params(HashPartitionSchema())
def create_hash_partition():
    request_data = json.loads(request.data)
    connection = establish_connection(request_data['db_connection'])
    partition = PartitionByHash(connection)
    if partition.create_partition_tables(request_data['table_name'],
                                         request_data['parent_table_name'],
                                         request_data['modulus'],
                                         request_data['remainder']):
        return jsonify({"message": Constants.SUCCESS_MESSAGE.value}), Constants.CREATED.value
    return jsonify({"message": Constants.ERROR_MESSAGE.value}), Constants.INTERNAL_SERVER_ERROR.value
