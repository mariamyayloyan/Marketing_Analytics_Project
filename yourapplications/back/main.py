from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import CustomerDB, PlanDB, ApplicationDB, SubscriptionDB, LocationDB, PriceDB, NotificationDB  # Import database models # Import database models
from schema import (
    Customer, CustomerCreate,
    Plan, PlanCreate,
    Application, ApplicationCreate,
    Subscription, SubscriptionCreate,
    Location, LocationCreate,
    Price, PriceCreate,
    Notification, NotificationCreate,
)
from database import get_db

app = FastAPI(title="FastAPI for Subscription Management")

# CRUD for Customer

# GET Request - Retrieve a customer by ID
@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# POST Request - Create a new customer
@app.post("/customers/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = CustomerDB(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# PUT Request - Update an existing customer
@app.put("/customers/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, updated_customer: CustomerCreate, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in updated_customer.dict().items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

# DELETE Request - Delete a customer by ID
@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}

# CRUD for Plan

# GET Request - Retrieve a plan by ID
@app.get("/plans/{plan_id}", response_model=Plan)
async def get_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(PlanDB).filter(PlanDB.plan_id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

# POST Request - Create a new plan
@app.post("/plans/", response_model=Plan)
async def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    db_plan = PlanDB(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

# PUT Request - Update an existing plan
@app.put("/plans/{plan_id}", response_model=Plan)
async def update_plan(plan_id: int, updated_plan: PlanCreate, db: Session = Depends(get_db)):
    plan = db.query(PlanDB).filter(PlanDB.plan_id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    for key, value in updated_plan.dict().items():
        setattr(plan, key, value)
    db.commit()
    db.refresh(plan)
    return plan

# DELETE Request - Delete a plan by ID
@app.delete("/plans/{plan_id}")
async def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(PlanDB).filter(PlanDB.plan_id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    db.delete(plan)
    db.commit()
    return {"message": "Plan deleted successfully"}

# CRUD for Application

# GET Request - Retrieve an application by ID
@app.get("/applications/{application_id}", response_model=Application)
async def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(ApplicationDB).filter(ApplicationDB.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

# POST Request - Create a new application
@app.post("/applications/", response_model=Application)
async def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    db_application = ApplicationDB(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

# PUT Request - Update an existing application
@app.put("/applications/{application_id}", response_model=Application)
async def update_application(application_id: int, updated_application: ApplicationCreate, db: Session = Depends(get_db)):
    application = db.query(ApplicationDB).filter(ApplicationDB.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    for key, value in updated_application.dict().items():
        setattr(application, key, value)
    db.commit()
    db.refresh(application)
    return application

# DELETE Request - Delete an application by ID
@app.delete("/applications/{application_id}")
async def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(ApplicationDB).filter(ApplicationDB.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"message": "Application deleted successfully"}

# GET Request - Retrieve a subscription by ID
@app.get("/subscriptions/{sbs_id}", response_model=Subscription)
async def get_subscription(sbs_id: int, db: Session = Depends(get_db)):
    subscription = db.query(SubscriptionDB).filter(SubscriptionDB.sbs_id == sbs_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

# POST Request - Create a new subscription
@app.post("/subscriptions/", response_model=Subscription)
async def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = SubscriptionDB(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

# PUT Request - Update an existing subscription
@app.put("/subscriptions/{sbs_id}", response_model=Subscription)
async def update_subscription(sbs_id: int, updated_subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    subscription = db.query(SubscriptionDB).filter(SubscriptionDB.sbs_id == sbs_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    for key, value in updated_subscription.dict().items():
        setattr(subscription, key, value)
    db.commit()
    db.refresh(subscription)
    return subscription

# DELETE Request - Delete a subscription by ID
@app.delete("/subscriptions/{sbs_id}")
async def delete_subscription(sbs_id: int, db: Session = Depends(get_db)):
    subscription = db.query(SubscriptionDB).filter(SubscriptionDB.sbs_id == sbs_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    db.delete(subscription)
    db.commit()
    return {"message": "Subscription deleted successfully"}

# CRUD for Location

# GET Request - Retrieve a location by ID
@app.get("/locations/{location_id}", response_model=Location)
async def get_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(LocationDB).filter(LocationDB.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

# POST Request - Create a new location
@app.post("/locations/", response_model=Location)
async def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    db_location = LocationDB(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# PUT Request - Update an existing location
@app.put("/locations/{location_id}", response_model=Location)
async def update_location(location_id: int, updated_location: LocationCreate, db: Session = Depends(get_db)):
    location = db.query(LocationDB).filter(LocationDB.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    for key, value in updated_location.dict().items():
        setattr(location, key, value)
    db.commit()
    db.refresh(location)
    return location

# DELETE Request - Delete a location by ID
@app.delete("/locations/{location_id}")
async def delete_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(LocationDB).filter(LocationDB.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(location)
    db.commit()
    return {"message": "Location deleted successfully"}

# CRUD for Price

# GET Request - Retrieve a price by ID
@app.get("/prices/{price_id}", response_model=Price)
async def get_price(price_id: int, db: Session = Depends(get_db)):
    price = db.query(PriceDB).filter(PriceDB.price_id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    return price

# POST Request - Create a new price
@app.post("/prices/", response_model=Price)
async def create_price(price: PriceCreate, db: Session = Depends(get_db)):
    db_price = PriceDB(**price.dict())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

# PUT Request - Update an existing price
@app.put("/prices/{price_id}", response_model=Price)
async def update_price(price_id: int, updated_price: PriceCreate, db: Session = Depends(get_db)):
    price = db.query(PriceDB).filter(PriceDB.price_id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    for key, value in updated_price.dict().items():
        setattr(price, key, value)
    db.commit()
    db.refresh(price)
    return price

# DELETE Request - Delete a price by ID
@app.delete("/prices/{price_id}")
async def delete_price(price_id: int, db: Session = Depends(get_db)):
    price = db.query(PriceDB).filter(PriceDB.price_id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    db.delete(price)
    db.commit()
    return {"message": "Price deleted successfully"}

# CRUD for Notification

# GET Request - Retrieve a notification by ID
@app.get("/notifications/{notification_id}", response_model=Notification)
async def get_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(NotificationDB).filter(NotificationDB.notification_id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

# POST Request - Create a new notification
@app.post("/notifications/", response_model=Notification)
async def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    db_notification = NotificationDB(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

# PUT Request - Update an existing notification
@app.put("/notifications/{notification_id}", response_model=Notification)
async def update_notification(notification_id: int, updated_notification: NotificationCreate, db: Session = Depends(get_db)):
    notification = db.query(NotificationDB).filter(NotificationDB.notification_id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    for key, value in updated_notification.dict().items():
        setattr(notification, key, value)
    db.commit()
    db.refresh(notification)
    return notification

# DELETE Request - Delete a notification by ID
@app.delete("/notifications/{notification_id}")
async def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(NotificationDB).filter(NotificationDB.notification_id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(notification)
    db.commit()
    return {"message": "Notification deleted successfully"}