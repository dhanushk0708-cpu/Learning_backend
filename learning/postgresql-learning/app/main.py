from sqlalchemy import text

from database import engine

with engine.connect() as connection:
    result = connection.execute(text("SELECT current_database()"))
    database_name = result.scalar()

    print("Connected to:", database_name)