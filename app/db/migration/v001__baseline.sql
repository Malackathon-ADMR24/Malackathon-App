CREATE TABLE migration(
    name VARCHAR
);

CREATE TABLE contact(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    email VARCHAR NOT NULL
);

-- DATOS DE EJEMPLO

INSERT INTO contact (name, last_name, phone, email) values ('John', 'Doe', '123456789', 'foo@bar.com');
INSERT INTO contact (name, last_name, phone, email) values ('Jane', 'Doe', '111222333', 'baz@bar.org');