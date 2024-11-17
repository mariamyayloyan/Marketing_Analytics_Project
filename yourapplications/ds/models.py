import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

script_dir = os.path.dirname(os.path.abspath(__file__))

base_dir = os.path.join(script_dir, "..", "etl", "Data")

customer = pd.read_csv(os.path.join(base_dir, "customer.csv"))
plan = pd.read_csv(os.path.join(base_dir, "plan.csv"))
application = pd.read_csv(os.path.join(base_dir, "application.csv"))
location = pd.read_csv(os.path.join(base_dir, "location.csv"))
price = pd.read_csv(os.path.join(base_dir, "price.csv"))
notification = pd.read_csv(os.path.join(base_dir, "notification.csv"))
subscription = pd.read_csv(os.path.join(base_dir, "subscription.csv"))

""" Merging tables """
merged_table = customer.merge(subscription, on='customer_id', how='inner')

merged_table = merged_table.merge(application, left_on='application_id', right_on='app_id', how='inner')

merged_table = merged_table.merge(location, on='location_id', how='inner')

merged_table = merged_table.merge(price, left_on='price_id', right_on='id', how='inner')

merged_table = merged_table.merge(notification, on='notification_id', how='inner')

merged_table = merged_table.merge(plan, left_on='plan_type_id', right_on='plan_id', how='inner')


""" Cleaning  and labeling data"""

# Defining subscription duration

merged_table['start_date'] = pd.to_datetime(merged_table['start_date'])
merged_table['end_date'] = pd.to_datetime(merged_table['end_date'])

merged_table['subscription_duration'] = (merged_table['end_date'] - merged_table['start_date']).dt.days

columns_to_drop = ['first_name', 'last_name','location', 'app_id', 'area_name','id_x',  'id_y', 'start_date','end_date', 'plan_id_x', 'plan_id_y']
merged_table = merged_table.drop(columns=columns_to_drop)


categorical_columns = merged_table.select_dtypes(include=['object', 'category']).columns
label_encoder = LabelEncoder()

for col in categorical_columns:
    merged_table[col] = label_encoder.fit_transform(merged_table[col])

#print(merged_table.head(20))

""" Defining functions for evaluating ML models"""

def evaluate_model(y_true, y_pred, y_proba=None):
    """
    Evaluate a classification model's performance.

    Parameters:
        y_true: Actual target values.
        y_pred: Predicted target values.
        y_proba: Predicted probabilities for the positive class (optional).

    Returns:
        A dictionary with evaluation metrics.
    """
    metrics = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1-Score": f1_score(y_true, y_pred)
    }
    if y_proba is not None:
        metrics["ROC AUC"] = roc_auc_score(y_true, y_proba)
    else:
        metrics["ROC AUC"] = "N/A (no probabilities provided)"
    return metrics



def visualize_metrics(metrics_dict):
    """
    Parameters:
        metrics_dict: A dictionary where keys are model names
                      and values are dictionaries of evaluation metrics.
    """
    # Convert metrics to a DataFrame
    metrics_df = pd.DataFrame(metrics_dict).T  # Transpose for easier plotting

    # Making sure all numeric values are float
    metrics_df = metrics_df.apply(pd.to_numeric, errors='coerce')

    # 1. Grouped Bar Chart
    plt.figure(figsize=(12, 6))
    metrics_df.plot(kind='bar', figsize=(12, 6))
    plt.title("Model Evaluation Metrics - Grouped Bar Chart")
    plt.ylabel("Score")
    plt.xlabel("Models")
    plt.xticks(rotation=45)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()

    # 2. Line Plot for Metrics
    plt.figure(figsize=(12, 6))
    for metric in metrics_df.columns:
        plt.plot(metrics_df.index, metrics_df[metric], marker='o', label=metric)
    plt.title("Model Evaluation Metrics - Line Plot")
    plt.ylabel("Score")
    plt.xlabel("Models")
    plt.xticks(rotation=45)
    plt.legend(loc="best")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 3. Individual Metric Distribution
    for metric in metrics_df.columns:
        plt.figure(figsize=(8, 5))
        plt.bar(metrics_df.index, metrics_df[metric], color='skyblue')
        plt.title(f"{metric} Distribution Across Models")
        plt.ylabel(metric)
        plt.xlabel("Models")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


""" Predicting status activity (churn rate)"""

# churn rate = (Number of Canceled/Expired Users) / (Total Users)

merged_table['is_churned'] = merged_table['status'].apply(lambda x: 1 if x in [1, 2] else 0)

# as our active status = 0, canceled = 1, expired = 2
# to find churn rate we need canced/exprired percantage

churn_rate = merged_table['is_churned'].mean()
print(f"Churn Rate: {churn_rate:.2%}")

# We have 61% churn rate

""" Model building """

# Define features  and target
X = merged_table.drop(columns=['status', 'is_churned'])
y = merged_table['is_churned']

#Splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


metrics_dict = {}

models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    "SVM": SVC(probability=True, random_state=42),  # SVM with probabilities
    "Logistic Regression": LogisticRegression(random_state=42),
    "Bagging": BaggingClassifier(estimator=LogisticRegression(), random_state=42)
}


for model_name, model in models.items():
    print(f"Training {model_name}...")

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None


    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred),
        "ROC AUC": roc_auc_score(y_test, y_proba) if y_proba is not None else "N/A"
    }


    metrics_dict[model_name] = metrics


for model_name, metrics in metrics_dict.items():
    print(f"\n{model_name} Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")

# Visualize metrics
visualize_metrics(metrics_dict)



metrics_df = pd.DataFrame(metrics_dict).T

# Display the metrics sorted by F1-Score
# I decided to go with F1- score as it is better for predicting churn rate
# Precision: Minimize unnecessary retention efforts for users who wouldn't churn.
# Recall: Ensure you capture as many churned users as possible.
# F1 Score balances these priorities.

best_model = metrics_df.sort_values(by="F1-Score", ascending=False).iloc[0]
print("Best Model Based on F1-Score:\n", best_model)

print("\nAll Model Metrics:\n", metrics_df)


sorted_metrics = metrics_df.sort_values(by="F1-Score", ascending=False)
print("\nMetrics Sorted by F1-Score:\n", sorted_metrics)

best_model_name = sorted_metrics.index[0]
print(f"\nOverall Best Model Based on F1-Score: {best_model_name}")


""" Logistic Regressing has the highest Accuracy and F1-score, so for our future prediction for churn rate
    we can proceed with Logistic regression as the best model"""





"""  Predicting subscription duration """

X = merged_table.drop(columns=['subscription_duration'])  # Drop target variable
y = merged_table['subscription_duration']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Random Forest": RandomForestRegressor(random_state=42),
    "XGBoost": XGBRegressor(random_state=42),
    "Support Vector Regressor": SVR(),
    "Linear Regression": LinearRegression(),
    "Bagging": BaggingRegressor(estimator=LinearRegression(), random_state=42)
}

metrics_dict = {}

for model_name, model in models.items():
    print(f"Training {model_name}...")

    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)

    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "MSE": mean_squared_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "R² Score": r2_score(y_test, y_pred)
    }
    metrics_dict[model_name] = metrics

metrics_df = pd.DataFrame(metrics_dict).T
print("\nRegression Metrics:\n", metrics_df)

visualize_metrics(metrics_dict)

""" For subscription duration prediction, Random forest performs the best, 
    demonstrating the lowest values across all key metrics"""


"""In summary, for Churn rate prediction we will go with logistic regression model 
    and for Subscription durationg prediction we will go with Random Forest model"""