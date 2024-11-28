from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, Date, String, ForeignKey, DECIMAL
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.orm import declarative_base
Base = declarative_base()

from yourapplications.etl.Database.database import *
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


class Location(Base):
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True, index=True)
    area_name = Column(String, unique = True)

    subscriptions = relationship("Subscription", back_populates="location")

class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    location = Column(String, ForeignKey("location.area_name"))


class Plan(Base):
    __tablename__ = "plan"
    plan_id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    plan_type = Column(String, index=True)
    subscriptions = relationship("Subscription", back_populates="plan")


class Application(Base):
    __tablename__ = "application"
    application_id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    application_name = Column(String, index=True)
    subscriptions = relationship("Subscription", back_populates="application")


class Price(Base):
    __tablename__ = "price"
    price_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("application.application_id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plan.plan_id"), nullable=False)
    price = Column(DECIMAL)
    subscriptions = relationship("Subscription", back_populates="price")
    application = relationship("Application", back_populates="prices")
    plan = relationship("Plan", back_populates="prices")

class Notification(Base):
    __tablename__ = "notification"
    notification_id = Column(Integer, primary_key=True, index=True)
    notification_type = Column(String)

    subscriptions = relationship("Subscription", back_populates="notification")
    Application.prices = relationship("Price", back_populates="application")
    Plan.prices = relationship("Price", back_populates="plan")

class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    location_id = Column(Integer, ForeignKey("location.location_id"), nullable=False)
    application_id = Column(Integer, ForeignKey("application.application_id"), nullable=False)
    plan_type_id = Column(Integer, ForeignKey("plan.plan_id"), nullable=False)
    price_id = Column(Integer, ForeignKey("price.price_id"), nullable=False)
    notification_id = Column(Integer, ForeignKey("notification.notification_id"), nullable=False)
    start_date = Column(Date)
    status = Column(String)
    end_date = Column(Date)
    duration = Column(DECIMAL)
    device_type = Column(String)

    customer = relationship("Customer", back_populates="subscriptions")
    location = relationship("Location", back_populates="subscriptions")
    application = relationship("Application", back_populates="subscriptions")
    plan = relationship("Plan", back_populates="subscriptions")
    price = relationship("Price", back_populates="subscriptions")
    notification = relationship("Notification", back_populates="subscriptions")

