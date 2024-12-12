from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base, relationship
from Database.database import Base, engine

Base = declarative_base()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

class Location(Base):
    """
    Represents a location entity in the database.

    Attributes:
        location_id (int): Primary key for the location table.
        area_name (str): Name of the geographical area.
        subscriptions (list): Relationship to the subscriptions associated with the location.
    """
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True, index=True)
    area_name = Column(String)

    subscriptions = relationship("Subscription", back_populates="location")


class Customer(Base):
    """
    Represents a customer entity in the database.

    Attributes:
        customer_id (int): Primary key for the customer table.
        first_name (str): First name of the customer.
        last_name (str): Last name of the customer.
        gender (str): Gender of the customer.
        birth_date (date): Date of birth of the customer.
        age (int): Age of the customer.
        location (str): Foreign key to the `Location` table.
    """
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    location = Column(String, ForeignKey("location.area_name"))


class Plan(Base):
    """
    Represents a subscription plan entity in the database.

    Attributes:
        plan_id (int): Primary key for the plan table.
        plan_type (str): Type of the subscription plan (e.g., basic, premium).
        subscriptions (list): Relationship to subscriptions associated with the plan.
    """
    __tablename__ = "plan"
    plan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plan_type = Column(String, index=True)
    subscriptions = relationship("Subscription", back_populates="plan")


class Application(Base):
    """
    Represents an application entity in the database.

    Attributes:
        app_id (int): Primary key for the application table.
        application_name (str): Name of the application.
        subscriptions (list): Relationship to subscriptions associated with the application.
    """
    __tablename__ = "application"
    app_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    application_name = Column(String, index=True)
    subscriptions = relationship("Subscription", back_populates="application")


class Price(Base):
    """
    Represents pricing details for subscription plans and applications.

    Attributes:
        price_id (int): Primary key for the price table.
        application_id (int): Foreign key to the `Application` table.
        plan_id (int): Foreign key to the `Plan` table.
        price (decimal): Price of the subscription.
        subscriptions (list): Relationship to subscriptions associated with this price.
        application (Application): Relationship to the application associated with this price.
        plan (Plan): Relationship to the plan associated with this price.
    """
    __tablename__ = "price"
    price_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("application.application_id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plan.plan_id"), nullable=False)
    price = Column(DECIMAL)
    subscriptions = relationship("Subscription", back_populates="price")
    application = relationship("Application", back_populates="prices")
    plan = relationship("Plan", back_populates="prices")


class Notification(Base):
    """
    Represents a notification type entity in the database.

    Attributes:
        notification_id (int): Primary key for the notification table.
        notification_type (str): Type of notification (e.g., email, SMS).
        subscriptions (list): Relationship to subscriptions associated with the notification.
    """
    __tablename__ = "notification"
    notification_id = Column(Integer, primary_key=True, index=True)
    notification_type = Column(String)

    subscriptions = relationship("Subscription", back_populates="notification")
    Application.prices = relationship("Price", back_populates="application")
    Plan.prices = relationship("Price", back_populates="plan")


class Subscription(Base):
    """
    Represents a subscription entity in the database.

    Attributes:
        id (int): Primary key for the subscription table.
        customer_id (int): Foreign key to the `Customer` table.
        location_id (int): Foreign key to the `Location` table.
        application_id (int): Foreign key to the `Application` table.
        plan_type_id (int): Foreign key to the `Plan` table.
        price_id (int): Foreign key to the `Price` table.
        notification_id (int): Foreign key to the `Notification` table.
        start_date (date): Start date of the subscription.
        status (str): Status of the subscription (e.g., active, canceled).
        end_date (date): End date of the subscription.
        duration (decimal): Duration of the subscription in days.
        device_type (str): Type of device associated with the subscription.
    """
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

class Results(Base):
    """
    Represents analysis results for customer churn.

    Attributes:
        id (int): Primary key for the results table.
        customer_id (int): Foreign key to the `Customer` table.
        churn_probability (decimal): Probability of customer churn.
        cluster_number (int): Cluster identifier for customer segmentation.
    """
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    churn_probability = Column(DECIMAL(5, 2))
    cluster_number = Column(Integer)
