# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import mysql.connector
from mysql.connector import Error

# Load data from MySQL database
def load_data(table_name, db_config):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        query = f"SELECT review, sentiment FROM {table_name}"
        df = pd.read_sql(query, connection)
        return df
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Train the model
def train_model(train_df):
    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train = vectorizer.fit_transform(train_df["review"])
    y_train = train_df["sentiment"]

    # Train Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, vectorizer

# Save the model and vectorizer
def save_model(model, vectorizer, model_path="model.pkl", vectorizer_path="vectorizer.pkl"):
    with open(model_path, "wb") as model_file:
        pickle.dump(model, model_file)
    with open(vectorizer_path, "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

# Main function
def main():
    # MySQL database configuration
    db_config = {
        "host": "localhost",       # Replace with your MySQL host
        "user": "root",            # Replace with your MySQL username
        "password": "sambhavmehta1",
        "database": "sentiment_db" 
    }

    # Load training data
    train_df = load_data("train_reviews", db_config)

    # Train the model
    model, vectorizer = train_model(train_df)

    # Save the model and vectorizer
    save_model(model, vectorizer)

if __name__ == "__main__":
    main()

