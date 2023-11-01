from marshmallow import Schema, fields, EXCLUDE

from flaskr.models.connection_schema import ConnectionSchema


class TableSchema(Schema):
    """
    Schema for creating any generic table with partitions
    """
    class Meta:
        unknown = EXCLUDE
    table_name = fields.String(required=True)
    partition_type = fields.String(required=True)
    partition_column = fields.String(required=True)
    db_connection = fields.Nested(ConnectionSchema(), required=True)
