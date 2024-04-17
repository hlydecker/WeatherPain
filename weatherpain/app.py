from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from forms import PainForm
from models import db, PainRecord
from weather_api import fetch_weather_data
from plotly import graph_objs as go
from plotly.offline import plot

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pain_records.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PainForm()
    if form.validate_on_submit():
        pain_score = form.pain_score.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        timestamp = datetime.now()
        weather_data = fetch_weather_data(latitude, longitude, timestamp)
        new_record = PainRecord(pain_score=pain_score, timestamp=timestamp, latitude=latitude, longitude=longitude, weather=weather_data)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))
    records = PainRecord.query.all()
    plots = create_plots(records)
    return render_template('index.html', form=form, plots=plots)

def create_plots(records):
    if not records:
        return None
    pain_scores = [record.pain_score for record in records]
    timestamps = [record.timestamp for record in records]
    temperatures = [record.weather['temperature'] for record in records]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=pain_scores, mode='lines+markers', name='Pain Score'))
    fig.add_trace(go.Scatter(x=timestamps, y=temperatures, mode='lines+markers', name='Temperature', yaxis='y2'))
    fig.update_layout(title='Pain Scores and Weather Data', xaxis_title='Time', yaxis_title='Pain Score', yaxis2=dict(title='Temperature', overlaying='y', side='right'))
    plot_div = plot(fig, output_type='div')
    return plot_div

if __name__ == '__main__':
    app.run(debug=True)
