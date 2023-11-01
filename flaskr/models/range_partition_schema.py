from marshmallow import Schema, fields, EXCLUDE

from flaskr.models.connection_schema import ConnectionSchema


class RangePartitionSchema(Schema):
    """
    Schema for creating any generic partition.
    """
    class Meta:
        unknown = EXCLUDE
    table_name = fields.String(required=True)
    parent_table_name = fields.String(required=True)
    from_value = fields.String(required=True)
    to_value = fields.String(required=True)
    db_connection = fields.Nested(ConnectionSchema(), required=True)
