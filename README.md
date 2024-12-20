# Stock Predictor 📈

Welcome to Stock Predictor, a cutting-edge platform for forecasting stock market trends using publicly available data and advanced AI techniques. This project is designed to help users make informed investment decisions by analyzing historical data and providing predictions on stock movements.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Stock Predictor provides a user-friendly interface for analyzing and predicting stock market trends. Users can choose specific stocks or let the platform suggest random selections. The application leverages advanced algorithms and machine learning techniques to provide reliable insights on stock performance.

---

## Features

- **Stock Selection**: Choose from a wide range of stocks or let the platform select randomly.
- **Predictive Analysis**: Get predictions for short-term, medium-term, and long-term stock trends.
- **Interactive Visualization**: View historical stock data and time-series predictions with detailed graphs.
- **User Authentication**: Secure login and signup portal for personalized user experiences.

---

## How It Works

1. **Stock Selection**: Choose a specific stock or let the system select one for you.
2. **Data Analysis**: The system analyzes historical data points using AI and ML algorithms.
3. **Prediction Report**: A detailed prediction report is generated, including stock performance forecasts and trends.

---

## Technologies Used

- **Frontend**: Streamlit for creating the interactive user interface.
- **Backend**: Python with Facebook Prophet for time-series forecasting.
- **Data Analysis**: yFinance for fetching stock market data.
- **Authentication**: Firebase for secure user login and signup.

---

## Installation

### Prerequisites
- Python 3.8+

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-predictor.git
   cd stock-predictor
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   streamlit run app.py
   ```
4. Open the application in your browser at the URL provided by Streamlit.

---

## Usage

1. **Login or Signup**: Create an account or log in through the Firebase-based user portal.
2. **Choose Stock Data**: Select a stock for analysis using yFinance.
3. **View Results**: Analyze predictions generated by Facebook Prophet and visualize trends.

---

## Screenshots

### About Page
![screenshot](docs/page1.png)

### Login Page
![screenshot](docs/page2.png)

### Stock Infos Page
![screenshot](docs/page3.png)

### Stock Prediction Page
![screenshot](docs/page4.png)
---




## Future Improvements

- **Real-time Data Integration**: Fetch live stock market data for real-time predictions.
- **Improved AI Models**: Incorporate advanced deep learning models for higher accuracy.
- **Mobile App**: Develop a mobile application for better accessibility.
- **Portfolio Management**: Add features to manage and optimize user portfolios.
