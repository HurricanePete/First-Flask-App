from datetime import datetime
from app import db, ma
from marshmallow import fields

class Meters(db.Model):
	__tablename__ = "meters"
	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(120), index=True, unique=True)
	data = db.relationship('MeterData', backref='meter', lazy='dynamic')

	def __repr__(self):
		return '<label {}, id {}>'.format(self.label, self.id)

class MeterData(db.Model):
	__tablename__ = "meter_data"
	id = db.Column(db.Integer, primary_key=True)
	meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	value = db.Column(db.Integer)

	def __repr__(self):
		return '<id: {}, meter_id {}, timestamp {}, value {}>'.format(self.id, self.meter_id, self.timestamp, self.value)

class MeterDataSchema(ma.ModelSchema):
	class Meta:
		fields = ('id', 'meter_id', 'timestamp', 'value')