from app.stocks import bp
from app.stocks.forms import StockForm
from flask import render_template

@bp.route('/stocks', methods=['GET'])
def get_stocks():
    find_stock_form = StockForm()
    # TODO read saved stocks from db
    return render_template('stocks.html', find_stock_form=find_stock_form)


@bp.route('/stocks', methods=['POST'])
def post_stocks():
    find_stock_form = StockForm()
    # TODO fetch yahoo and write to db
    return render_template('stocks.html', find_stock_form=find_stock_form)

