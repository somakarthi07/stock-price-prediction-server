from flask import Flask, request # import flask 
import yfinance as yf # import yfinance
import prediction
import pandas as pd
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/company-list', methods=['GET'])
def companies_list_get():
    df = pd.read_csv("./static/nasdaq_screener.csv")[["Symbol","Name"]]
    print(df.head())
    return df.to_json()


# URL: http://locahost:5000/company/MSFT
@app.route('/company', methods=['GET'])
def company_data_get():
    companyName = request.args.get("code")
    companyData = yf.Ticker(companyName)
    return companyData.info

@app.route('/result', methods=['GET'])
def download_train_predict():
    # Define the stock symbol and timeframe
    stock_symbol = 'AAPL'
    start_date = '2010-01-01'
    end_date = '2023-04-01'
    # end_date = '2020-12-31'

    # Download stock data into a DataFrame
    df = yf.download(stock_symbol, start=start_date, end=end_date)

    company_data = yf.Ticker(stock_symbol)

    # hist = company_data.history(period="1mo")
    hist = company_data.history(period="1d")
    print(df)
    print(hist)
    data = hist[['Open', 'High', 'Low', 'Volume']]

    # train and predict
    prediction.train_and_predict(historical_df=df, predict_df=data)

    return "success"

 
# main driver function
if __name__ == '__main__':
    app.run()