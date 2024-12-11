from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base, relationship
from app_components.etl.Database.database import Base, engine

Base = declarative_base()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


class Location(Base):
    """
    Represents a location with an area name.

    Attributes:
        location_id (int): Primary key.
        area_name (str): Unique name of the area.
        subscriptions (list): relationship with subscriptions.
    """
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True, index=True)
    area_name = Column(String, unique=True)

    subscriptions = relationship("Subscription", back_populates="location")


class customer(Base):
    """
    Represents a customer.

    Attributes:
        customer_id (int): Primary key.
        first_name (str): First name of the customer.
        last_name (str): Last name of the customer.
        gender (str): Gender of the customer.
        birth_date (date): Date of birth.
        age (int): Age of the customer.
        location_id (int): Foreign key to location.
        email (str): Unique email address.
        subscriptions (list):  relationship with subscriptions.
    """
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    location_id = Column(Integer, ForeignKey("location.location_id"), nullable=False)
    email = Column(String, unique=True)

    subscriptions = relationship("Subscription", back_populates="customer")


class Plan(Base):
    """
    Represents a subscription plan.

    Attributes:
        plan_id (int): Primary key.
        plan_type (str): Type of the plan.
        prices (list): Associated prices for the plan.
        subscriptions (list):  relationship with subscriptions.
    """
    __tablename__ = "plan"
    plan_id = Column(Integer, primary_key=True, index=True)
    plan_type = Column(String, index=True)

    prices = relationship("Price", back_populates="plan")
    subscriptions = relationship("Subscription", back_populates="plan")


class Application(Base):
    """
    Represents an application.

    Attributes:
        application_id (int): Primary key.
        application_name (str): Name of the application.
        prices (list): Associated prices for the application.
        subscriptions (list): relationship with subscriptions.
    """
    __tablename__ = "application"
    application_id = Column(Integer, primary_key=True, index=True)
    application_name = Column(String, index=True)

    prices = relationship("Price", back_populates="application")
    subscriptions = relationship("Subscription", back_populates="application")


class Price(Base):
    """
    Represents a pricing model.

    Attributes:
        price_id (int): Primary key.
        application_id (int): Foreign key to application.
        plan_id (int): Foreign key to plan.
        price (decimal): Price value.
        application (Application): Associated application.
        plan (Plan): Associated plan.
        subscriptions (list):  relationship with subscriptions.
    """
    __tablename__ = "price"
    price_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("application.application_id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plan.plan_id"), nullable=False)
    price = Column(DECIMAL(10, 2))

    application = relationship("Application", back_populates="prices")
    plan = relationship("Plan", back_populates="prices")
    subscriptions = relationship("Subscription", back_populates="price")


class Notification(Base):
    """
    Represents a notification type.

    Attributes:
        notification_id (int): Primary key.
        notification_type (str): Type of notification.
        subscriptions (list):  relationship with subscriptions.
    """
    __tablename__ = "notification"
    notification_id = Column(Integer, primary_key=True, index=True)
    notification_type = Column(String)

    subscriptions = relationship("Subscription", back_populates="notification")


class Subscription(Base):
    """
    Represents a subscription for a customer.

    Attributes:
        id (int): Primary key.
        customer_id (int): Foreign key to customer.
        location_id (int): Foreign key to location.
        application_id (int): Foreign key to application.
        plan_id (int): Foreign key to plan.
        price_id (int): Foreign key to price.
        notification_id (int): Foreign key to notification.
        start_date (date): Start date of the subscription.
        status (str): Subscription status.
        end_date (date): End date of the subscription.
        duration (decimal): Duration of the subscription.
        device_type (str): Type of device used.

        customer (Customer):  relationship with customer.
        location (Location): relationship with location..
        application (Application):  relationship with application.
        plan (Plan):  relationship with plan.
        price (Price):  relationship with price.
        notification (Notification):  relationship with notification.
    """
    __tablename__ = "subscription"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    location_id = Column(Integer, ForeignKey("location.location_id"), nullable=False)
    application_id = Column(Integer, ForeignKey("application.application_id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plan.plan_id"), nullable=False)
    price_id = Column(Integer, ForeignKey("price.price_id"), nullable=False)
    notification_id = Column(Integer, ForeignKey("notification.notification_id"), nullable=False)
    start_date = Column(Date)
    status = Column(String)
    end_date = Column(Date)
    duration = Column(DECIMAL(10, 2))
    device_type = Column(String)

    customer = relationship("Customer", back_populates="subscriptions")
    location = relationship("Location", back_populates="subscriptions")
    application = relationship("Application", back_populates="subscriptions")
    plan = relationship("Plan", back_populates="subscriptions")
    price = relationship("Price", back_populates="subscriptions")
    notification = relationship("Notification", back_populates="subscriptions")


class Results(Base):
    """
    Represents results for analysis.

    Attributes:
        id (int): Primary key.
        customer_id (int): Foreign key to customer.
        churn_probability (decimal): Probability of churn.
        cluster_number (int): Cluster number.
    """
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    churn_probability = Column(DECIMAL(5, 2))
    cluster_number = Column(Integer)

