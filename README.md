# codesamples-python3-imports-nasa-public-api-parser-flask-mvc-mvt-interface
Python 3, Flask, Imports NASA Open APIs parser with Flask MVC/MVT HTML/CSS interface
# Description
Graphical edition of the https://github.com/giantpanda9/codesamples-python3-imports-nasa-public-api-parser-bash projects, created using Python 3, Imports, Flask Framework, Jinja2 template
# Purposes
To demonstrate ability to integrate APIs on Python 3 - to parse one of APIs from https://api.nasa.gov/ - to create an MVC/MVT structured Web Sites using Flask - one of the dedicted MVC project promised here: https://github.com/giantpanda9/codesamples-python3-flask-api
# Requirements
1) Python 3
2) Imports
3) virtualenv
4) Modified code from: https://github.com/giantpanda9/codesamples-python3-imports-nasa-public-api-parser-bash
5) Flask
# Installation instructions (approximate, not the last ones to follow):
1) sudo pip3 install virtualenv
2) mkdir Python3_ParseNASA_Flask or clone the project
3) cd Python3_ParseNASA_Flask
4) virtualenv Python3_ParseNASA_Flask
5) source Python3_ParseNASA_Flask/bin/activate
6) pip install gunicorn flask
7) Overall you structure should be similar to the one in github except for the files created by Flask
8) [if not done earlier] sudo ufw allow 5000
9) python app.py
11) [optional, done playing?] deactivate
# How to run?
1) 127.0.0.1:5000/ - should display the page with simple css design and small cardlooking cells with Asteroids data or single card looking cell with error message if NASA API is not available
# Notes
1) To parse Near Earth Objects data provided by NASA and 
SpaceRocks Team ( https://github.com/SpaceRocks/ ): David Greenfield, Arezu Sarvestani, Jason English, Peter Baunach
2) This script is to parse Earth Object Web Service RESTful web service
3) Commercial use not implied or considered. In fact this is to be used a Python/Imports/Flask/Jinja/MVC/MVT programming skills sample no other use is conidered in a sythentic way - [UPDATE March 29th, 2020] some functions and methods created to demonstrate the ability mostly
