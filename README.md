Laptop Price Predictor


Overview:

The Laptop Price Predictor is a machine learning project designed to estimate the price of a laptop based on its specifications. By analyzing various features such as brand, processor type, RAM size, storage capacity, and screen size, the model predicts the likely market price. This tool is useful for consumers, retailers, and businesses looking to understand and evaluate laptop pricing based on hardware and brand features.


Features:

- Data Preprocessing: Cleaned the dataset by handling missing values, encoding categorical variables (like brand and processor type), and scaling numerical features (such as RAM, storage, and screen size).
- Exploratory Data Analysis (EDA): Conducted EDA to uncover trends, correlations, and patterns between the features and the laptop prices.
- Feature Engineering: Created and selected relevant features that contribute significantly to the model’s accuracy, such as brand popularity, processor performance, and price-to-performance ratios.
- Modeling: Trained multiple regression models including Linear Regression, Decision Trees, Random Forest, and Gradient Boosting to predict laptop prices. The best-performing model was selected based on cross-validation and test set performance.
- Model Evaluation: Evaluated the models using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² score to determine the accuracy of predictions.
- Deployment: Deployed the final model as an interactive web application using Streamlit, allowing users to input laptop specifications and receive a predicted price.


Installation:

To set up and run this project locally, follow these steps:


Clone the repository:

bash

Copy code

git clone https://github.com/yourusername/laptop-price-predictor.git

Navigate to the project directory:

bash

Copy code

cd laptop-price-predictor

Install the required dependencies:

bash

Copy code

pip install -r requirements.txt

Run the Streamlit application:

bash

Copy code

streamlit run app.py


Usage:

- Web Application: After running the Streamlit app, you can use the web interface to predict laptop prices. Enter the laptop's specifications, such as brand, processor type, RAM size, storage, etc., and the app will display the predicted price.

- Jupyter Notebooks: Review the provided Jupyter notebooks to explore the data preprocessing, feature engineering, model training, and evaluation processes.


Technologies Used:

Programming Language: Python

Libraries:
- Pandas: For data manipulation and analysis
- Scikit-learn: For machine learning model training and evaluation
- XGBoost/LightGBM: For advanced gradient boosting models
- Streamlit: For deploying the machine learning model as a web application
- Matplotlib/Seaborn: For data visualization during EDA


Contributing:

Contributions are welcome! If you'd like to improve the model, enhance the application, or fix issues, feel free to fork the repository, create a new branch, and submit a pull request. Please ensure that your contributions align with the project's goals and follow best practices.


License:

This project is licensed under the MIT License. See the LICENSE file for more information.

Demo:

https://f3bdhzxlhxyxgacue7pkur.streamlit.app/








