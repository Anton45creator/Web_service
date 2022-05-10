import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db/data.db")
