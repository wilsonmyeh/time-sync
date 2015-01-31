from flask import Flask,render_template,jsonify, redirect, render_template,request, session
from flask.ext.login import current_user
from flask.views import MethodView
import time
import imp
import oauth

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
	return redirect(oauth.startOAUTH())

@app.route('/login', methods = ['GET','POST'])
def login():
	session['code'] = request.args.get('code','')
	printThis = oauth.getBusyDates("2015-01-31T00:00:00Z", "2015-02-03T00:00:00Z", "steventr@usc.edu", session['code'])
	return printThis

			
if __name__ == '__main__':
	app.run(debug = True)