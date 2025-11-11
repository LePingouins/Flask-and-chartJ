import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_db_connection(db_name):
    conn = sqlite3.connect(f'data/{db_name}')
    conn.row_factory = sqlite3.Row  # enables dictionary-style row access
    return conn

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

@app.route('/api/test-db')
def test_db():
    conn = get_db_connection('iot_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return jsonify([t[0] for t in tables])

@app.route('/api/line-data')
def line_data():
    # Connect to the IoT database
    conn = get_db_connection('iot_data.db')

    # Query temperature readings ordered by timestamp
    readings = conn.execute(
        'SELECT timestamp, temperature FROM temperature_readings ORDER BY timestamp'
    ).fetchall()
    conn.close()

    # Format data for Chart.js
    data = {
        'labels': [row['timestamp'] for row in readings],
        'datasets': [{
            'label': 'Temperature (°C)',
            'data': [row['temperature'] for row in readings],
            'borderColor': 'rgb(75, 192, 192)',
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
            'tension': 0.4,
            'fill': True
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