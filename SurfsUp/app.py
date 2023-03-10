import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#database set up
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurements = Base.classes.measurement
station = Base.classes.station

session = Session(engine)
#flask set up
app = Flask(__name__)
#flask routes

@app.route("/")
def welcome():
    return(
        f"Available Routes"
        <br>
        f"/api/v1.0/precipitation"
        <br>
        f"/api/v1.0/stations"
        <br>
        f"/api/v1.0/tobs"
         <br>
        f"/api/v1.0/start/end"
    )
@app.route(/api/v1.0/precipitation)
def precipitation():
    rain = session.query(Measurements.date, Measurements.prcp).\
    filter(Measurements.date < '2011-01-01').\
    order_by(Measurements.date).all()
    return jsonify(rain)

@app.route("/api/v1.0/stations")
def stations():
        results = session.query(station.station).all()
        stations = list(np.ravel(results))
        return jsonify(stations)

@app.route("/api/v1.0/tobs")
def observations():
       results = session.query(Measurements.tobs).\
                filter(Measurements.station == 'USC00519281').\
                filter(Measurements.date >= '2016-08-23').all()

        temps = list(np.ravel(results))
        return jsonify(temps)  

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start, end):

if __name__ == "__main__":
    app.run(debug=True)