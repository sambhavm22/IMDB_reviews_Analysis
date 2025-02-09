# Sentiment Analysis using Logistic Regression and Flask

This project performs sentiment analysis on movie reviews using a Logistic Regression model trained on TF-IDF vectors. The model is deployed as a Flask API that predicts whether a given text is positive or negative.

## Project Structure
sentiment-analysis/

1. data_setup.py -> Script to load and preprocess data, and save it to MySQL
2. model_trainer.py -> Script to train the Logistic Regression model
3. app.py -> Flask API for sentiment prediction
4. requirements.txt -> Python dependencies
5. IMDB.csv -> Dataset (reviews and sentiment)
6. README.md -> Project documentation
7. model.pkl -> Trained Logistic Regression model
8. tfidf_vectorizer.pkl -> Trained TF-IDF vectorizer

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.8+**
2. **MySQL Server** (for storing the dataset)
3. **MySQL Workbench** (optional, for managing the database)

## Setup Instructions

1. Clone this repository:
   ```bash
    git clone https://github.com/sambhavm22/IMDB_reviews_Analysis.git
    cd sentiment-analysis


2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Set Up MySQL Database
  Create a MySQL database named sentiment_db.

  Update the db_config dictionary in data_setup.py and model_trainer.py with your MySQL credentials:

4. Load and Preprocess Data
  Run the data_setup.py script to load the dataset, preprocess it, and save it to the MySQL database:
   ```bash
   python data_setup.py

This script will:

Load the IMDB.csv dataset.

Split the data into training and testing sets.

Save the data into two MySQL tables: train_reviews and test_reviews.

5. Train the Model
Run the model_trainer.py script to train the Logistic Regression model and save it to disk:
   ```bash
   python train_model.py
   
This script will:

Load the training data from the train_reviews table.

Train a Logistic Regression model on TF-IDF vectors.

Save the trained model (model.pkl) and vectorizer (tfidf_vectorizer.pkl) to disk.

6. Run the Flask API
Start the Flask API by running:
   ```bash
   python app.py
The API will be available at http://127.0.0.1:5000.

Using the Flask API
Endpoint: /predict
Method: POST

Input: JSON with a review_text field.

Output: JSON with a sentiment_prediction field (positive or negative).
---

#### Testing the API
You can test the API using:

1. Postman (GUI tool)

2. Python’s requests library

---
#### License
This project is licensed under the MIT License. See the LICENSE file for details.
---
#### Author
Sambhav Mehta
