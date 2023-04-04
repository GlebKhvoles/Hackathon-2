from app import db
from app.stocks import bp
from app.stocks.forms import StockForm
from flask import render_template, redirect, url_for
from app.models import Stock
from app.yahoof import fetchm_nq

@bp.route('/stocks', methods=['GET'])
def get_stocks():
    find_stock_form = StockForm()
    stocks = db.session.query(Stock.ticker).distinct().all()
    return render_template('stocks.html', find_stock_form=find_stock_form, stocks=stocks)


@bp.route('/ticker/<ticker>', methods=['GET'])
def get_ticker(ticker):
    ticker_data = Stock.query.filter_by(ticker=ticker).all()
    return render_template('ticker.html', ticker_data=ticker_data)


@bp.route('/stocks', methods=['POST'])
def post_stocks():
    find_stock_form = StockForm()
    if find_stock_form.validate_on_submit():
        data = fetchm_nq(find_stock_form.stock.data)
        for date, row in data.iterrows():
            stock = Stock(ticker=find_stock_form.stock.data, date=date, price=row['Close'])
            db.session.add(stock)
            db.session.commit()

    return redirect(url_for('stocks.get_stocks'))


