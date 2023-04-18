from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_and_predict(historical_df, predict_df):
    # Prepare features and target variable
    X = historical_df[['Open', 'High', 'Low', 'Volume']]  # Use relevant features as X
    y = historical_df['Close']  # Predict the Close price

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)

    # Prepare features for prediction
    X_pred = predict_df  # Prepare X_pred with relevant features for prediction

    # Make predictions
    y_pred = model.predict(X_pred)

    # Print predicted stock prices
    print(y_pred)
    

