from flask import *
import my_dividend_scraper as div

app = Flask(__name__)


@app.route('/dividend/<ticker>')
def dividend_JSON(ticker):
    return div.get_dividend_json(ticker)


if __name__ == '__main__':
    app.run(port=8675)
