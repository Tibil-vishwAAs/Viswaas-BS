from flask import Flask, request, jsonify
import logging
import requests
import json
from MockAAGetSet import *
from Database import DbConnection as db
# from  MockAAHandler import *

app = Flask(__name__)

conn = db.get_connection()
cur = conn.cursor()

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


@app.route('/consent', methods=['POST'])
def consent_request():
    # app.logger.info("Post/Consent will Raise the consent request.")
    request_body = request.get_json()

    # request_body =

    # headers = {
    #     'Content-Type': 'application/json'
    # }

    # Extracting required data from the request body
    ver = request_body['ver']
    customer_id = request_body['ConsentDetail']['Customer']['id']
    timestamp = request_body['timestamp']
    txnid = request_body['txnid']
    # stored_consent_handle = request_body['ConsentHandle']

    # Creating the response body
    response_body = {
        "ver": ver,
        "Customer": {
            "id": customer_id
        },
        "ConsentHandle": "39e108fe-9243-11e8-b9f2-0256d88baae8",
        "timestamp": timestamp,
        "txnid": txnid
    }

    # app.logger.info("Send the request as received from post/consent.")
    import requests
    import json

    url = "http://127.0.0.1:8082/consent/request"

    payload = json.dumps({
        "ver": "1.0",
        "timestamp": "2023-05-29T07:48:51.054Z",
        "txnid": "4a4adbbe-29ae-11e8-a8d7-0289437bf331",
        "ConsentDetail": {
            "consentStart": "2019-12-06T11:39:57.153Z",
            "consentExpiry": "2019-12-06T11:39:57.153Z",
            "consentMode": "VIEW",
            "fetchType": "ONETIME",
            "consentTypes": [
                "PROFILE"
            ],
            "fiTypes": [
                "DEPOSIT"
            ],
            "DataConsumer": {
                "id": "fiu7465374537id"
            },
            "Customer": {
                "id": "customer_identifier@AA_identifier"
            },
            "Purpose": {
                "code": "101",
                "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
                "text": "Wealth management service",
                "Category": {
                    "type": "string"
                }
            },
            "FIDataRange": {
                "from": "2018-12-06T11:39:57.153Z",
                "to": "2019-12-06T11:39:57.153Z"
            },
            "DataLife": {
                "unit": "MONTH",
                "value": 0
            },
            "Frequency": {
                "unit": "HOUR",
                "value": 1
            },
            "DataFilter": [
                {
                    "type": "TRANSACTIONAMOUNT",
                    "operator": ">=",
                    "value": "20000"
                }
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())

    return jsonify(response_body)

    # consentHandle = response_body['ConsentHandle']
    # url = "http://127.0.0.1:5000/Consent/handle/" + consentHandle
    # response = requests.get(url)
    # response_data = response.json()
    # print(response_data)

    # return jsonify(response_body)

    # url = "http://127.0.0.1:5000/Consent/handle/" + consentHandle
    # response = requests.get(url)
    #
    # print(response)
    # return jsonify({'message': 'POST API response'})


@app.route('/consent/handle/<consent_handle>', methods=['GET'])
def get_consent_handle(consent_handle):
    """
    It will
    """
    # consentHandle = "39e108fe-9243-11e8-b9f2-0256d88baae8"
    # print(consent_handle)
    # print(consent_handle)
    # consent_handle = request.view_args['consent_handle']
    # if consentHandle == data['consentHandle']:

    # url = "http://127.0.0.1:8082/consent/handle/request"
    # response = requests.get(url=url)
    # print(response)

    # logger.info("Send the request as received from post/consent/handle.")

    url = "http://127.0.0.1:8082/consent/handle/request"
    # data = request.get_json()

    # Do not hardcode Send consent_handle as it is received [Addt]
    payload = json.dumps({
        "ver": "1.0",
        "timestamp": "2023-05-29T07:48:51.054Z",
        "txnid": "4a4adbbe-29ae-11e8-a8d7-0289437bf331",
        "ConsentDetail": {
            "consentStart": "2019-12-06T11:39:57.153Z",
            "consentExpiry": "2019-12-06T11:39:57.153Z",
            "consentMode": "VIEW",
            "fetchType": "ONETIME",
            "consentTypes": [
                "PROFILE"
            ],
            "fiTypes": [
                "DEPOSIT"
            ],
            "DataConsumer": {
                "id": "fiu7465374537id"
            },
            "Customer": {
                "id": "customer_identifier@AA_identifier"
            },
            "Purpose": {
                "code": "101",
                "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
                "text": "Wealth management service",
                "Category": {
                    "type": "string"
                }
            },
            "FIDataRange": {
                "from": "2018-12-06T11:39:57.153Z",
                "to": "2019-12-06T11:39:57.153Z"
            },
            "DataLife": {
                "unit": "MONTH",
                "value": 0
            },
            "Frequency": {
                "unit": "HOUR",
                "value": 1
            },
            "DataFilter": [
                {
                    "type": "TRANSACTIONAMOUNT",
                    "operator": ">=",
                    "value": "20000"
                }
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    # seperrate class  or file approach

    # Status = "Ready"

    # mockAaResponseObj.getResponse()
    Status = mockAaResponseObj.getResponse("status")

    # Share the data received from /consent/handle
    response = requests.request("POST", url, headers=headers, data=payload)

    # if response.status_code == 200:
    #     Status = "Pending"
    # else:
    #     Status = "Ready"

    print(response)
    print(response.json())

    # statusJson = mockAaResponseObj.getResponse()

    response = {
        "ver": "1.0",
        "timestamp": "2018-12-06T11:39:57.153Z",
        "txnid": "795038d3-86fb-4d3a-a681-2d39e8f4fc3c",
        "ConsentHandle": consent_handle,
        "ConsentStatus": {
            "id": "654024c8-29c8-11e8-8868-0289437bf3x31",
            # "status": statusJson['status']
            "status": Status
        }
    }



    return response


# def set_consent_handle_request():
#     url = "http://127.0.0.1:5000/consent/handle/39e108fe-9243-11e8-b9f2-0256d88baae8"  # Replace <consent_handle> with the actual consent handle value
#
#     response = requests.get(url=url)
#     print("Response of Consent handle status")
#     print(response)
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


# payload = json.dumps({
#     "ver": "1.0",
#     "timestamp": "2023-05-29T07:48:51.054Z",
#     "txnid": "4a4adbbe-29ae-11e8-a8d7-0289437bf331",
#     "ConsentDetail": {
#         "consentStart": "2019-12-06T11:39:57.153Z",
#         "consentExpiry": "2019-12-06T11:39:57.153Z",
#         "consentMode": "VIEW",
#         "fetchType": "ONETIME",
#         "consentTypes": ["PROFILE"],
#         "fiTypes": ["DEPOSIT"],
#         "DataConsumer": {"id": "fiu7465374537id"},
#         "Customer": {"id": "customer_identifier@AA_identifier"},
#         "Purpose": {
#             "code": "101",
#             "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
#             "text": "Wealth management service",
#             "Category": {"type": "string"}
#         },
#         "FIDataRange": {
#             "from": "2018-12-06T11:39:57.153Z",
#             "to": "2019-12-06T11:39:57.153Z"
#         },
#         "DataLife": {"unit": "MONTH", "value": 0},
#         "Frequency": {"unit": "HOUR", "value": 1},
#         "DataFilter": [
#             {"type": "TRANSACTIONAMOUNT", "operator": ">=", "value": "20000"}
#         ]
#     }
# })
# headers = {
#     'Content-Type': 'application/json'
# }


# Call the function to set the Consent Handle request response


# else:
#     return {'message': 'Invalid consentHandle ID'}


@app.route('/Consent/Notification/Trigger', methods=['POST'])
def trigger_consent_notification():
    """
    Triggers the /consent/notification
    :returns /consent/notification response.
    """

    import requests
    import json

    url = "http://127.0.0.1:5000/consent/notification"

    payload = json.dumps({
        "ver": "1.0",
        "timestamp": "2018-12-06T11:39:57.153Z",
        "txnid": "0b811819-9044-4856-b0ee-8c88035f8858",
        "Notifier": {
            "type": "AA",
            "id": "AA-1"
        },
        "ConsentStatusNotification": {
            "consentId": "XXXX0-XXXX-XXXX",
            "consentHandle": "39e108fe-9243-11e8-b9f2-0256d88baae8",
            "consentStatus": "PAUSED"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.json()


if __name__ == '__main__':
    app.run(port=5001)

# import json
#
# import requests
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
#
# @app.route('/consent', methods=['POST'])
# def handle_consent_request():
#     # url = "http://127.0.0.1:5001/consent"
#     payload = json.dumps({
#         "ConsentDetail": {
#             "Customer": {
#                 "id": "<string>"
#             },
#             "DataConsumer": {
#                 "id": "<string>"
#             },
#             "DataLife": {
#                 "unit": "INF",
#                 "value": "<number>"
#             },
#             "FIDataRange": {
#                 "from": "<dateTime>",
#                 "to": "<dateTime>"
#             },
#             "Frequency": {
#                 "unit": "DAY",
#                 "value": "<number>"
#             },
#             "Purpose": {
#                 "code": "<string>",
#                 "refUri": "<string>",
#                 "text": "<string>",
#                 "Category": {
#                     "type": "<string>"
#                 }
#             },
#             "consentExpiry": "<dateTime>",
#             "consentMode": "STORE",
#             "consentStart": "<dateTime>",
#             "consentTypes": [
#                 "TRANSACTIONS"
#             ],
#             "fetchType": "ONETIME",
#             "fiTypes": [
#                 "REIT"
#             ],
#             "DataFilter": [
#                 {
#                     "operator": ">=",
#                     "type": "TRANSACTIONAMOUNT",
#                     "value": "<string>"
#                 },
#                 {
#                     "operator": "!=",
#                     "type": "TRANSACTIONAMOUNT",
#                     "value": "<string>"
#                 }
#             ]
#         },
#         "timestamp": "<dateTime>",
#         "txnid": "<string>",
#         "ver": "<string>"
#     })
#     headers = {
#         'x_jws_signature': '<string>',
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'client_api_key': '{{apiKey}}'
#     }
#
#     # Process the payload and perform the desired actions
#     # ...
#
#     # Example response
#     # response_data = {'message': 'Consent request processed successfully'}
#     response_data = requests.request("POST",url=url, headers=headers, data=payload)
#     return jsonify(response_data)
#
#
# if __name__ == '__main__':
#     app.run(port=5001)
