from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

Base = declarative_base()

# Database Models
class CustomerDB(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    location = Column(String)

# Plan Model
class PlanDB(Base):
    __tablename__ = "plans"
    plan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plan_type = Column(String, index=True)

# Application Model
class ApplicationDB(Base):
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_name = Column(String, index=True)

# Location Model
class LocationDB(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    area_name = Column(String, index=True)

# Price Model
class PriceDB(Base):
    __tablename__ = "prices"
    price_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_id = Column(Integer, ForeignKey('applications.application_id'))
    plan_id = Column(Integer, ForeignKey('plans.plan_id'))
    price = Column(Float)

    application = relationship("ApplicationDB", back_populates="prices")
    plan = relationship("PlanDB", back_populates="prices")

# Notification Model
class NotificationDB(Base):
    __tablename__ = "notifications"
    notification_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    notification_type = Column(String, index=True)

# Subscription Model
class SubscriptionDB(Base):
    __tablename__ = "subscriptions"
    sbs_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    location_id = Column(Integer, ForeignKey('locations.location_id'))
    application_id = Column(Integer, ForeignKey('applications.application_id'))
    plan_id = Column(Integer, ForeignKey('plans.plan_id'))
    price_id = Column(Integer, ForeignKey('prices.price_id'))
    notification_id = Column(Integer, ForeignKey('notifications.notification_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    duration = Column(Float)
    device_type = Column(String)

    customer = relationship("CustomerDB", back_populates="subscriptions")
    location = relationship("LocationDB", back_populates="subscriptions")
    application = relationship("ApplicationDB", back_populates="subscriptions")
    plan = relationship("PlanDB", back_populates="subscriptions")
    price = relationship("PriceDB", back_populates="subscriptions")
    notification = relationship("NotificationDB", back_populates="subscriptions")

# Relationships
CustomerDB.subscriptions = relationship("SubscriptionDB", back_populates="customer")
LocationDB.subscriptions = relationship("SubscriptionDB", back_populates="location")
ApplicationDB.prices = relationship("PriceDB", back_populates="application")
ApplicationDB.subscriptions = relationship("SubscriptionDB", back_populates="application")
PlanDB.prices = relationship("PriceDB", back_populates="plan")
PlanDB.subscriptions = relationship("SubscriptionDB", back_populates="plan")
PriceDB.subscriptions = relationship("SubscriptionDB", back_populates="price")
NotificationDB.subscriptions = relationship("SubscriptionDB", back_populates="notification")