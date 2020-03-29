#models.py
#Data Model

import requests
from datetime import date, timedelta

class parseNASA():
	def __init__(self):
		self.dateDelta = 7
		self.dateToday = date.today()
		self.previousDate = self.dateToday - timedelta(days=self.dateDelta)
		self.APIKey = "DEMO_KEY"
	def getAPIUrl(self, showToday = False):
		startDate = self.dateToday if showToday else self.previousDate
		return f"https://api.nasa.gov/neo/rest/v1/feed?start_date={startDate}&end_date={self.dateToday}&api_key={self.APIKey}"
	def getAll(self, showToday = False):
		APIUrl = self.getAPIUrl(showToday)
		response = requests.get(APIUrl)
		returned = []
		if response.status_code != 200:
			return []
		responseJSON = response.json()
		currentDelta = timedelta(days=1)
		currentDate = self.dateToday if showToday else self.previousDate
		while currentDate <= self.dateToday:
			responseJSONCurrent = responseJSON["near_earth_objects"][str(currentDate)]
			for nasaItem in responseJSONCurrent:
				returnedItem = {}
				returnedItem["name"] = nasaItem["name"]
				returnedItem["fromDate"] = currentDate
				returnedItem["diameterEstMin"] = nasaItem["estimated_diameter"]["kilometers"]["estimated_diameter_min"] or 0
				returnedItem["diameterEstMax"] = nasaItem["estimated_diameter"]["kilometers"]["estimated_diameter_max"] or 0
				returnedItem["hazardous"] = "Yes" if nasaItem["is_potentially_hazardous_asteroid"] else "No"
				returnedItem["cameCloser"] = nasaItem["close_approach_data"][0]["close_approach_date"]
				returnedItem["details"] = nasaItem["nasa_jpl_url"]
				returned.append(returnedItem)
			currentDate += currentDelta
		return returned
	
	def getHazardous(self):
		APIUrl = self.getAPIUrl()
		response = requests.get(APIUrl)
		returned = []
		if response.status_code != 200:
			return []
		responseJSON = response.json()
		currentDelta = timedelta(days=1)
		currentDate = self.previousDate
		while currentDate <= self.dateToday:
			responseJSONCurrent = responseJSON["near_earth_objects"][str(currentDate)]
			for nasaItem in responseJSONCurrent:
				returnedItem = {}
				if (nasaItem["is_potentially_hazardous_asteroid"]):
					returnedItem["name"] = nasaItem["name"]
					returnedItem["fromDate"] = currentDate
					returnedItem["diameterEstMin"] = nasaItem["estimated_diameter"]["kilometers"]["estimated_diameter_min"] or 0
					returnedItem["diameterEstMax"] = nasaItem["estimated_diameter"]["kilometers"]["estimated_diameter_max"] or 0
					returnedItem["hazardous"] = "Yes" if nasaItem["is_potentially_hazardous_asteroid"] else "No"
					returnedItem["cameCloser"] = nasaItem["close_approach_data"][0]["close_approach_date"]
					returnedItem["details"] = nasaItem["nasa_jpl_url"]
					returned.append(returnedItem)
			currentDate += currentDelta
		if (len(returned) <= 0):
			returnedItem = {}
			returnedItem["notAvailable"] = 1
			returned.append(returnedItem)
		return returned
