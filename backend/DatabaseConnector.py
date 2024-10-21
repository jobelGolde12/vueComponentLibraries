from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.UserTable import Base as userCredential
from database.TemplateTable import Base as templateData

LOCAL_DB_URL = ''
ONLINE_DB_URL = ''

def create_session(engine_url):
    engine = create_engine(engine_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        userCredential.metadata.create_all(engine)
        templateData.metadata.create_all(engine)
        print(f"Successfully connected to the database at {engine_url}")
        return session
    except Exception as e:
        print(f"Error connecting to database or creating tables at {engine_url}: {e}")
        return None

def db_conn():
    session = create_session(LOCAL_DB_URL)
    if not session:
        session = create_session(ONLINE_DB_URL) 
    return session
