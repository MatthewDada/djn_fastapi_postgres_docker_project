import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm 

#creat url for database.py with our docker postgress db setup
DATABASE_URL = "postgresql://dataholic:mypass@localhost:5432/fastapi_database"

# connect to database
engine = _sql.create_engine(DATABASE_URL)

# create a session to enable interaction with database.py
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

#initialize SQLAlchemy databse built in Model.
Base = _declarative.declarative_base()