from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/line_chart')
def line_chart():
    return render_template('line_chart.html')

@app.route('/bar_chart')
def bar_chart():
    return render_template('bar_chart.html')

@app.route('/pie_chart')
def pie_chart():
    return render_template('pie_chart.html')

# 👇 This part actually starts the Flask development server
if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#  return render_template('home.html')
#
# @app.route('/line-chart')
# def line_chart():
#  return render_template('line_chart.html')
#
# @app.route('/bar-chart')
# def bar_chart():
#  return render_template('bar_chart.html')
#
# @app.route('/pie-chart')
# def pie_chart():
#  return render_template('pie_chart.html')
#
# if __name__ == '__main__':
#  app.run(debug=True)