from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from flask.ext.login import UserMixin

Base = declarative_base()


# inherit from UserMixin to make sure flask_login works properly
class User(Base, UserMixin):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False, unique=True)
  email = Column(String, nullable=False, unique=True)
  access_token = Column(String(length=128))
  access_token_expire_date = Column(Date)
  access_level = Column(Enum('ADMIN', 'REGULAR_USER', name='access_level'), nullable=False)

  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.access_level = 'REGULAR_USER'

  # required by flask-login to get a string id for the user - we use the users id because that
  # is garenteed to be unique
  def get_id(self):
    return str(self.id)


class Event(Base):
  __tablename__ = 'hours'

  id = Column(Integer, primary_key=True)
  user = Column(Integer, ForeignKey('users.id'), nullable=False)
  title = Column(String, nullable=False)
  description = Column(String, nullable=False)
  hours = Column(Integer, nullable=False)

  def __init__(self, title, description, hours):
    self.title = title
    self.description
    self.hours = hours
