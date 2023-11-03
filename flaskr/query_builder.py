from typing import Any, Dict


def define_table_partitioning_by_range(table_name: str, partition_column: str, attributes: Dict):
    """
    Build query to define a table for range based partitioning.
    :param table_name: Name of the table
    :param partition_column: Column on which the partitioning is applied
    :param attributes: Attributes of the table
    :return: Query string
    """
    table_attributes = ''
    attribute_count = 0
    for attribute, data_type in attributes.items():
        attribute_count += 1
        if attribute_count < len(attributes):
            table_attributes += str(attribute) + ' ' + str(data_type) + ', '
        else:
            table_attributes += str(attribute) + ' ' + str(data_type)
    return f"CREATE TABLE IF NOT EXISTS {table_name}({table_attributes}) PARTITION BY RANGE ({partition_column});"


def create_range_partitions(table_name: str, parent_table_name: str, from_value: Any, to_value: Any):
    """
    Build query to create range partitions based on a parent table.
    :param table_name: Name of the partition
    :param parent_table_name: Name of the table of which this table is a partition
    :param from_value: Start value for range based partitioning
    :param to_value: End value for range based partitioning
    :return: Query string
    """
    return (f"CREATE TABLE IF NOT EXISTS {table_name} PARTITION OF {parent_table_name} "
            f"FOR VALUES FROM ('{from_value}') TO ('{to_value}')")


def define_table_partitioning_by_hash(table_name: str, partition_column: str, attributes: Dict):
    """
    Build query to define a table for hash based partitioning.
    :param table_name: Name of the table
    :param partition_column: Column on which the partitioning is applied
    :param attributes: Attributes of the table
    :return: Query string
    """
    table_attributes = ''
    attribute_count = 0
    for attribute, data_type in attributes.items():
        attribute_count += 1
        if attribute_count < len(attributes):
            table_attributes += str(attribute) + ' ' + str(data_type) + ', '
        else:
            table_attributes += str(attribute) + ' ' + str(data_type)
    return f"CREATE TABLE IF NOT EXISTS {table_name}({table_attributes}) PARTITION BY HASH ({partition_column});"


def create_hash_partitions(table_name: str, parent_table_name: str, partition_column: str, num_partitions: int):
    """
    Build query to create hash partitions based on a parent table.
    :param table_name: Name of the partition
    :param parent_table_name: Name of the table of which this table is a partition
    :param partition_column: Column name to partition over
    :param num_partitions: Number of partitions to create
    :return: Query string
    """
    return (f"CREATE TABLE IF NOT EXISTS {table_name} PARTITION OF {parent_table_name} "
            f"PARTITION BY HASH ({partition_column}) PARTITIONS {num_partitions}")