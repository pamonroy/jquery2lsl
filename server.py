''''
Remember to start the server
    export FLASK_APP=server.py
    flask run
'''

from flask import Flask, request, jsonify #import main Flask class and request object
from flask_cors import CORS
from pylsl import StreamInfo, StreamOutlet 

info = StreamInfo('markerStreamName','Markers',1,0,'string','marker-data') # declare the LSL stream
outlet = StreamOutlet(info) # create the LSL outlet

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Here should be directions on how to use this API'

# This routine is called from the client (AJAX) using POST method with data in Json format
@app.route('/send-to-lsl', methods=['POST']) #GET requests will be blocked
def send_to_lsl():
    global outlet
    requestData = request.get_json(force=True)
    marker = requestData['markerName']  # get the marker value
    outlet.push_sample([marker])  # send data to Lab Streaming Layer
    returnData = "Hi, this is the server"
    return jsonify(returnData)  # return something to the client
