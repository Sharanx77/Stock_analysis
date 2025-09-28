# 📈 Stock Analysis Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

An interactive web application built with Streamlit for visualizing and analyzing stock market data. This dashboard allows users to fetch historical data for any stock ticker, plot interactive charts with key technical indicators, view performance summaries, and export data for further analysis.

---


## ✨ Key Features

* **Dynamic Ticker Input**: Analyze any stock by entering its ticker symbol (e.g., AAPL, GOOGL, MSFT).
* **Custom Date Range**: Select a specific start and end date for your analysis.
* **Technical Indicators**: Visualize popular indicators with customizable periods:
    * **SMA** (Simple Moving Average)
    * **EMA** (Exponential Moving Average)
    * **RSI** (Relative Strength Index)
* **Interactive Visualizations**:
    * **Candlestick Chart**: Displays the stock's price action (Open, High, Low, Close).
    * **Moving Averages**: Overlaid as line graphs on the price chart.
    * **RSI Plot**: A separate chart for the Relative Strength Index with overbought (70) and oversold (30) levels.
* **Performance Summary**: Get a quick overview of key metrics, including Start Price, End Price, Total Return, and Annualized Volatility.
* **Data Export**: Download the raw and calculated data as a **CSV file** with a single click.

---

## 🛠️ Technologies Used

* **Python**: Core programming language.
* **Streamlit**: For creating and serving the interactive web application.
* **yfinance**: For fetching historical stock market data from Yahoo Finance.
* **Plotly**: For generating beautiful and interactive charts.
* **Pandas**: For efficient data manipulation and analysis.
* **pandas-ta**: To easily calculate technical analysis indicators.

---

## 📂 Repository Contents

This repository includes the following deliverables:

* [`app.py`](./app.py): The complete Python source code for the Streamlit application.
* [`downloaded_file_from_the_dashboard.csv`](./downloaded_file_from_the_dashboard.csv): An example CSV file...
* [`dashboard.pdf`](./dashboard.pdf): A document containing screenshots...

---

## 🚀 Getting Started

Follow these instructions to get the dashboard running on your local machine.

### Prerequisites

* Python 3.8 or newer.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Sharanx77/Stock_analysis.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Stock_analysis
    ```
3.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### How to Run the Application

1.  Open your terminal or command prompt in the project directory.
2.  Run the following command to start the Streamlit server:
    ```bash
    streamlit run app.py
    ```
3.  Your default web browser will automatically open a new tab with the running application.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving the dashboard, feel free to fork the repository and create a pull request. You can also open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewIndicator`)
3.  Commit your Changes (`git commit -m 'Add some NewIndicator'`)
4.  Push to the Branch (`git push origin feature/NewIndicator`)
5.  Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
