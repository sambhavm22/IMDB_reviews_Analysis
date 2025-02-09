# data_setup.py
import pandas as pd
from sklearn.model_selection import train_test_split
import mysql.connector
from mysql.connector import Error

# Load the dataset
def load_data(filepath):
    df = pd.read_csv(filepath)  
    return df

# Preprocess the data
def preprocess_data(df):
    # Example: Drop missing values
    df = df.dropna()
    return df

# Save data to MySQL database
def save_to_db(df, table_name, db_config):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Create table if it doesn't exist
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            review TEXT,
            sentiment VARCHAR(10)
        )
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        for _, row in df.iterrows():
            insert_query = f"""
            INSERT INTO {table_name} (review, sentiment)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (row["review"], row["sentiment"]))

        # Commit changes
        connection.commit()
        print(f"Data saved to {table_name} table successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main function
def main():
    # Load and preprocess data
    df = load_data("IMDB.csv")  # Replace with your dataset file
    df = preprocess_data(df)

    # Split data into train and test sets
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # MySQL database configuration
    db_config = {
        "host": "localhost",       # Replace with your MySQL host
        "user": "root",            # Replace with your MySQL username
        "password": "sambhavmehta1",
        "database": "sentiment_db" # Replace with your database name
    }

    # Save data to MySQL database
    save_to_db(train_df, "train_reviews", db_config)
    save_to_db(test_df, "test_reviews", db_config)

if __name__ == "__main__":
    main()