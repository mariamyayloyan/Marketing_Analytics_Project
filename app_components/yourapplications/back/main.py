from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from models import CustomerDB, PlanDB, ApplicationDB, SubscriptionDB, LocationDB, PriceDB, NotificationDB, ResultsDB  # Import database models # Import database models
from schema import (
    Customer, CustomerCreate,
    Plan, PlanCreate,
    Application, ApplicationCreate,
    Subscription, SubscriptionCreate,
    Location, LocationCreate,
    Price, PriceCreate,
    Notification, NotificationCreate,
    Result, ResultCreate
)
from database import get_db

app = FastAPI(title="FastAPI for Subscription Management")

# CRUD for Customer

# GET Request - Retrieve a customer by ID
@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a customer by their customer ID.

    **Parameters:**
    
    - `customer_id (int):` The unique identifier for the customer.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Customer:` The customer's details.

    **Raises:**
        - `HTTPException: 404` if the customer is not found.
    """
    customer = db.query(CustomerDB).filter(CustomerDB.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# POST Request - Create a new customer
@app.post("/customers/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.

    **Parameters:**
    
    - `customer (CustomerCreate):` The customer data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Customer:` The newly created customer's details.
    """
    db_customer = CustomerDB(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# PUT Request - Update an existing customer
@app.put("/customers/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, updated_customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Update an existing customer by their customer ID.

    **Parameters:**
    
    - `customer_id (int):` The unique identifier for the customer.
    - `updated_customer (CustomerCreate):` The updated customer data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Customer:` The updated customer's details.

    **Raises:**
        - `HTTPException: 404` if the customer is not found.
    """
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
    """
    Delete a customer by their customer ID.

    **Parameters:**
    
    - `customer_id (int):` The unique identifier for the customer.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the customer was deleted.

    **Raises:**
        - `HTTPException: 404` if the customer is not found.
    """
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
    """
    Retrieve a plan by its plan ID.

    **Parameters:**
    
    - `plan_id (int):` The unique identifier for the plan.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Plan:` The plan's details.

    **Raises:**
        - `HTTPException: 404` if the plan is not found.
    """
    plan = db.query(PlanDB).filter(PlanDB.plan_id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

# POST Request - Create a new plan
@app.post("/plans/", response_model=Plan)
async def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    """
    Create a new plan.

    **Parameters:**
    
    - `plan (PlanCreate):` The plan data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Plan:` The newly created plan's details.
    """
    db_plan = PlanDB(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

# PUT Request - Update an existing plan
@app.put("/plans/{plan_id}", response_model=Plan)
async def update_plan(plan_id: int, updated_plan: PlanCreate, db: Session = Depends(get_db)):
    """
    Update an existing plan by its plan ID.

    **Parameters:**
    
    - `plan_id (int):` The unique identifier for the plan.
    - `updated_plan (PlanCreate):` The updated plan data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Plan:` The updated plan's details.

    **Raises:**
        - `HTTPException: 404` if the plan is not found.
    """
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
    """
    Delete a plan by its plan ID.

    **Parameters:**
    
    - `plan_id (int):` The unique identifier for the plan.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the plan was deleted.

    **Raises:**
        - `HTTPException: 404` if the plan is not found.
    """
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
    """
    Retrieve an application by its application ID.

    **Parameters:**
    
    - `application_id (int):` The unique identifier for the application.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Application:` The application's details.

    **Raises:**
        - `HTTPException: 404` if the application is not found.
    """
    application = db.query(ApplicationDB).filter(ApplicationDB.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

# POST Request - Create a new application
@app.post("/applications/", response_model=Application)
async def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    """
    Create a new application.

    **Parameters:**
    
    - `application (ApplicationCreate):` The application data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Application:` The newly created application's details.
    """
    db_application = ApplicationDB(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

# PUT Request - Update an existing application
@app.put("/applications/{application_id}", response_model=Application)
async def update_application(application_id: int, updated_application: ApplicationCreate, db: Session = Depends(get_db)):
    """
    Update an existing application by its application ID.

    **Parameters:**
    
    - `application_id (int):` The unique identifier for the application.
    - `updated_application (ApplicationCreate):` The updated application data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Application:` The updated application's details.

    **Raises:**
        - `HTTPException: 404` if the application is not found.
    """
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
    """
    Delete an application by its application ID.

    **Parameters:**
    
    - `application_id (int):` The unique identifier for the application.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the application was deleted.

    **Raises:**
        - `HTTPException: 404` if the application is not found.
    """
    application = db.query(ApplicationDB).filter(ApplicationDB.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"message": "Application deleted successfully"}

# GET Request - Retrieve a subscription by ID
@app.get("/subscriptions/{sbs_id}", response_model=Subscription)
async def get_subscription(sbs_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a subscription by its subscription ID.

    **Parameters:**
    
    - `sbs_id (int):` The unique identifier for the subscription.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Subscription:` The subscription's details.

    **Raises:**
        - `HTTPException: 404` if the subscription is not found.
    """
    subscription = db.query(SubscriptionDB).filter(SubscriptionDB.sbs_id == sbs_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

# POST Request - Create a new subscription
@app.post("/subscriptions/", response_model=Subscription)
async def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    """
    Create a new subscription.

    **Parameters:**
    
    - `subscription (SubscriptionCreate):` The subscription data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Subscription:` The newly created subscription's details.
    """
    db_subscription = SubscriptionDB(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

# PUT Request - Update an existing subscription
@app.put("/subscriptions/{sbs_id}", response_model=Subscription)
async def update_subscription(sbs_id: int, updated_subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    """
    Update an existing subscription identified by its subscription ID.

    **Parameters:**
    
    - `sbs_id (int):` The unique identifier for the subscription.
    - `updated_subscription (SubscriptionCreate):` The updated subscription data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Subscription:` The updated subscription's details.

    **Raises:**
        - `HTTPException: 404` if the subscription is not found.
    """
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
    """
    Delete a subscription by its subscription ID.

    **Parameters:**
    
    - `sbs_id (int):` The unique identifier for the subscription.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the subscription was deleted.

    **Raises:**
        - `HTTPException: 404` if the subscription is not found.
    """
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
    """
    Retrieve a location by its location ID.

    **Parameters:**
    
    - `location_id (int):` The unique identifier for the location.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Location:` The location's details.

    **Raises:**
        - `HTTPException: 404` if the location is not found.
    """
    location = db.query(LocationDB).filter(LocationDB.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

# POST Request - Create a new location
@app.post("/locations/", response_model=Location)
async def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    """
    Create a new location.

    **Parameters:**
    
    - `location (LocationCreate):` The location data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Location:` The newly created location's details.
    """
    db_location = LocationDB(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# PUT Request - Update an existing location
@app.put("/locations/{location_id}", response_model=Location)
async def update_location(location_id: int, updated_location: LocationCreate, db: Session = Depends(get_db)):
    """
    Update an existing location identified by its location ID.

    **Parameters:**
    
    - `location_id (int):` The unique identifier for the location.
    - `updated_location (LocationCreate):` The updated location data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Location:` The updated location's details.

    **Raises:**
        - `HTTPException: 404` if the location is not found.
    """
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
    """
    Delete a location by its location ID.

    **Parameters:**
    
    - `location_id (int):` The unique identifier for the location.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the location was deleted.

    **Raises:**
        - `HTTPException: 404` if the location is not found.
    """
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
    """
    Retrieve a price by its price ID.

    **Parameters:**
    
    - `price_id (int):` The unique identifier for the price.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Price:` The price's details.

    **Raises:**
        - `HTTPException: 404` if the price is not found.
    """
    price = db.query(PriceDB).filter(PriceDB.price_id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    return price

# POST Request - Create a new price
@app.post("/prices/", response_model=Price)
async def create_price(price: PriceCreate, db: Session = Depends(get_db)):
    """
    Create a new price.

    **Parameters:**
    
    - `price (PriceCreate):` The price data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Price:` The newly created price's details.
    """
    db_price = PriceDB(**price.dict())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

# PUT Request - Update an existing price
@app.put("/prices/{price_id}", response_model=Price)
async def update_price(price_id: int, updated_price: PriceCreate, db: Session = Depends(get_db)):
    """
    Update an existing price identified by its price ID.

    **Parameters:**
    
    - `price_id (int):` The unique identifier for the price.
    - `updated_price (PriceCreate):` The updated price data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Price:` The updated price's details.

    **Raises:**
        - `HTTPException: 404` if the price is not found.
    """
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
    """
    Delete a price by its price ID.

    **Parameters:**
    
    - `price_id (int):` The unique identifier for the price.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the price was deleted.

    **Raises:**
        - `HTTPException: 404` if the price is not found.
    """
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
    """
    Retrieve a notification by its notification ID.

    **Parameters:**
    
    - `notification_id (int):` The unique identifier for the notification.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Notification:` The notification's details.

    **Raises:**
        - `HTTPException: 404` if the notification is not found.
    """
    notification = db.query(NotificationDB).filter(NotificationDB.notification_id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

# POST Request - Create a new notification
@app.post("/notifications/", response_model=Notification)
async def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    """
    Create a new notification.

    **Parameters:**
    
    - `notification (NotificationCreate):` The notification data to create.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Notification:` The newly created notification's details.
    """
    db_notification = NotificationDB(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

# PUT Request - Update an existing notification
@app.put("/notifications/{notification_id}", response_model=Notification)
async def update_notification(notification_id: int, updated_notification: NotificationCreate, db: Session = Depends(get_db)):
    """
    Update an existing notification identified by its notification ID.

    **Parameters:**
    
    - `notification_id (int):` The unique identifier for the notification.
    - `updated_notification (NotificationCreate):` The updated notification data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Notification:` The updated notification's details.

    **Raises:**
        - `HTTPException: 404` if the notification is not found.
    """
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
    """
    Delete a notification by its notification ID.

    **Parameters:**
    
    - `notification_id (int):` The unique identifier for the notification.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the notification was deleted.

    **Raises:**
        - `HTTPException: 404` if the notification is not found.
    """
    notification = db.query(NotificationDB).filter(NotificationDB.notification_id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(notification)
    db.commit()
    return {"message": "Notification deleted successfully"}

# GET Request - Retrieve results for a specific customer by customer ID
@app.get("/customers/{customer_id}/results", response_model=List[Result])
async def get_results_by_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve processed results for a specific customer by their customer ID.

    **Parameters:**
    
    - `customer_id (int):` The unique identifier for the customer.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `List[Result]:` A list of results associated with the given customer.

    **Raises:**
        - `HTTPException: 404` if no results are found for the customer.
    """
    results = db.query(ResultsDB).filter(ResultsDB.customer_id == customer_id).all()
    if not results:
        raise HTTPException(status_code=404, detail="Results not found for the customer")
    return results

# GET Request - Retrieve a result by result ID
@app.get("/results/{result_id}", response_model=Result)
async def get_result_by_id(result_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific result entry by its result ID.

    **Parameters:**
    
    - `result_id (int):` The unique identifier for the result.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Result:` The details of the result with the given `result_id`.

    **Raises:**
        - `HTTPException: 404` if the result with the provided ID is not found.
    """
    result = db.query(ResultsDB).filter(ResultsDB.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    return result

# POST Request - Create a new result entry
@app.post("/results/", response_model=Result)
async def create_result(result: ResultCreate, db: Session = Depends(get_db)):
    """
    Create a new result entry for a customer with churn probability and cluster information.

    **Parameters:**
    
    - `result (ResultCreate):` The data for the new result.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Result:` The newly created result's details.

    **Raises:**
        - `HTTPException: 400` if the data cannot be processed.
    """
    db_result = ResultsDB(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

# PUT Request - Update an existing result by result ID
@app.put("/results/{result_id}", response_model=Result)
async def update_result(result_id: int, updated_result: ResultCreate, db: Session = Depends(get_db)):
    """
    Update an existing result entry identified by its result ID.

    **Parameters:**
    
    - `result_id (int):` The unique identifier for the result to update.
    - `updated_result (ResultCreate):` The updated result data.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `Result:` The updated result's details.

    **Raises:**
        - `HTTPException: 404` if the result with the provided ID is not found.
    """
    result = db.query(ResultsDB).filter(ResultsDB.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    for key, value in updated_result.model_dump().items():
        setattr(result, key, value)
    db.commit()
    db.refresh(result)
    return result

# DELETE Request - Delete a result by result ID
@app.delete("/results/{result_id}")
async def delete_result(result_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific result entry identified by its result ID.

    **Parameters:**
    
    - `result_id (int):` The unique identifier for the result to delete.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `message (str):` A success message confirming the result was deleted.

    **Raises:**
        - `HTTPException: 404` if the result with the provided ID is not found.
    """
    result = db.query(ResultsDB).filter(ResultsDB.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    db.delete(result)
    db.commit()
    return {"message": "Result deleted successfully"}

# GET Request - Retrieve users filtered by churn probability or cluster number
@app.get("/users/segmented/", response_model=List[Customer])
async def get_users_by_segment(
    churn_probability: Optional[float] = Query(None, ge=0.0, le=1.0),
    cluster_number: Optional[int] = None,
    db: Session = Depends(get_db),
):
    """
    Retrieve users filtered by churn probability or cluster number based on segmentation data.

    **Parameters:**
    
    - `churn_probability (float, optional):` A filter for churn probability (between 0.0 and 1.0).
    - `cluster_number (int, optional):` A filter for the segmentation cluster number.
    - `db (Session, optional):` Database session provided by dependency injection.

    **Returns:**
        - `List[Customer]:` A list of customers that match the provided segmentation criteria.

    **Raises:**
        - `HTTPException: 404` if no users match the filtering criteria.
    """
    query = db.query(CustomerDB).join(ResultsDB, CustomerDB.customer_id == ResultsDB.customer_id)

    if churn_probability is not None:
        query = query.filter(ResultsDB.churn_probability >= churn_probability)

    if cluster_number is not None:
        query = query.filter(ResultsDB.cluster_number == cluster_number)

    users = query.all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found matching the criteria.")
    return users
