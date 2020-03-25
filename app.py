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
	APIResponse = parseNASAInstance.getResponse()
	return render_template(
		'index.html',
		APIResponse=APIResponse
		)

if __name__ == "__main__":
	app.run()
