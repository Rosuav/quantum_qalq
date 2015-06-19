from flask import Flask, render_template
from flask import request, redirect, url_for
import datetime
current_time=datetime.datetime.now()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
  return render_template('base.html',
                         my_title="Home page is currently under construction",
                         current_time=datetime.datetime.now())

@app.route("/fin", methods=["GET"])
def compound_interest_get():
  return render_template('compound_interest.html',
                         my_title="Compound Interest",
                         current_time=datetime.datetime.now())

@app.route("/fin", methods=["POST"])
def compound_interest_post():
  present_value = float(request.form["present_value"])
  interest_rate = float(request.form["interest_rate"])
  time = float(request.form["time"])
  future_value = present_value * ((1 + interest_rate) ** time)
  return redirect(url_for("compound_interest_get"))

@app.route("/min", methods=["GET"])
def minimum_balance_get():
  return render_template('pay_minimum.html',
                        my_title="Paying Minimum Balance",
                        current_time=datetime.datetime.now())

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
  """Convert a datetime to a different format."""
  return value.strftime(format)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)