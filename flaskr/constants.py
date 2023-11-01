from enum import Enum


class Constants(Enum):
    # Types of partition
    PARTITION_TYPE_LIST = 'list'
    PARTITION_TYPE_HASH = 'hash'
    PARTITION_TYPE_RANGE = 'range'

    # Response Messages
    ERROR_MESSAGE = 'error'
    SUCCESS_MESSAGE = 'success'

    # Response Status Codes
    CREATED = 201
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500