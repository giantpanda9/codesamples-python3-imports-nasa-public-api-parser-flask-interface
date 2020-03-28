#app.py
#data Controller

from flask import Flask, render_template
from models import parseNASA

#create Flask app instance
app = Flask(__name__)

#Debug mode on
app.debug = True

@app.route("/")
def index():
	parseNASAInstance = parseNASA()
	APIResponse = parseNASAInstance.getAll()
	typeText = "for 7 days"
	return render_template(
		'index.html',
		APIResponse=APIResponse,
		typeText=typeText
		)

@app.route("/today")
def today():
	parseNASAInstance = parseNASA()
	APIResponse = parseNASAInstance.getAll(True)
	typeText = "for today"
	return render_template(
		'index.html',
		APIResponse=APIResponse,
		typeText=typeText
		)

@app.route("/hazardous")
def hazardous():
	parseNASAInstance = parseNASA()
	APIResponse = parseNASAInstance.getHazardous()
	typeText = "hazardous to Earth for 7 days"
	return render_template(
		'hazardous.html',
		APIResponse=APIResponse,
		typeText=typeText
		)

if __name__ == "__main__":
	app.run()
