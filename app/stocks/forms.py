from flask_wtf import FlaskForm
import wtforms

class StockForm(FlaskForm):
    stock = wtforms.StringField('Stock', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Find')

