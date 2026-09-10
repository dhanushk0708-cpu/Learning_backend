from database import engine


with engine.connect() as connection:
    print("PostgreSQL connection successful")