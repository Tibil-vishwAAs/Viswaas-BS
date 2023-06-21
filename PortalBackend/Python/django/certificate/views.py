import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import request as rq
from .constants import header,generate_token_payload,generate_token_url,certificate_header,get_request_method,post_request_method,data,Authorization,Bearer,signedCredentials,_osSignedData,access_token
from .config_reader import read_config


config = read_config()
generate_token_url = config.get('URL', 'generate_token_url')
certificate_url = config.get('URL', 'certificate_url')
verify_certificate_url = config.get('URL', 'verify_certificate_url')


def call_api(**kwargs):
    http_method = kwargs.get('http_method')
    http_url = kwargs.get('http_url')
    http_headers = kwargs.get('http_header')
    http_payload = kwargs.get('http_payload')
    response = rq(http_method, http_url, headers=http_headers, data=http_payload)
    if response.status_code == 200:
        response_data = {"status_code": response.status_code,
                         "data": response.json()  
                         }
        return response_data
    else:
        return Response({'error': 'Something went wrong'},
                        status=response.status_code)  


def generate_tokens():
    api_response = call_api(http_method=post_request_method, http_url=generate_token_url, http_header=header,
                            http_payload=generate_token_payload)
    return api_response


def get_entity(access_token):
    header[Authorization] = Bearer + access_token
    certificate_response = call_api(http_method=get_request_method, http_url=certificate_url, http_header=header)
    return certificate_response


def create_certificate(data, access_token):
    certificate_header[Authorization] = Bearer + access_token
    response = call_api(http_method=post_request_method, http_url=certificate_url, http_header=certificate_header,
                        http_payload=data)
    return response


class Certificate(APIView):
    def post(self, request):
        get_token = generate_tokens()  
        token = get_token[data][access_token]
        get_the_entity = get_entity(token)
        if isinstance(get_the_entity[data], list):
            flag = False
            for i in get_the_entity[data]:
                if i['name'] == request.data['name'] and i['certificateid'] == request.data['certificateid'] and i[
                    'entitytype'] == request.data['entitytype'] and i['rebitversion'] == request.data[
                    'rebitversion'] and i['purposecode'] == request.data['purposecode'] and i['fitype'] == request.data[
                    'fitype'] and i['expired'] == request.data['expired']:
                    flag = True
                    break
            if flag:
                return Response({'message': "Certificate already exists"}, status=status.HTTP_409_CONFLICT)
            elif flag == False:
                response = create_certificate(json.dumps(request.data), token)
                return Response({"message": "Certificate created", "response": response}, status=status.HTTP_200_OK)
        elif get_the_entity['status_code'] == 404:
            response = create_certificate(json.dumps(request.data), token)
            return Response({"message": "Certificate created", "response": response}, status=status.HTTP_200_OK)


def get_entity_by_id(certificate_id, access_token):
    certificate_header[Authorization] = Bearer + access_token
    response = call_api(http_method=get_request_method, http_url=certificate_url + "/" + certificate_id, http_header=certificate_header)
    return response


def verify_certificate(access_token, payload):
    certificate_header[Authorization] = Bearer + access_token
    response = call_api(http_method=post_request_method, http_url=verify_certificate_url, http_header=certificate_header,
                        http_payload=payload)
    return response


class Verification(APIView):

    def get(self, request, certificate_id):
        get_token = generate_tokens()
        token = get_token[data][access_token]
        get_the_entity = get_entity_by_id(certificate_id, token)
        unescaped_data = {
            signedCredentials : json.loads(get_the_entity[data][_osSignedData])
        }
        payload = json.dumps(unescaped_data)
        response = verify_certificate(token, payload)
        return Response({"Message:": "Certificate verified", "response": response[data]}, status=status.HTTP_200_OK)
