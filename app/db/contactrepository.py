from app.db import databaseconnection
from app.domain.contact import Contact


class ContactRepository:
    def __init__(self):
        self.db_connection = databaseconnection.DatabaseConnection()
        self.db_connection.connect()

    def get_all(self) -> [Contact]:
        return [
            self._map_row(row)
            for row
            in self.db_connection.execute_query("SELECT * FROM contact")
        ]

    def get(self, id: int) -> Contact:
        return self._map_row(
            self.db_connection.execute_query("SELECT * FROM contact WHERE id=?", (id,))[0]
        )

    def search(self, predicate: str) -> Contact:
        return self.db_connection.execute_query("SELECT * FROM contact WHERE " + predicate)

    def save(self, contact: Contact):
        if contact.id is None:
            self._insert(contact)
            contact.id = self.db_connection.last_rowid
        else:
            self._update(contact)

    def delete(self, id: int):
        return self.db_connection.execute_query("DELETE FROM contact WHERE id=?", (id,))

    def _insert(self, contact: Contact):
        self.db_connection.execute_query(
            """INSERT INTO contact (name, last_name, phone, email) VALUES (?, ?, ?, ?)""",
            (contact.name, contact.last_name, contact.phone, contact.mail)
        )

    def _update(self, contact: Contact):
        self.db_connection.execute_query(
            """UPDATE contact SET name=?, last_name=?, phone=?, email=? WHERE id=?""",
            (contact.name, contact.last_name, contact.phone, contact.mail, contact.id)
        )

    def _map_row(self, row) -> Contact:
        return Contact(*row)

    def __del__(self):
        self.db_connection.close()
