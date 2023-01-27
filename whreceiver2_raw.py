# Webhook receiver 2 for getting raw data from webhook

import os
import sys
import time
import json
import configparser
from flask import Flask, request, Response, jsonify
from flask_caching import Cache

## read config
whconfig = configparser.ConfigParser()
whrootdir = os.path.dirname(os.path.abspath('config.ini'))
whconfig.read(whrootdir + "/config.ini")
wh_host = whconfig.get("socketserver", "host", fallback='0.0.0.0')
wh_port = whconfig.get("socketserver", "port", fallback='4444')
wh_output_file = whconfig.get("output", "filename", fallback='webhook_log.json')

## set cache 
config = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

# POST request for webhook services.

## webhook receiver
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook")
        request_json = request.json
        # print the received notification
        print('Payload: ')
        # Change from original - remove the need for function to print
        print(json.dumps(request_json,indent=4))

        # save as a file, create new file if not existing, append to existing file
        # full details of each notification to file 'webhook_log.json'

        with open(whrootdir + "/output/" + wh_output_file, 'a') as filehandle:
            # Change from original - we output to file so that the we page works better with the newlines.
            filehandle.write('%s\n' % json.dumps(request_json,indent=4))
            filehandle.write('= - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - \n')

        return "Webhook received!"
    else:
        return "POST Method not supported"

# start scheduling
try:
    app.run(host=wh_host, port=wh_port, debug=False)
except:
    print('Error occured, starting again...')
    pass