import httplib2
import os
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
import datetime
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

flow= OAuth2WebServerFlow(
	client_id='671063856681-k9qpm7880m7d60o5ktutpjgg25rq2ke7.apps.googleusercontent.com',
    client_secret='ya3PZA52xTuWcErhNognf2zy',
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://localhost:5000/success')

def startOAUTH():
	storage = Storage('calendar.dat')
	credentials = storage.get()	
	if credentials is None:
		auth_uri = flow.step1_get_authorize_url()
	return auth_uri

def endOAUTH2(code):
	credentials = flow.step2_exchange(code)	

	http = httplib2.Http()
	http = credentials.authorize(http)

	service = build(serviceName='calendar', version='v3', http=http)
	page_token = None
	calendar_list = service.calendarList().list(pageToken = page_token).execute()
	for calendar_list_entry in calendar_list['items']:
		print(calendar_list_entry['summary'])

def getBusyDates(startDate, endDate,id, code):
	credentials = flow.step2_exchange(code)	

	http = httplib2.Http()
	http = credentials.authorize(http)

	service = build(serviceName='calendar', version='v3', http=http)
	return service.freebusy().__dict__.keys()

