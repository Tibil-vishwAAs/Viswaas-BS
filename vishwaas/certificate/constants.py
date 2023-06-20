generate_token_payload = {
    "client_id": "registry-frontend",
    "username": "1234567890",
    "password": "abcd@123",
    "grant_type": "password"
}

header = {'content-type': "application/x-www-form-urlencoded"}
certificate_header = {"Content-Type": "application/json"}
generate_token_url = "http://keycloak:8080/auth/realms/sunbird-rc/protocol/openid-connect/token"


data = 'data'


