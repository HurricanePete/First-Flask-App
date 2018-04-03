import json

from flask import render_template
from app import app

from app.models import Meters
from app.models import MeterData, MeterDataSchema

@app.route('/')
@app.route('/meters')
@app.route('/meters/')
def meters():
	meters = Meters.query.all()

	return render_template('index.html', title='Home', meters=meters)


@app.route('/meters/<id>')
def meterById(id):
	meterQuery = MeterData.query.filter(MeterData.meter_id==id).order_by(MeterData.timestamp.desc())
	meterData = MeterDataSchema(many=True).dump(meterQuery)
	jsonMeterData = json.dumps(meterData[0], indent=4)

	return render_template('index.html', title='Home', meter_data=jsonMeterData)