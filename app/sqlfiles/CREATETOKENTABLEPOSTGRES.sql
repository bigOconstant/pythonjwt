CREATE TABLE IF NOT EXISTS tokens
(id INTEGER NOT NULL PRIMARY KEY, creationdate timestamp NOT NULL , expirationdate timestamp, token text, userid INTEGER NOT NULL)