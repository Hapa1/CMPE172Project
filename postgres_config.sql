CREATE ROLE django WITH LOGIN PASSWORD 'se172fun';
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC'; 

ALTER ROLE django CREATEDB;
CREATE DATABASE djangoapp;
GRANT ALL PRIVILEGES ON DATABASE djangoapp TO django;

/* 
	you can now login with:
   psql djangoapp -U django
*/

