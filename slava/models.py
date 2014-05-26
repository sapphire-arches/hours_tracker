from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from flask.ext.login import UserMixin

Base = declarative_base()


# inherit from UserMixin to make sure flask_login works properly
class User(Base, UserMixin):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  student_id = Column(String, nullable=False, unique=True)
  access_level = Column(Enum('ADMIN', 'REGULAR_USER', name='access_level'))

  def __init__(self, name, password, student_id):
    self.name = name
    self.password = password
    self.student_id = student_id

  # get the user id that flask_login will use
  def get_id(self):
    return self.name


class Event(Base):
  __tablename__ = 'hours'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  description = Column(String)
  hours = Column(Integer)

  def __init__(self, title, description, hours):
    self.title = title
    self.description
    self.hours = hours
