from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key = True)
  name = Column(String, nullable = False)
  password = Column(String, nullable = False)
  student_id = Column(Integer, nullable = False)

  def __init__ (self, name, password, student_id):
    self.name = name
    self.password = password
    self.student_id = student_id
