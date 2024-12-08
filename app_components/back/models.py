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
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    location = Column(String)

    # Relationships
    subscriptions = relationship("SubscriptionDB", back_populates="customer", cascade="all, delete")
    results = relationship("ResultsDB", back_populates="customer", cascade="all, delete")


class PlanDB(Base):
    """
    Represents a Subscription Plan in the database.

    **Attributes:**
    - `plan_id (int):` The unique identifier for the plan (auto-incremented).
    - `plan_type (str):` The type or category of the plan.
    """
    __tablename__ = "plan"
    plan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plan_type = Column(String, index=True)

    # Relationships
    subscriptions = relationship("SubscriptionDB", back_populates="plan")
    prices = relationship("PriceDB", back_populates="plan")


class ApplicationDB(Base):
    """
    Represents an Application in the database.

    **Attributes:**
    - `application_id (int):` The unique identifier for the application (auto-incremented).
    - `application_name (str):` The name of the application.
    """
    __tablename__ = "application"
    application_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_name = Column(String, index=True)

    # Relationships
    prices = relationship("PriceDB", back_populates="application")
    subscriptions = relationship("SubscriptionDB", back_populates="application")


class LocationDB(Base):
    """
    Represents a Location in the database.

    **Attributes:**
    - `location_id (int):` The unique identifier for the location (auto-incremented).
    - `area_name (str):` The name of the geographical area or location.
    """
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    area_name = Column(String, index=True)

    # Relationships
    subscriptions = relationship("SubscriptionDB", back_populates="location")


class PriceDB(Base):
    """
    Represents a Price in the database.

    **Attributes:**
    - `price_id (int):` The unique identifier for the price (auto-incremented).
    - `application_id (int):` The foreign key reference to the `application` table.
    - `plan_id (int):` The foreign key reference to the `plan` table.
    - `price (float):` The price value for the application-plan combination.
    """
    __tablename__ = "price"
    price_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_id = Column(Integer, ForeignKey('application.application_id'))
    plan_id = Column(Integer, ForeignKey('plan.plan_id'))
    price = Column(Float)

    # Relationships
    application = relationship("ApplicationDB", back_populates="prices")
    plan = relationship("PlanDB", back_populates="prices")
    subscriptions = relationship("SubscriptionDB", back_populates="price")


class NotificationDB(Base):
    """
    Represents a Notification in the database.

    **Attributes:**
    - `notification_id (int):` The unique identifier for the notification (auto-incremented).
    - `notification_type (str):` The type or category of the notification.
    """
    __tablename__ = "notification"
    notification_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    notification_type = Column(String, index=True)

    # Relationships
    subscriptions = relationship("SubscriptionDB", back_populates="notification")


class SubscriptionDB(Base):
    """
    Represents a Subscription in the database.

    **Attributes:**
    - `sbs_id (int):` The unique identifier for the subscription (auto-incremented).
    - `customer_id (int):` The foreign key reference to the `customer` table.
    - `location_id (int):` The foreign key reference to the `location` table.
    - `application_id (int):` The foreign key reference to the `application` table.
    - `plan_id (int):` The foreign key reference to the `plan` table.
    - `price_id (int):` The foreign key reference to the `price` table.
    - `notification_id (int):` The foreign key reference to the `notification` table.
    - `start_date (date):` The start date of the subscription.
    - `end_date (date):` The end date of the subscription.
    - `status (str):` The status of the subscription.
    - `duration (float):` The duration of the subscription.
    - `device_type (str):` The type of device used for the subscription.
    """
    __tablename__ = "subscription"
    sbs_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    location_id = Column(Integer, ForeignKey('location.location_id'))
    application_id = Column(Integer, ForeignKey('application.application_id'))
    plan_id = Column(Integer, ForeignKey('plan.plan_id'))
    price_id = Column(Integer, ForeignKey('price.price_id'))
    notification_id = Column(Integer, ForeignKey('notification.notification_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    duration = Column(Float)
    device_type = Column(String)

    # Relationships
    customer = relationship("CustomerDB", back_populates="subscriptions")
    location = relationship("LocationDB", back_populates="subscriptions")
    application = relationship("ApplicationDB", back_populates="subscriptions")
    plan = relationship("PlanDB", back_populates="subscriptions")
    price = relationship("PriceDB", back_populates="subscriptions")
    notification = relationship("NotificationDB", back_populates="subscriptions")


class ResultsDB(Base):
    """
    Represents the Results of churn probability prediction and customer segmentation in the database.

    **Attributes:**
    - `id (int):` The unique identifier for the result (auto-incremented).
    - `customer_id (int):` The foreign key reference to the `customer` table.
    - `churn_probability (decimal):` The predicted probability that the customer will churn.
    - `cluster_number (int):` The assigned cluster number for the customer based on segmentation.
    
    **Relationships:**
    - `customer (CustomerDB):` The customer associated with this result.
    """
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id", ondelete="CASCADE"))
    churn_probability = Column(DECIMAL(5, 2))
    cluster_number = Column(Integer)

    # Relationship
    customer = relationship("CustomerDB", back_populates="results")

# Relationships
CustomerDB.subscriptions = relationship("SubscriptionDB", back_populates="customer", cascade="all, delete")
LocationDB.subscriptions = relationship("SubscriptionDB", back_populates="location")
ApplicationDB.subscriptions = relationship("SubscriptionDB", back_populates="application")
PlanDB.subscriptions = relationship("SubscriptionDB", back_populates="plan")
PriceDB.subscriptions = relationship("SubscriptionDB", back_populates="price")
NotificationDB.subscriptions = relationship("SubscriptionDB", back_populates="notification")
CustomerDB.results = relationship("ResultsDB", back_populates="customer", cascade="all, delete")
