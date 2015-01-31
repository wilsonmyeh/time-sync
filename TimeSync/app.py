from flask import Flask,render_template,jsonify, redirect, render_template,request
from flask.ext.login import current_user
from flask.views import MethodView
import time
import imp
import oauth

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
	return redirect(oauth.startOAUTH())

@app.route('/login', methods = ['GET','POST'])
def login():
	calendar = oauth.endOAUTH2(request.args.get('code',''))
	return calendar

			
if __name__ == '__main__':
	app.run(debug = True)