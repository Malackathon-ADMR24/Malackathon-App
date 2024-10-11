import os
from pathlib import Path

from app.db import databaseconnection


def migrate():
    base_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    migration_files = [
        filepath
        for filepath
        in os.listdir(base_dir)
        if filepath.endswith(".sql")
    ]

    db_connection = databaseconnection.DatabaseConnection()
    db_connection.connect()
    existing_migrations = []
    try:
        existing_migrations = db_connection.execute_query("SELECT * FROM migration")
    except:
        print("Is database new?")

    new_migration_files = [file for file in migration_files if (file,) not in existing_migrations]

    for sql_file in new_migration_files:
        with open(base_dir / sql_file) as fh:
            db_connection.execute_script(fh.read())
        db_connection.execute_query("INSERT INTO migration VALUES (?)", (sql_file,))
    db_connection.close()
