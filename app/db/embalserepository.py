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
            in self.db_connection.execute_query(
                "SELECT id, nombre, demarc, cauce, provincia, ccaa, tipo, cota_coron, alt_cimien, x, y FROM embalses join listado on embalses.embalse_nombre = listado.nombre")
        ]

    def get(self, id: int) -> Embalse:
        return self._map_row(
            self.db_connection.execute_query(
                "SELECT id, nombre, demarc, cauce, provincia, ccaa, tipo, cota_coron, alt_cimien, x, y FROM embalses join listado on embalses.embalse_nombre = listado.nombre WHERE id=?",
                (id,))[0]
        )

    def search(self, predicate: str) -> Embalse:
        return self.db_connection.execute_query("SELECT * FROM embalses WHERE " + predicate)

    def _map_row(self, row) -> Embalse:
        embalse = Embalse(*row)
        embalse.x = embalse.x.replace(".", "")
        embalse.y = embalse.y.replace(".", "")
        embalse.x = float(embalse.x[:2] + "." + embalse.x[2:])
        embalse.y = float(embalse.y[:2] + "." + embalse.y[2:])
        return embalse

    def __del__(self):
        self.db_connection.close()
