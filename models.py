from sqlalchemy import *
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from config import *

Base = declarative_base()


class QuizModel(Base):

    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True, unique=True)
    answer = Column(String)
    question = Column(String)
    date_of_creation = Column(DateTime)

    def __repr__(self) -> str:
        return f'\n{self.question} {self.answer}: {self.date_of_creation}'


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)

