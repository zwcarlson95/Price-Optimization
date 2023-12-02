import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def preprocess_data(dataset):
    # Handle missing values
    dataset = dataset.dropna()

    # Handle outliers
    selected_features = ['qty', 'freight_price', 'product_score', 'customers',
                         'volume', 'comp_1', 'ps1', 'fp1', 'comp_2', 'ps2', 'fp2']

    for feature in selected_features:
        mean = dataset[feature].mean()
        std = dataset[feature].std()
        dataset = dataset[(dataset[feature] >= mean - 3 * std) & (dataset[feature] <= mean + 3 * std)]

    # Convert columns to numeric
    dataset = dataset.apply(pd.to_numeric, errors='coerce')

    # Remove rows with incorrect data types
    for column in dataset.columns:
        dataset = dataset[dataset[column].apply(lambda x: isinstance(x, (int, float)))]

    return dataset

def train_model(dataset):
    # Select specific features for training
    selected_features = ['qty', 'freight_price', 'product_score', 'customers',
                         'volume', 'comp_1', 'ps1', 'fp1', 'comp_2', 'ps2', 'fp2']

    # Features (X) and target variable (y)
    X = dataset[selected_features]
    y = dataset['unit_price']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the decision tree regression model
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    return model, X_test, y_test

def calculate_metrics(model, X_test, y_test):
    # Calculate regression metrics on the test set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2