import pandas as pd
#from shapely.geometry import Point, shape
from flask import request
import os


from flask import Flask
#from flask_compress import Compress
from flask import render_template
import json




def start_app():
    app = Flask(__name__)
    #compress.init_app(app)
    return app




# with open('input/mtrssssss_station.json') as data_file:    
#     provinces_json = json.load(data_file)

app = Flask(__name__)

#@app.route('/coordinates', methods=['GET', 'POST'])
f = open('./static/movesdata.json', 'r')
moves = json.loads(f.read())
coordinatesarr = []
activitiesarr = []

#return the lat-long coordinates array to visualize on map

def coordinates(moves):
	for m in moves:
	    #print "\n-----------------\n", m["date"], "\n\tSEGMENTS"
	    if (m["segments"]):
			for s in m["segments"]:
				if 'activities' in s.keys():
					for a in s['activities']:
						if a['trackPoints']:
							for t in a['trackPoints']:
								coordinatesarr.append([t['lat'], t['lon']]); 
	return coordinatesarr

#return the activities array
def activities(moves):
	for m in moves:
	    
	    if (m["segments"]):
			for s in m["segments"]:
				if 'activities' in s.keys():
					for a in s['activities']:
						if a['group']:
							activitiesarr.append(a['group'])
	return activitiesarr

#print(activities(moves))
@app.route("/")
def index():

	return render_template("index.html", location=coordinates(moves), time = activities(moves))



if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)