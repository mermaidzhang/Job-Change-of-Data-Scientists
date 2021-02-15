# connect and write to DB
from sqlalchemy import create_engine
alchemyEngine           = create_engine('postgresql+psycopg2://postgres:5661MZyx@127.0.0.1', pool_recycle=3600);
postgreSQLConnection    = alchemyEngine.connect();