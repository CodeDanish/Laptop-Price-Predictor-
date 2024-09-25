# Laptop Price Predictor 💻💸

![Laptop Price](https://img.shields.io/badge/Price-Prediction-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 📚 Overview

The **Laptop Price Predictor Model** uses machine learning to predict the price of laptops based on their specifications such as brand, processor type, RAM, storage, and GPU. The project aims to assist consumers in determining the approximate market price of a laptop given its features.

### 🎯 Objective
To create a model that predicts laptop prices with high accuracy based on various specifications.

## 📂 Project Structure

```
laptop-price-prediction/
├── data/
│   ├── laptops.csv            # Dataset with laptop specifications and prices
├── notebooks/
│   ├── data_analysis.ipynb    # EDA and data analysis
│   ├── model_building.ipynb   # Model development and evaluation
├── app.py                     # Streamlit app for price prediction
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/laptop-price-predictor.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd laptop-price-predictor
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## ⚙️ Model Building Process

### 1. Data Preprocessing 🧹
- Clean the dataset, handle missing values, and encode categorical features such as laptop brand and processor type.
- Convert text-based features like `RAM`, `Storage`, and `GPU` into numerical formats for model training.

### 2. Feature Engineering 🛠️
Key features used in the model:
- **Brand**: Laptop brand
- **Processor**: CPU model and generation
- **RAM**: Amount of RAM in GB
- **Storage**: Type and capacity (SSD/HDD)
- **GPU**: Graphics card used

### 3. Model Training 🤖
The model was trained using the following algorithms:
- **Linear Regression**
- **Random Forest Regressor**
- **XGBoost Regressor**

### 4. Model Evaluation 🏅
The best model achieved:
- **R² Score:** 0.91
- **Mean Absolute Error (MAE):** 1500 USD
- **Mean Squared Error (MSE):** 5000000 USD

## 🖥️ Demo

You can interact with the **Laptop Price Predictor Model** using the Streamlit app:

https://f3bdhzxlhxyxgacue7pkur.streamlit.app/

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas, Numpy** for data analysis
- **Scikit-learn** for machine learning models
- **XGBoost** for advanced model tuning
- **Streamlit** for the web interface

## 📊 Model Performance

| Algorithm            | R² Score | MAE      | MSE       |
|----------------------|----------|----------|-----------|
| Linear Regression     | 0.85     | 1800 USD | 6000000   |
| Random Forest         | 0.90     | 1600 USD | 5300000   |
| XGBoost               | 0.91     | 1500 USD | 5000000   |

## 🤝 Contributing

Contributions are welcome! If you want to improve this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss your ideas.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> 🔗 **References**:
> - [Pandas Documentation](https://pandas.pydata.org/)
> - [Scikit-learn Documentation](https://scikit-learn.org/stable/)
> - [Streamlit Documentation](https://docs.streamlit.io/)

