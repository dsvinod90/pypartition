from typing import Any, Dict

from flaskr import query_builder


class PartitionByHash:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def define_table(self, table_name: str, partition_column: str, attributes: Dict):
        """
        Create a table as a partitioned table.
        :param table_name: Name of the table
        :param partition_column: Column on which the partitioning is applied
        :param attributes: Attributes of the table
        :return: None
        """
        query = query_builder.define_table_partitioning_by_hash(table_name, partition_column, attributes)
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
        return True

    def create_partition_tables(self, table_name: str, parent_table_name: str, modulus: int, remainder: int):
        """
        Create partition tables from a parent table.
        :param table_name: Name of the partition
        :param parent_table_name: Name of the table of which this table is a partition
        :param modulus:
        :param remainder:
        :return: None
        """
        query = query_builder.create_hash_partitions(table_name, parent_table_name, modulus, remainder)
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
        return True
