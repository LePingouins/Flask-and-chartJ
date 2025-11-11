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

@app.route('/api/pie-data')
def pie_data():
    data = {
        'labels': ['Online', 'Sleeping', 'Charging', 'Error'],
        'datasets': [{
            'label': 'Smart Devices',
            'data': [20, 5, 8, 2],  # change counts here
            'backgroundColor': [
                'rgba(54, 162, 235, 0.7)',   # Blue
                'rgba(255, 206, 86, 0.7)',   # Yellow
                'rgba(75, 192, 192, 0.7)',   # Teal
                'rgba(255, 99, 132, 0.7)'    # Pink
            ],
            'borderColor': [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)'
            ],
            'borderWidth': 1
        }]
    }
    return jsonify(data)


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