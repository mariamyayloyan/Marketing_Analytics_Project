from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Customer Pydantic Models
class Customer(BaseModel):
    customer_id: int  # Auto-generated by the DB
    first_name: str
    last_name: str
    gender: Optional[str]
    birth_date: Optional[date]
    age: Optional[int]
    location: Optional[str]

    class Config:
        orm_mode = True  # Enable compatibility with SQLAlchemy models

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    gender: Optional[str]
    birth_date: Optional[date]
    age: Optional[int]
    location: Optional[str]

# Plan Pydantic Models
class Plan(BaseModel):
    plan_id: int  # Auto-generated by the DB
    plan_type: str

    class Config:
        orm_mode = True

class PlanCreate(BaseModel):
    plan_type: str

# Application Pydantic Models
class Application(BaseModel):
    application_id: int  # Auto-generated by the DB
    application_name: str

    class Config:
        orm_mode = True

class ApplicationCreate(BaseModel):
    application_name: str

# Location Pydantic Models
class Location(BaseModel):
    location_id: int  # Auto-generated by the DB
    area_name: str

    class Config:
        orm_mode = True

class LocationCreate(BaseModel):
    area_name: str

# Price Pydantic Models
class Price(BaseModel):
    price_id: int  # Auto-generated by the DB
    application_id: int
    plan_id: int
    price: float

    class Config:
        orm_mode = True

class PriceCreate(BaseModel):
    application_id: int
    plan_id: int
    price: float

# Notification Pydantic Models
class Notification(BaseModel):
    notification_id: int  # Auto-generated by the DB
    notification_type: str

    class Config:
        orm_mode = True

class NotificationCreate(BaseModel):
    notification_type: str

# Subscription Pydantic Models
class Subscription(BaseModel):
    sbs_id: int  # Auto-generated by the DB
    customer_id: int
    location_id: int
    application_id: int
    plan_id: int
    price_id: int
    notification_id: Optional[int]
    start_date: date
    end_date: Optional[date]
    status: str
    duration: Optional[float]
    device_type: Optional[str]

    class Config:
        orm_mode = True

class SubscriptionCreate(BaseModel):
    customer_id: int
    location_id: int
    application_id: int
    plan_id: int
    price_id: int
    notification_id: Optional[int]
    start_date: date
    end_date: Optional[date]
    status: str
    duration: Optional[float]
    device_type: Optional[str]
