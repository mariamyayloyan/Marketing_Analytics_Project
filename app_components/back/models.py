"""
Database Models for the ETL Process.

This module defines the database models using SQLAlchemy for customers, subscriptions, plans, 
applications, locations, prices, notifications, subscriptions and prediction results.

Modules:
    - sqlalchemy: For ORM and database schema definition.
    - pydantic: For data validation (not used in these models).
"""
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DECIMAL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

Base = declarative_base()

# Database Models
class CustomerDB(Base):
    """
    Represents a Customer in the database.

    **Attributes:**
    
    - `customer_id (int):` The unique identifier for the customer (auto-incremented).
    - `first_name (str):` The first name of the customer.
    - `last_name (str):` The last name of the customer.
    - `gender (str):` The gender of the customer.
    - `birth_date (date):` The birth date of the customer.
    - `age (int):` The age of the customer.
    - `location (str):` The location or address of the customer.
    """
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
    """
    Represents a Subscription Plan in the database.

    **Attributes:**
    
    - `plan_id (int):` The unique identifier for the plan (auto-incremented).
    - `plan_type (str):` The type or category of the plan.
    """
    __tablename__ = "plans"
    plan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plan_type = Column(String, index=True)

# Application Model
class ApplicationDB(Base):
    """
    Represents an Application in the database.

    **Attributes:**
    
    - `application_id (int):` The unique identifier for the application (auto-incremented).
    - `application_name (str):` The name of the application.
    """
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_name = Column(String, index=True)

# Location Model
class LocationDB(Base):
    """
    Represents a Location in the database.

    **Attributes:**
    
    - `location_id (int):` The unique identifier for the location (auto-incremented).
    - `area_name (str):` The name of the geographical area or location.
    """
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    area_name = Column(String, index=True)

# Price Model
class PriceDB(Base):
    """
    Represents a Price in the database.

    **Attributes:**
    
    - `price_id (int):` The unique identifier for the price (auto-incremented).
    - `application_id (int):` The foreign key reference to the `applications` table.
    - `plan_id (int):` The foreign key reference to the `plans` table.
    - `price (float):` The price value for the application-plan combination.
    
    **Relationships:**
    
    - `application (ApplicationDB):` The application associated with this price.
    - `plan (PlanDB):` The subscription plan associated with this price.
    """
    __tablename__ = "prices"
    price_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_id = Column(Integer, ForeignKey('applications.application_id'))
    plan_id = Column(Integer, ForeignKey('plans.plan_id'))
    price = Column(Float)

    application = relationship("ApplicationDB", back_populates="prices")
    plan = relationship("PlanDB", back_populates="prices")

# Notification Model
class NotificationDB(Base):
    """
    Represents a Notification in the database.

    **Attributes:**
    
    - `notification_id (int):` The unique identifier for the notification (auto-incremented).
    - `notification_type (str):` The type or category of the notification.
    """
    __tablename__ = "notifications"
    notification_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    notification_type = Column(String, index=True)

# Subscription Model
class SubscriptionDB(Base):
    """
    Represents a Subscription in the database.

    **Attributes:**
    
    - `sbs_id (int):` The unique identifier for the subscription (auto-incremented).
    - `customer_id (int):` The foreign key reference to the `customers` table.
    - `location_id (int):` The foreign key reference to the `locations` table.
    - `application_id (int):` The foreign key reference to the `applications` table.
    - `plan_id (int):` The foreign key reference to the `plans` table.
    - `price_id (int):` The foreign key reference to the `prices` table.
    - `notification_id (int):` The foreign key reference to the `notifications` table.
    - `start_date (date):` The start date of the subscription.
    - `end_date (date):` The end date of the subscription.
    - `status (str):` The status of the subscription.
    - `duration (float):` The duration of the subscription.
    - `device_type (str):` The type of device used for the subscription.
    
    **Relationships:**
    
    - `customer (CustomerDB):` The customer associated with this subscription.
    - `location (LocationDB):` The location where the subscription was made.
    - `application (ApplicationDB):` The application associated with this subscription.
    - `plan (PlanDB):` The plan associated with this subscription.
    - `price (PriceDB):` The price associated with this subscription.
    - `notification (NotificationDB):` The notification associated with this subscription.
    """
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

#Results Model
class ResultsDB(Base):
    """
    Represents the Results of churn probability prediction and customer segmentation in the database.

    **Attributes:**
    
    - `id (int):` The unique identifier for the result (auto-incremented).
    - `customer_id (int):` The foreign key reference to the `customers` table.
    - `churn_probability (decimal):` The predicted probability that the customer will churn.
    - `cluster_number (int):` The assigned cluster number for the customer based on segmentation.
    
    **Relationships:**
    
    - `customer (CustomerDB):` The customer associated with this result.
    """
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id", ondelete="CASCADE"))
    churn_probability = Column(DECIMAL(5, 2))
    cluster_number = Column(Integer)



# Relationships
CustomerDB.subscriptions = relationship("SubscriptionDB", back_populates="customer")
LocationDB.subscriptions = relationship("SubscriptionDB", back_populates="location")
ApplicationDB.prices = relationship("PriceDB", back_populates="application")
ApplicationDB.subscriptions = relationship("SubscriptionDB", back_populates="application")
PlanDB.prices = relationship("PriceDB", back_populates="plan")
PlanDB.subscriptions = relationship("SubscriptionDB", back_populates="plan")
PriceDB.subscriptions = relationship("SubscriptionDB", back_populates="price")
NotificationDB.subscriptions = relationship("SubscriptionDB", back_populates="notification")
CustomerDB.results = relationship("ResultsDB", back_populates="customer", cascade="all, delete")
ResultsDB.customer = relationship("CustomerDB", back_populates="results")