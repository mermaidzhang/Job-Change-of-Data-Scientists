-- Database: module20

-- DROP DATABASE module20;

CREATE DATABASE module20
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Canada.1252'
    LC_CTYPE = 'English_Canada.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE module20
    IS 'UofT data analytics final project database';