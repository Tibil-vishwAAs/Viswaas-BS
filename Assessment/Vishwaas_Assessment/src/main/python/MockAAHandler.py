import json
from flask import Flask, request, jsonify
import logging
from MockAAGetSet import *

import requests

# import Validator

# from Assessment import  logger
# logger = logging.getLogger('Assessment-logger')
# # Create a file handler to write logs to a file
# handler = logging.FileHandler('/home/amith/Desktop/Vishwass/Runner/vishwaas-final-poc-1/vishwaas/src/main/python/api/assessment.log',mode='a')
# # Set the logging level to INFO
# logger.setLevel(logging.INFO)
# # Create a formatter to format the log messages
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#
# # Set the formatter for the handler
# handler.setFormatter(formatter)
#
# # Add the handler to the logger
# logger.addHandler(handler)


app = Flask(__name__)
# Set the log level to DEBUG
app.logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler(
    '/home/amith/Desktop/Vishwass/Runner/vishwaas-final-poc-1/vishwaas/src/main/python/assessment.log',
    mode='a')  # mode = 'a ',it will append new logs to an existing file rather than creating a new one each time.
handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the app logger
app.logger.addHandler(handler)


@app.route('/consent/request', methods=['POST'])
def consent_request():
    app.logger.info("Consent request received from SUT")

    # Extract data from request
    ver = request.json['ver']
    txnid = request.json['txnid']

    # Perform necessary actions with data (e.g. save to database)
    # ...

    # Construct response
    response_data = {
        'ver': ver,
        'txnid': txnid,
        'status': 'ok',
        "message": "from Mock-AA Consent request is received"
    }
    return jsonify(response_data)


@app.route('/consent/handle/request', methods=['Post'])
def consent_handle_request():
    app.logger.info("Consent handle request received from SUT")

    # Extract data from request
    ver = request.json['ver']
    txnid = request.json['txnid']
    # ConsentStatus = request.json.get('ConsentStatus', {}).get('status')
    # Perform necessary actions with data (e.g. save to database)
    # ...

    # Construct response
    response_data = {
        'ver': ver,
        'txnid': txnid,
        'status': "OK",
        "message": "from Mock-AA Consent Handler request"
    }

    mockAaResponseObj.setResponse("Pending")
    # print(Status)

    return jsonify(response_data)


@app.route('/Sum', methods=['POST'])
def sum():
    """"
    Create an api to add two numbers,
    enpoint = /sum,
    method = post,
    response sum of two numbers,
    api shouldnot accept -ve numbers and throw error with appropriate message like api doesn't accept -ve numbers please provide +ve numbers
    """
    data = request.get_json()
    a = int(data.get("a"))
    b = int(data.get("b"))

    if a < 0 or b < 0:
        return "API does not accept negative numbers please provide positive numbers."
    result = a + b

    return jsonify(result)


# def set_consent_handle_request():
#     consent_handle = "39e108fe-9243-11e8-b9f2-0256d88baae8"
#     url = f"http://localhost:5001/consent/handle/{consent_handle}"  # Replace <consent_handle> with the actual consent handle value
#
#     response = requests.get(url=url)
#     print("Response of Consent handle status")
#     print(response.text)
#
#     if response.status_code == 200:
#         response_data = response.json()
#
#         # Update the Consent Handle request response with 'PENDING' status
#         response_data["ConsentStatus"]["status"] = "PENDING"
#
#         updated_response = json.dumps(response_data)
#         print("Status Changed "+updated_response)
#     else:
#         print(f"Error: {response.status_code} - {response.text}")
#
#
# set_consent_handle_request()


@app.route('/consent/notification/response', methods=['POST'])
def consent_notification_response():
    app.logger.info("Consent notification response received from MOCK-AA")

    ver = request.json['ver']
    txnid = request.json['txnid']

    # Perform necessary actions with data (e.g. save to database)
    # ...

    # Construct response
    response_data = {
        'ver': ver,
        'txnid': txnid,
        'status': 'ok',
        "message": "Consent notification response received from Mock AA, ready for validation"
    }

    app.logger.info("Validation started for consent notification response")
    app.logger.info("Parsing the validation json specification file")

    res = jsonify(response_data)
    # print(res.status_code)

    assert res.status_code == 200
    print(f"Response code: {res.status_code}")

    # with open('config.json') as config_file:
    #     config_data = json.load(config_file)
    #
    # # app.logger.info((request.json))
    # data = request.json
    # Version = config_data['Column']['ver']
    #
    # assert data.status_code == 200
    # print(f"Response code: {data.status_code}")
    # app.logger.info("Validating the API version ", data)
    # response_version = data['ver']
    #
    # if response_version in Version:
    #     # print('Response version matches the config version:', response_version)
    #     app.logger.info(f"version:{response_version} validation is successful and match NBFC-AA ecosystem version")
    # else:
    #     # print('Response version does not match the config version')
    #     app.logger.info(f"version:{response_version} validation is unsuccessful, not match NBFC-AA ecosystem version")

    return res

    #

    #

    # #
    # #

    #
    #
    # if data['response'].lower() == "ok":
    #     app.logger.info('Response key validation started')
    #     app.logger.info('Response key validation is successful, response value  displayed as "OK"')
    # else:
    #     app.logger.info('Response key validation is not successful, response is not displayed as "OK"')

    # Extract data from request
    # ver = request.json['ver']
    # txnid = request

    # Perform necessary actions with data (e.g. save to database)
    # ...

    # Construct response
    # response_data = {
    #     'ver': "ver",
    #     'txnid': "txnid",
    #     'status': 'ok'
    # }
    # return jsonify(response_data)


if __name__ == '__main__':
    app.run(port=8082)
