package api_endpoints;

import static io.restassured.RestAssured.given;

import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class VerificationApi 
{

	 public static Response getVerification(String osid) {
	        String url = "http://localhost:8090/api/v1/Verification/" + osid;

	        Response response = given()
	                .contentType(ContentType.JSON).header("Accept", "application/json")
	                .when()
	                .get(url);

	        return response;
	    }
	 
	 public static Response getVerificationUsingInvalidEndpoints(String osid) 
	 {
	        String url = "http://localhost:8090/api/v1/Verificationn/" + osid;

	        Response response = given()
	                .contentType(ContentType.JSON).header("Accept", "application/json")
	                .when()
	                .get(url);

	        return response;
	    }
}
