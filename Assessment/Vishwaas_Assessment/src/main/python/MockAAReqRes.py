import psycopg2
import json
import uuid
from Database import DbConnection as db
import Constants as cons


class ConsentHandler:
    def __init__(self, request):
        self.request = request
        self.response = {}

    def process_request(self):
        self.response["ver"] = self.request["ver"]
        self.response["timestamp"] = self.request["timestamp"]
        self.response["txnid"] = self.request["txnid"]
        self.response["Customer"] = self.request["ConsentDetail"]["Customer"]
        self.response["ConsentHandle"] = str(uuid.uuid4())

        # Set the timestamp to consentStart date from the request
        self.response["timestamp"] = self.request["ConsentDetail"]["consentStart"]

    def get_response(self):
        conn = db.get_connection()
        cur = conn.cursor()

        # Convert UUID to string representation
        response_id = str(uuid.uuid4())

        # Insert the response into the database
        cur.execute(
            f"""
            INSERT INTO {cons.Constants.MOCK_AA_REQ_RES} (id, requestdata, responsedata)
            VALUES (%s, %s, %s);
            """,
            (
                response_id,
                json.dumps(self.request),
                json.dumps(self.response),
            ),
        )

        conn.commit()
        cur.close()
        conn.close()

        return self.response


# Example request
request = {
    "ver": "1.0",
    "timestamp": "2023-06-02T05:22:14.177Z",
    "txnid": "4a4adbbe-29ae-11e8-a8d7-0289437bf331",
    "ConsentDetail": {
        "consentStart": "2019-12-06T11:39:57.153Z",
        "consentExpiry": "2019-12-06T11:39:57.153Z",
        "consentMode": "VIEW",
        "fetchType": "ONETIME",
        "consentTypes": ["PROFILE"],
        "fiTypes": ["DEPOSIT"],
        "DataConsumer": {"id": "fiu7465374537id"},
        "Customer": {"id": "customer_identifier@AA_identifier"},
        "Purpose": {
            "code": "101",
            "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
            "text": "Wealth management service",
            "Category": {"type": "string"}
        },
        "FIDataRange": {
            "from": "2018-12-06T11:39:57.153Z",
            "to": "2019-12-06T11:39:57.153Z"
        },
        "DataLife": {"unit": "MONTH", "value": 0},
        "Frequency": {"unit": "HOUR", "value": 1},
        "DataFilter": [{
            "type": "TRANSACTIONAMOUNT",
            "operator": ">=",
            "value": "20000"
        }]
    }
}

consent_handler = ConsentHandler(request)
consent_handler.process_request()
response = consent_handler.get_response()
print(response)


class ConsentHandler:
    def __init__(self, request):
        self.request = request
        self.response = {}

    def process_request(self):
        self.response["ver"] = "1.0"
        self.response["timestamp"] = "2018-12-06T11:39:57.153Z"
        self.response["txnid"] = str(uuid.uuid4())
        self.response["ConsentHandle"] = str(uuid.uuid4())
        self.response["ConsentStatus"] = {
            "id": str(uuid.uuid4()),
            "status": "READY"
        }

    def get_response(self):
        return self.response


# Example request
request = {
    "ver": "1.0",
    "timestamp": "2023-06-02T05:22:14.177Z",
    "txnid": "4a4adbbe-29ae-11e8-a8d7-0289437bf331",
    "ConsentDetail": {
        "consentStart": "2019-12-06T11:39:57.153Z",
        "consentExpiry": "2019-12-06T11:39:57.153Z",
        "consentMode": "VIEW",
        "fetchType": "ONETIME",
        "consentTypes": ["PROFILE"],
        "fiTypes": ["DEPOSIT"],
        "DataConsumer": {"id": "fiu7465374537id"},
        "Customer": {"id": "customer_identifier@AA_identifier"},
        "Purpose": {
            "code": "101",
            "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
            "text": "Wealth management service",
            "Category": {"type": "string"}
        },
        "FIDataRange": {
            "from": "2018-12-06T11:39:57.153Z",
            "to": "2019-12-06T11:39:57.153Z"
        },
        "DataLife": {"unit": "MONTH", "value": 0},
        "Frequency": {"unit": "HOUR", "value": 1},
        "DataFilter": [{
            "type": "TRANSACTIONAMOUNT",
            "operator": ">=",
            "value": "20000"
        }]
    }
}

consent_handler = ConsentHandler(request)
consent_handler.process_request()
response = consent_handler.get_response()
print(response)
