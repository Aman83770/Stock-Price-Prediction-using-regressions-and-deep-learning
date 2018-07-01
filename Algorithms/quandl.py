import quandl as quandl
import sys
import requests


def get_historical(quote):
    FILE_NAME = quote + '.csv'
    # Download our file from google finance
    url = 'https://www.quandl.com/api/v3/datasets/NSE/'+quote+'.csv?api_key=t6gLn75zvyd9a748yqqy'
    r = requests.get(url, stream=True)
    if r.status_code != 400:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)
        return True

quote  =  sys.argv[1]
if get_historical(quote):
	print "file has been saved"