from flask import *
import my_dividend_scraper as div

app = Flask(__name__)


@app.route('/dividend/', methods=['GET'])
def dividend_JSON():
    query = str(request.args.get('ticker'))  # /dividend/?ticker=ticker_symbol
    return div.get_dividendJSON(query)


if __name__ == '__main__':
    app.run(port=8675)
