package api_endpoints;
import static io.restassured.RestAssured.given ;

import org.json.JSONObject;


import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class certificate
{
	public static Response Create_user(String jsonData)
	{
		Response response = given().contentType(ContentType.JSON).log().all().body(jsonData)
		.when()
		.post(Routes.Certificate_url);
		
		return response;
		
	}
	
	public static Response Create_User_using_invalidEndpoints(String jsonData)
	{
		Response response = given().contentType(ContentType.JSON).log().all().body(jsonData)
				.when()
				.post(Routes.Invalid_url);
				
				return response;
				
		
	}
	
	
}
