from marshmallow import Schema, fields, EXCLUDE


class ConnectionSchema(Schema):
    """
    Schema for creating any database connection
    """
    class Meta:
        unknown = EXCLUDE
    host_name = fields.String(required=True)
    port_number = fields.Integer(required=True)
    db_name = fields.String(required=True)
