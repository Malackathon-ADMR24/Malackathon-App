CREATE TABLE migration(
    name TEXT
);

CREATE TABLE contact(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
);
