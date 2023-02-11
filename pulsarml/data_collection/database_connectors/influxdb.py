from database_actions import DatabaseActions, DatabaseActionsFactory
from influxdb import DataFrameClient


class InfluxdbActions(DatabaseActions):
    """Infuxdb database connection"""

    def make_connection(
        self, host: str, port: int, password: str, database_name: str, ssl: bool = False, verify_ssl: bool = False
    ) -> DataFrameClient:
        """Makes connection to the Influxdb database"""

        return DataFrameClient(host=host, port=port, password=password, database_name: str, ssl=ssl, verify_ssl=verify_ssl)

    def write_data(self, client: DataFrameClient):
        """Sends data to the database"""
        pass
        # client.write_points


class Influxdb(DatabaseActionsFactory):
    """Infuxdb database connection"""

    def get_database_actions(self) -> DatabaseActions:
        """Makes connection to the Influxdb database"""
        return InfluxdbActions
