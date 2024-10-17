from app.db import databaseconnection
from app.domain.embalse import Embalse


class EmbalseRepository:
    def __init__(self):
        self.db_connection = databaseconnection.DatabaseConnection()
        self.db_connection.connect()

    def get_all(self) -> [Embalse]:
        return [
            self._map_row(row)
            for row
            in self.db_connection.execute_query("SELECT * FROM Embalse")
        ]

    def get(self, id: int) -> Embalse:
        return self._map_row(
            self.db_connection.execute_query("SELECT * FROM embalse WHERE id=?", (id,))[0]
        )

    def search(self, predicate: str) -> Embalse:
        return self.db_connection.execute_query("SELECT * FROM embalse WHERE " + predicate)

    def _map_row(self, row) -> Embalse:
        return Embalse(*row)

    def __del__(self):
        self.db_connection.close()
