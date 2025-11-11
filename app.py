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
    # Static data representing IoT device statuses
    data = {
        'labels': ['Active', 'Inactive', 'Maintenance', 'Offline'],
        'datasets': [{
            'label': 'Device Status',
            'data': [12, 3, 2, 1],  # Example counts for each label
            'backgroundColor': [
                'rgba(75, 192, 192, 0.7)',
                'rgba(255, 99, 132, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(153, 102, 255, 0.7)'
            ],
            'borderColor': [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(153, 102, 255, 1)'
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