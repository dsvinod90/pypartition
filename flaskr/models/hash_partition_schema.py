from marshmallow import Schema, fields, EXCLUDE

from flaskr.models.connection_schema import ConnectionSchema


class HashPartitionSchema(Schema):
    """
    Schema for creating any generic hash partition.
    """
    class Meta:
        unknown = EXCLUDE
    table_name = fields.String(required=True)
    parent_table_name = fields.String(required=True)
    partition_column = fields.String(required=True)
    num_partitions = fields.Integer(required=True)
    db_connection = fields.Nested(ConnectionSchema(), required=True)
