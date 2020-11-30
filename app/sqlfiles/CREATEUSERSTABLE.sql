CREATE TABLE IF NOT EXISTS users (
 id SERIAL NOT NULL PRIMARY KEY,
 CreateDate date,
 username varchar(80) NOT NULL,
 password varchar(80) NOT NULL,
 email varchar(160) NOT NULL)