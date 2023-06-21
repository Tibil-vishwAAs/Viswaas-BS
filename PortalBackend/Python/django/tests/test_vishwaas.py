from configparser import ConfigParser


config = ConfigParser()
config.read('/home/pavan/projects/Testing/vishwaas/certificate/config.ini')

generate_token_url = config.get('URL', 'generate_token_url')
certificate_url = config.get('URL', 'certificate_url')
verify_certificate_url = config.get('URL', 'verify_certificate_url')

from certificate.views import *     
from .test_constants import *

get_token = call_api(http_method=post_request_method,http_url=generate_token_url,http_header=header,http_payload=generate_token_payload)

def test_endpoint_validation():
    access_token = get_token['data']['access_token']             
    response = get_entity(access_token)
    assert response['status_code'] == 200        
    print(f"Testcase - Valid endpoint test : {generate_token_url} is a valid end-pont with the status code of {response['status_code']}")

def test_generate_token():
    response = generate_tokens()
    assert response['status_code'] == 200           
    print(f"Testcase - Generate token test : Token is generated with the status code of {response['status_code']}")

def test_get_certificate():
    access_token = get_token['data']['access_token']    
    response = get_entity(access_token)
    assert response['status_code'] == 200           
    print(f"Testcase - Get entity test : Got all the certificates with the status code of {response['status_code']}")

def test_create_certificate():
    access_token = get_token['data']['access_token']          
    response = create_certificate(json.dumps(create_certificate_body),access_token)
    assert response['status_code'] == 200           
    print(f"Testcase - Create certificate : Certificate is created with the status code of {response['status_code']}")

def test_verify_certificate():
    access_token = get_token['data']['access_token']              
    response =verify_certificate(access_token,json.dumps(verify_certificate_payload))
    assert response['status_code'] == 200                          
    print(f"Testcase - Verify certificate : Certificate is verified with the status code of {response['status_code']}")

